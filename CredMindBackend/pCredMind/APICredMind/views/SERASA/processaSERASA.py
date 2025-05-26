#consultaSERASARelato.py
import requests
import json

import csv

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from APICredMind.views.funcoesGerais import GeraIDs
from APICredMind.views.SERASA.mappingsSERASA import *

from APICredMind.serializers import ConsultasSerializer
from APICredMind.serializers import ProspecSERASASerializer

from APICredMind.views.SERASA.DadosCadastrais_01 import *
from APICredMind.views.SERASA.DadosComerciaisConsolidados_02 import *
from APICredMind.views.SERASA.DadosComerciaisSegmentoConsolidado_02 import *
from APICredMind.views.SERASA.DadosConsultaAlertas_03 import *
from APICredMind.views.SERASA.DadosApontamentos_04 import *
from APICredMind.views.SERASA.DadosMensagensBloco_04 import *
from APICredMind.views.SERASA.DadosRiskScoring_07 import *
from APICredMind.views.SERASA.DadosRiscoCredito_09 import *
from APICredMind.views.SERASA.DadosGastoEstimado_10 import *
from APICredMind.views.SERASA.DadosAlertaIdentidadePJ_11 import *
from APICredMind.views.SERASA.DadosMosaicPJ_12 import *
from APICredMind.views.SERASA.DadosOrgaosPublicos_12 import *
from APICredMind.views.SERASA.DadosPontualidadePagamentos_13 import *
from APICredMind.views.SERASA.DadosRiscoNovasEmpresas_14 import *
from APICredMind.views.SERASA.DadosCapacidadeMensalPagtoPJ_15 import *
from APICredMind.views.SERASA.DadosEnderecosTelefonesAlternativos_28 import *
from APICredMind.views.SERASA.DadosSituacaoFiscal_27 import *
from APICredMind.views.SERASA.DadosFaturamentoEstimado_30 import *
from APICredMind.views.SERASA.DadosPerfilFinanceiro_30 import *
from APICredMind.views.SERASA.DadosHistoricoPagamentoFinanceiroAvancado_32 import *
from APICredMind.views.SERASA.DadosAlertaCadastralEmpresa_60 import *
from APICredMind.views.SERASA.DadosAlertaCadastralSociosAdmin_61 import *
from APICredMind.views.SERASA.DadosIndiceRelacionamentoMercado_30 import *
from APICredMind.views.SERASA.DadosIndicadorRecuperacaoCredito_53 import *
from APICredMind.views.SERASA.DadosAlertScoring_55 import *
from APICredMind.views.SERASA.DadosLimiteCreditoPJ_56 import *
from APICredMind.views.SERASA.DadosInscricaoEstadual_57 import *
from APICredMind.views.SERASA.DadosInformacoesMonitoreGerencieCarteira_08 import *
from APICredMind.views.SERASA.DadosInformacoesSPC_90 import *
from APICredMind.views.SERASA.DadosAnotacoesConsultasSPC_91 import *
from APICredMind.views.SERASA.DadosComportamentoPagamentoSetor_31 import *
from APICredMind.views.SERASA.DadosVendaCartao_70 import *
from APICredMind.views.SERASA.DadosSociosAdministradoresSPC_92 import *
from APICredMind.views.SERASA.DadosAnotacoesConsultasSPCSociosAdministradores_92 import *
from APICredMind.views.SERASA.DadosIndicadorRecuperacaoDividas_58 import *
from APICredMind.views.SERASA.DadosConsultaStringRelatorio_99 import *

from rest_framework.permissions import IsAuthenticated

class processaSERASA(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        try:
            csv_file_path = r"E:\CredMind\SERASA\SERASA.csv"

            # Lê o arquivo CSV diretamente do diretório
            with open(csv_file_path, mode='r', encoding='utf-8') as file:
                decoded_file = file.read().splitlines() 
                       
            # Lê o CSV usando o módulo csv
            reader = csv.DictReader(decoded_file, delimiter=';')

            i = 0

            for row in reader:
                i = i + 1

                idConsulta = GeraIDs()

                DadosBrutos = row.get('ccs_string')

                CNPJ = row.get('cad_cgccpf')

                print(f"#: {i}")
                print(f"CNPJ: {CNPJ}")

                #Quebra a linha para o tratamento dos blocos
                DadosTratados = DadosBrutos.split('#')

                # Lista para armazenar os objetos do JSON
                RetornoSERASA = {'idConsulta': idConsulta}

                for Linha in DadosTratados:
                    TipoLinha = str(Linha[0:1])

                    if TipoLinha == 'L':
                        TipoRegistro = str(Linha[1:7])
                        NomeGrupo, NomeItem = buscaNomesBlocos(TipoRegistro)

                        RetornoBloco = globals()[f'processaBloco{TipoRegistro}'](Linha)

                        # Adicione esta verificação aqui
                        if not isinstance(RetornoBloco, (list, dict)):
                            raise ValueError(f"RetornoBloco esperado como lista ou dicionário, mas recebeu {type(RetornoBloco)}")

                        # Garantir que RetornoBloco é uma lista
                        if isinstance(RetornoBloco, list) and len(RetornoBloco) == 1:
                            RetornoBloco = RetornoBloco[0]

                        # Verificar se o nome do nó pai já está no RetornoSERASA
                        if NomeGrupo not in RetornoSERASA:
                            RetornoSERASA[NomeGrupo] = {}

                        # Atualizar a estrutura do dicionário de retorno com o nome do nó filho
                        if NomeItem not in RetornoSERASA[NomeGrupo]:
                            RetornoSERASA[NomeGrupo][NomeItem] = RetornoBloco
                        else:
                            # Se já existe, converter para lista se necessário e adicionar o novo bloco
                            if isinstance(RetornoSERASA[NomeGrupo][NomeItem], list):
                                RetornoSERASA[NomeGrupo][NomeItem].append(RetornoBloco)
                            else:
                                # Converte o valor existente em lista e adiciona o novo bloco
                                RetornoSERASA[NomeGrupo][NomeItem] = [RetornoSERASA[NomeGrupo][NomeItem], RetornoBloco]
                
                ############################################################
                #Gravacao da consulta geral base
                ############################################################
                DadosConsulta = {
                    'id_consulta': idConsulta,
                    'id_analise': None,
                    'DataConsulta': datetime.now(),
                    'Bureau': 'SERASA-Proc-String',
                    'Request': json.dumps(request.data),  # Serializa o dicionário
                    'Response': json.dumps(RetornoSERASA)  # Serializa o dicionário
                }

                consultasSerializer = ConsultasSerializer(data=DadosConsulta)

                if consultasSerializer.is_valid():
                    consultasSerializer.save()
                ############################################################
                #Gravacao da consulta geral base
                ############################################################

                ############################################################
                #Gravacao dos dados do SERASA
                ############################################################
                DadosCadatrais = RetornoSERASA.get("DadosCadastrais", {})

                print(f"Dados Cadastrais: {DadosCadatrais.get('Contabilizacao', {}).get('CNPJEditado')}")

                DadosSERASA = {
                    'id_consulta': idConsulta,
                    'CNPJ' : DadosCadatrais.get("Contabilizacao", {}).get("CNPJEditado"),
                    'RazaoSocial' :  DadosCadatrais.get("Identificacao", {}).get("RazaoSocial"),
                    'NomeFant' : DadosCadatrais.get("Identificacao", {}).get("NomeFatasia"),
                    
                    'Endereco' : DadosCadatrais.get("Endereco", {}).get("Endereco"),
                    'Bairro' : DadosCadatrais.get("Endereco", {}).get("Bairro"),

                    'Cidade' : DadosCadatrais.get("Localizacao", {}).get("Cidade"),
                    'UF' : DadosCadatrais.get("Localizacao", {}).get("UF"),
                    'CEP' : DadosCadatrais.get("Localizacao", {}).get("CEP"),
                    'eMail' : DadosCadatrais.get("Localizacao", {}).get("Email"),
                    'DDD' : DadosCadatrais.get("Localizacao", {}).get("DDD"),
                    'Telefone' : DadosCadatrais.get("Localizacao", {}).get("NumTelefone"),

                    'DataFundacao' : DadosCadatrais.get("Atividade", {}).get("DataFundacao"),
                    'Ramo' : DadosCadatrais.get("Atividade", {}).get("RamoAtividade")
                }

                print(f"Dados Cadastrais: {DadosSERASA}")

                prospecSERASASerializer = ProspecSERASASerializer(data=DadosSERASA)

                if prospecSERASASerializer.is_valid():
                    prospecSERASASerializer.save()
                else:
                    return Response('Erro ao serializar prospecSERASA', status=status.HTTP_400_BAD_REQUEST)
                ############################################################
                #Gravacao dos dados do SERASA
                ############################################################

            return Response('processaSERASA realizado com sucesso!', status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

