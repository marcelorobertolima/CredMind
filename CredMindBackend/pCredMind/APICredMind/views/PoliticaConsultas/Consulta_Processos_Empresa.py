import requests
import json

import io
import base64
from io import BytesIO

from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, PageBreak
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch

from rest_framework.response import Response
from rest_framework import status
from APICredMind.views.funcoesGerais import GeraIDs
from APICredMind.views.dadosTestes import dadosTeste_RelatorioProcessos
from APICredMind.views.dadosTestes import dadosTeste_BureauProcessos

from datetime import datetime
from APICredMind.serializers import ConsultasSerializer
from APICredMind.serializers import RelatoriosSerializer

from APICredMind.configAPICredMind import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from openai import OpenAI
import os

################################################################################################
################################################################################################
################################################################################################
class ConsultaProcessosEmpresa(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        try:
            cnpj = request.data.get('cnpj')
            idAnalise = request.data.get('idAnalise')

            print(cnpj)

            auth_header = request.headers.get('Authorization')

            if not auth_header:
                return Response({"error": "Não Autorizado!"}, status=status.HTTP_401_UNAUTHORIZED)

            if not cnpj:
                return Response({"error": "CNPJ obrigatório!"}, status=status.HTTP_400_BAD_REQUEST)

            ProcessosEmpresa = ConsultaProcessosEmpresa.consultarProcessosEmpresa(cnpj, auth_header, idAnalise)
            
            return Response(ProcessosEmpresa, status=status.HTTP_200_OK)
        except requests.exceptions.RequestException as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    ################################################################################################
    ################################################################################################
    ################################################################################################
    def consultarProcessosEmpresa(cnpj,
                                  auth,
                                  idAnalise=None):
        try:
            cnpjRegra = cnpj

            #Teste do HTML
            #DadosBureau = dadosTeste_RelatorioProcessos()
            #relatorioHTML = ConsultaProcessosEmpresa.gerarRelatorioHTML(DadosBureau)
            #return relatorioHTML

            if AMBIENTE == 'PRD':
                # URL da sua API interna
                url_interna = URL_APIs + 'consultaDadosEmpresa'
                auth_header = auth

                headers = {
                    'Content-Type': 'application/json',
                    'Authorization': auth_header,
                }
                
                data = {
                    "cnpj": cnpjRegra,
                    "linhaBDC": "",
                    "dataSet": "processes, basic_data"
                }

                Response = requests.get(url_interna, headers=headers, json=data)

                conteudo_json = Response.text
                DadosBureau = json.loads(conteudo_json)
            else:
                data = {
                    "cnpj": cnpjRegra,
                    "linhaBDC": "",
                    "dataSet": "TESTE"
                }

                #Falta implementar a string de teste de process
                DadosBureau = dadosTeste_BureauProcessos()

            idConsulta = GeraIDs()

            print("Dados Bureau ==>>", DadosBureau)

            ############################################################
            #Gravacao na base
            ############################################################
            DadosConsulta = {
                'id_consulta': idConsulta,
                'id_analise': idAnalise,
                'DataConsulta': datetime.now(),
                'Bureau': 'BigDataCorp-Processos-Empresa',
                'Request': json.dumps(data),  # Converte para string JSON
                'Response': json.dumps(DadosBureau)  # Converte para string JSON
            }

            consultasSerializer = ConsultasSerializer(data=DadosConsulta)

            if consultasSerializer.is_valid():
                consultasSerializer.save()
            ############################################################
            #Gravacao na base
            ############################################################

            relatorioProcessos = ConsultaProcessosEmpresa.gerarRelatorioProcessos(DadosBureau)

            ############################################################
            #Gravacao do relatório
            ############################################################
            DadosRelatorio = {
                'id_consulta': idConsulta,
                'id_analise': idAnalise,
                'Data': datetime.now(),
                'CNPJ': cnpjRegra,
                'Relatorio': json.dumps(relatorioProcessos),
                'RelatorioPDF': next((item['RelatorioPDF'] for item in relatorioProcessos if 'RelatorioPDF' in item), None)
            }

            dadosRelatoriosSerializer = RelatoriosSerializer(data=DadosRelatorio)

            if dadosRelatoriosSerializer.is_valid():
                dadosRelatoriosSerializer.save()
            ############################################################
            #Gravacao na base
            ############################################################

            if relatorioProcessos:
                return relatorioProcessos
            else:
                return "Não existem processos para o CNPJ informado!"
        except requests.exceptions.RequestException as e:
            return f"RequestException occurred: {e}"

    ################################################################################################
    ################################################################################################
    ################################################################################################
    def gerarRelatorioProcessos(processosBureau):
        dadosProcessosResult = processosBureau.get("DadosEmpresa", {}).get("Result", [])

        #Pega dados basicos da empresa
        dadosBasicosBureau = dadosProcessosResult[0].get("BasicData", {})
        dadosBasicosRelatorio = {
            "CNPJ": dadosBasicosBureau.get('TaxIdNumber'),
            "RazaoSocial": dadosBasicosBureau.get('OfficialName')
        }

        #Pega dados dos processos
        dadosProcessosBureau = dadosProcessosResult[0].get("Lawsuits", {}).get("Lawsuits", [])

        dadosProcResumido = []

        # Lista de palavras para buscar
        palavras_chave = ["FIDC", 
                          "FUNDO", 
                          "Fundo", 
                          "fundo", 
                          "Investimento",
                          "Securitizadora", 
                          "Sec.", 
                          "SEC", 
                          "Secur.", 
                          "Securit."]

        for processo in dadosProcessosBureau:
            #Verificar se o JSON contém alguma das palavras-chave
            TemPalavraChave = ConsultaProcessosEmpresa.possuiPalavraChave(processo, palavras_chave)

            if TemPalavraChave:
                proc = {
                        "Number": processo.get("Number"),
                        "Type": processo.get("Type"),
                        "MainSubject":  processo.get("MainSubject"),
                        "CourtName": processo.get("CourtName"),
                        "CourtLevel": processo.get("CourtLevel"),
                        "CourtType": processo.get("CourtType"),
                        "CourtDistrict": processo.get("CourtDistrict"),
                        "Judge": processo.get("Judge"),
                        "JudgingBody": processo.get("JudgingBody"),
                        "State": processo.get("State"),
                        "Status": processo.get("Status"),
                        "LawsuitHostService": processo.get("LawsuitHostService"),
                        "InferredCNJSubjectName": processo.get("InferredCNJSubjectName"),
                        "InferredCNJSubjectNumber": processo.get("InferredCNJSubjectNumber"),
                        "InferredCNJProcedureTypeName": processo.get("InferredCNJProcedureTypeName"),
                        "InferredBroadCNJSubjectName": processo.get("InferredBroadCNJSubjectName"),
                        "InferredBroadCNJSubjectNumber": processo.get("InferredBroadCNJSubjectNumber"),
                        "OtherSubjects": processo.get("OtherSubjects"),
                        "NumberOfVolumes": processo.get("NumberOfVolumes"),
                        "NumberOfPages": processo.get("NumberOfPages"),
                        "Value": processo.get("Value"),
                        "ResJudicataDate": processo.get("ResJudicataDate"),
                        "CloseDate": processo.get("CloseDate"),
                        "PublicationDate": processo.get("PublicationDate"),
                        "NoticeDate": processo.get("NoticeDate"),
                        "LastMovementDate": processo.get("LastMovementDate"),
                        "CaptureDate": processo.get("CaptureDate"),
                        "LastUpdate": processo.get("LastUpdate"),
                        "NumberOfUpdates": processo.get("NumberOfUpdates"),
                        "LawSuitAge": processo.get("LawSuitAge"),
                        "AverageNumberOfUpdatesPerMonth": processo.get("AverageNumberOfUpdatesPerMonth"),
                        "ReasonForConcealedData": processo.get("ReasonForConcealedData"),
                        "Parties": processo.get("Parties"),
                        "Updates": ConsultaProcessosEmpresa.get_last_n_items(processo.get("Updates", []), 5),
                        "Petitions": ConsultaProcessosEmpresa.get_last_n_items(processo.get("Petitions", []), 5),
                        "Decisions": ConsultaProcessosEmpresa.get_last_n_items(processo.get("Decisions", []), 5),
                }

                dadosProcResumido.append(proc)

        dadosProcessos = []

        if dadosProcResumido:
            chatGPT_APIKey = "sk-6fWB-ULhYgYVOgRz7A_aYRyJlWvXRqtJ0pPUUDIk-TT3BlbkFJ9s-jaASW32_bARG5x_G2UozBQQ6pwZ9mttkepI7O4A"
            chatGPT = OpenAI(api_key=os.environ.get("OPENAI_API_KEY", chatGPT_APIKey))

            #Loop por processo, solicitando ao GPT analise
            #Montar Relatório final para devolver
            for DadosProcesso in dadosProcResumido:
                prompt = (
                            "Analise o processo judicial abaixo e determine qual polo, ou seja ativo ou passivo o CNPJ: {cnpjRegra} é, "
                            "verifique também se há menções a FUNDO, Investimento, FIDC, Securitizadora. "
                            "Liste esses dados citando o numero do processo (number), o tipo do processo, o MainSubject," 
                            "o tipo da corte e se há as menções que coloquei acima. "
                            "Insira também um resumo com o valor da ação e o seus status atual, ou seja, em tramite, arquivada, etc. "
                            "Insira a data da ultima movimentação e um resumo do que aconteceu nesta ultima movimentação. "
                            "O retorno deve ser somente um json valido (pois será realizando um append numa variável [] no Python)" 
                            " com os seguintes campos e estrutura: "
                            "{"
                            "	Number: ,"
                            "	CourtType: ,"
                            "	Status: ,"
                            "	Value: 0 ,"
                            "	LastMovementDate: ,"
                            "	LastMovement: ,"
                            "	Summary: ,"
                            "	Parties: ["
                            "		{"
                            "			Type: ,"
                            "			Name: ,"
                            "			Doc: ,"
                            "			Polarity: ,"
                            "			IsCNPJConsulta: "
                            "		}"
                            "	]"
                            "	Mentions: {"
                            "		FUNDO: ,"
                            "		FIDC: ,"
                            "		Sec: ,"
                            "		Securitizadora: "
                            "	},"
                            "	Resumo: {"
                            "		Processo: ,"
                            "		Tipo: ,"
                            "		AssuntoPrincipal: ,"
                            "		TipoDaCorte: ,"
                            "		Status: ,"
                            "		Valor: ,"
                            "		DataDaUltimaMovimentacao: ,"
                            "		UltimaMovimentacao: "
                            "	}"
                            "} \n\n"
                            "Por favor só retorne o json, nada mais do que isso."
                            f"{DadosProcesso}"
                )

                MODEL = "gpt-4o-mini"
                response = chatGPT.chat.completions.create(
                    model=MODEL,
                    messages=[
                        {"role": "user", "content": prompt},
                    ],
                    temperature=0,
                )

                response_content = response.choices[0].message.content
                json_string = response_content.strip("```json\n")

                relatorioProcessos = json.loads(json_string)

                dadosProcessos.append(relatorioProcessos)
        
        print("RelatorioFinal:", json.dumps(dadosProcessos))

        #Gera PDF e HTML
        #pdf_base64 = ConsultaProcessosEmpresa.gerarRelatorioPDF(dadosBasicosRelatorio, dadosProcessos)
        relatorioHTML = ConsultaProcessosEmpresa.gerarRelatorioHTML(dadosBasicosRelatorio, dadosProcessos)

        #dadosProcessos.append({"RelatorioPDF": pdf_base64})
        dadosProcessos.append({"RelatorioHTML": relatorioHTML})

        #Retorna dos dados que estarão no HTML
        retornoDadosProcessos = {
            "DadosEmpresa": dadosBasicosRelatorio,
            "DadosProcessos": dadosProcessos
        }

        #Retorna Relatório Final
        return retornoDadosProcessos

    ################################################################################################
    ################################################################################################
    ################################################################################################
    # Função para verificar se alguma palavra-chave está presente no JSON
    def possuiPalavraChave(data, palavras_chave):
        if isinstance(data, dict):
            for key, value in data.items():
                if any(palavra in key for palavra in palavras_chave):
                    return 1
                if ConsultaProcessosEmpresa.possuiPalavraChave(value, palavras_chave) == 1:
                    return 1
        elif isinstance(data, list):
            for item in data:
                if ConsultaProcessosEmpresa.possuiPalavraChave(item, palavras_chave) == 1:
                    return 1
        elif isinstance(data, str):
            if any(palavra in data for palavra in palavras_chave):
                return 1
        return 0

    def get_last_n_items(data_list, n):
        return data_list[-n:]

    ################################################################################################
    ################################################################################################
    ################################################################################################
    def gerarRelatorioPDF(  dadosBasicos,
                            dadosProcessos):
        buffer = io.BytesIO()
        doc = SimpleDocTemplate(buffer, pagesize=letter, leftMargin=40, rightMargin=40)
        elements = []
        styles = getSampleStyleSheet()

        for idx, process in enumerate(dadosProcessos):
            process_data = process.get("Process", {})

            # Adicionar quebra de página, exceto antes do primeiro processo
            if idx > 0:
                elements.append(PageBreak())

            # Cabeçalho do Processo
            elements.append(Paragraph(f"Process Number: {process_data.get('Number', '')}", styles['Heading2']))

            # Seção de Sumário (Summary)
            summary_data = process_data.get("Summary", {})
            summary = summary_data.get("Description", "") if isinstance(summary_data, dict) else ""

            if summary:
                elements.append(Spacer(1, 12))  # Espaço antes do resumo
                elements.append(Paragraph("Summary:", styles['Heading3']))
                elements.append(Paragraph(summary, styles['BodyText']))
                elements.append(Spacer(1, 12))

            # Preenchendo os dados da tabela principal
            main_table_data = [
                ["Campo", "Valor"],
                ["Court Type", str(process_data.get("CourtType", ""))],
                ["Status", str(process_data.get("Status", ""))],
                ["Value", str(process_data.get("Value", ""))],
                ["Last Movement Date", str(process_data.get("LastMovementDate", ""))],
                ["Last Movement Summary", str(process_data.get("LastMovementSummary", ""))]
            ]

            # Definindo a tabela principal
            main_table = Table(main_table_data, colWidths=[2 * inch, 4 * inch], hAlign='LEFT')

            # Definindo estilos da tabela principal
            main_table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.grey),  # Cor de fundo do cabeçalho
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),  # Cor do texto do cabeçalho
                ('ALIGN', (0, 0), (-1, -1), 'LEFT'),  # Alinhamento do texto
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),  # Fonte do cabeçalho
                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),  # Padding do cabeçalho
                ('BACKGROUND', (0, 1), (-1, -1), colors.beige),  # Cor de fundo das linhas
                ('GRID', (0, 0), (-1, -1), 1, colors.black),  # Grade da tabela
            ]))

            # Preenchendo as células com Parágrafos
            for i in range(len(main_table_data)):
                if i > 0:  # Ignora a linha do cabeçalho
                    main_table._cellvalues[i][1] = Paragraph(str(main_table_data[i][1]), styles['BodyText'])

            elements.append(main_table)
            elements.append(Spacer(1, 12))

            # Seção de Parties
            parties = process_data.get("Parties", [])
            if isinstance(parties, list):  # Verifica se parties é uma lista
                # Cabeçalho da tabela de parties
                parties_table_data = [["Type", "Name", "Document", "Polarity"]]
                # Preencher dados das parties
                for party in parties:
                    parties_table_data.append([
                        Paragraph(str(party.get("Type", "")), styles['BodyText']),
                        Paragraph(str(party.get("Name", "")), styles['BodyText']),
                        Paragraph(str(party.get("Doc", "")), styles['BodyText']),
                        Paragraph(str(party.get("Polarity", "")), styles['BodyText']),
                    ])
                
                # Definindo a tabela de parties
                parties_table = Table(parties_table_data, colWidths=[1.5 * inch, 2.5 * inch, 1.5 * inch, 1 * inch], hAlign='LEFT')

                # Definindo estilos da tabela de parties
                parties_table.setStyle(TableStyle([
                    ('BACKGROUND', (0, 0), (-1, 0), colors.grey),  # Cor de fundo do cabeçalho
                    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),  # Cor do texto do cabeçalho
                    ('ALIGN', (0, 0), (-1, -1), 'LEFT'),  # Alinhamento do texto
                    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),  # Fonte do cabeçalho
                    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),  # Padding do cabeçalho
                    ('BACKGROUND', (0, 1), (-1, -1), colors.beige),  # Cor de fundo das linhas
                    ('GRID', (0, 0), (-1, -1), 1, colors.black),  # Grade da tabela
                    ('VALIGN', (0, 0), (-1, -1), 'TOP'),  # Alinhamento vertical
                ]))

                # Adicionando a tabela de parties ao documento
                elements.append(Paragraph("Parties:", styles['Heading3']))
                elements.append(parties_table)
                elements.append(Spacer(1, 12))
            else:
                print("Parties não é uma lista:", parties)

            # Seção de Menções (Mentions) como tabela
            mentions = process_data.get("Mentions", {})
            if isinstance(mentions, dict):  # Verifica se mentions é um dicionário
                mentions_table_data = [["Mention", "Value"]]
                for k, v in mentions.items():
                    mentions_table_data.append([
                        Paragraph(k, styles['BodyText']),
                        Paragraph("Yes" if v else "No", styles['BodyText'])
                    ])
                
                mentions_table = Table(mentions_table_data, colWidths=[2.5 * inch, 1.5 * inch], hAlign='LEFT')
                mentions_table.setStyle(TableStyle([
                    ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                    ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                    ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                    ('GRID', (0, 0), (-1, -1), 1, colors.black),
                ]))
                
                elements.append(Paragraph("Mentions:", styles['Heading3']))
                elements.append(mentions_table)
                elements.append(Spacer(1, 12))

        # Construir o PDF
        doc.build(elements)
        buffer.seek(0)

        # Converter PDF para base64
        pdf_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
        buffer.close()

        return pdf_base64

    ################################################################################################
    ################################################################################################
    ################################################################################################

    def gerarRelatorioHTML( dadosBasicos,
                            dadosProcessos):
        html_content = f"""
        <!DOCTYPE html>
        <html lang="pt-br">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Processos Judiciais - {dadosBasicos['RazaoSocial']} - CNPJ: {dadosBasicos['CNPJ']}</title>
            <script src="https://cdn.tailwindcss.com"></script>
        </head>
        <body class="bg-gray-100 py-6 px-4">
            <div class="max-w-7xl mx-auto">
                <h1 class="text-3xl font-semibold text-center mb-2">Processos Judiciais</h1>
                <h1 class="text-2xl font-semibold text-center mb-2">Razão Social: {dadosBasicos['RazaoSocial']}</h1>
                <h1 class="text-2xl font-semibold text-center mb-2">CNPJ: {dadosBasicos['CNPJ']}</h1>
                <div class="flex flex-col gap-6">
        """
        
        for processo in dadosProcessos:
            # Convertendo a data para o formato DD/MM/AAAA
            dataFormatada = datetime.strptime(processo['LastMovementDate'], "%Y-%m-%dT%H:%M:%S").strftime("%d/%m/%Y")

            html_content += f"""
                <div class="bg-white p-6 rounded-lg shadow-lg">
                    <div class="mt-4">
                        <span class="inline-block bg-blue-500 text-white text-xl py-1 px-4 rounded-full">Numero Processo: {processo['Number']}</span>
                    </div>
                    <div class="mt-4">
                        <span class="inline-block bg-blue-500 text-white text-xl py-1 px-4 rounded-full">Corte: {processo['CourtType']}</span>
                    </div>
                    <p><strong>Status: </strong> {processo['Status']}</p>
                    <p><strong>Valor: </strong> R$ {processo['Value']}</p>
                    <p><strong>Data Última Movimentação: </strong> {dataFormatada}</p>
                    <p><strong>Última Movimentação: </strong> {processo['LastMovement']}</p>
                    <p><strong>Resumo: </strong> {processo['Summary']}</p>

                    <h3 class="text-xl font-semibold mt-4">Partes:</h3>
                    <ul class="list-disc pl-5">
            """
            
            for parte in processo['Parties']:
                html_content += f"""
                        <li><strong>{parte['Type']}:</strong> {parte['Name']} (CNPJ: {parte['Doc']})</li>
                """
            
            html_content += f"""
                    </ul>
                </div>
            """
        
        html_content += """
                </div>
            </div>
        </body>
        </html>
        """        
        return html_content
