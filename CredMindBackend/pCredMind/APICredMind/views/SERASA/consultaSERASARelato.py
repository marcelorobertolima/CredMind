#consultaSERASARelato.py
import requests
import json

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from APICredMind.views.funcoesGerais import GeraIDs
from APICredMind.views.SERASA.mappingsSERASA import *

from APICredMind.serializers import ConsultasSerializer

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

class consultaSERASARelato(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        try:
            cnpj = request.data.get('cnpj')
            linhaRelato = request.data.get('linhaSERASA')

            if (not cnpj or not cnpj.strip()) and (not linhaRelato or not linhaRelato.strip()):
                return Response({'error': 'CNPJ ou linhaSERASA não fornecido'}, status=status.HTTP_400_BAD_REQUEST)

            if not linhaRelato:
                CNPJ = str(cnpj)

                RaizCNPJ = CNPJ.replace('.', '').replace('/', '').replace('-', '')
                RaizCNPJ = RaizCNPJ[0:8]

                UsuarioSERASA = '99574580'
                SenhaSERASA = 'oper4hl@'

                # Consumir a API externa
                url = f'https://mqlinuxext-2.serasa.com.br/Homologa/consultahttps?p={UsuarioSERASA}{SenhaSERASA}        IP20RELAS2        0{RaizCNPJ}22N            032E                                                                                    HPJ8'

                DadosSERASA = requests.post(url)

                if DadosSERASA.status_code == 200:
                    DadosBrutos = DadosSERASA.text
                else:
                    return Response({'error': 'Erro ao consumir API do SERASA'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            else:
                DadosBrutos = linhaRelato

            idConsulta = GeraIDs()

            #Quebra a linha para o tratamento dos blocos
            DadosTratados = DadosBrutos.split('#')

            # Lista para armazenar os objetos do JSON
            RetornoSERASA = {'idConsulta': idConsulta}

            for Linha in DadosTratados:
                TipoLinha = str(Linha[0:1])

                if TipoLinha == 'L':
                    TipoRegistro = str(Linha[1:7])
                    NomeGrupo, NomeItem = buscaNomesBlocos(TipoRegistro)

                    # Verifica o tipo de RetornoBloco
                    print(f"Tipo Registro: {TipoRegistro}")
                    print(f"Nome Grupo: {NomeGrupo}")
                    print(f"Nome Item: {NomeItem}")

                    RetornoBloco = globals()[f'processaBloco{TipoRegistro}'](Linha)

                    print(f"Tipo de RetornoBloco: {type(RetornoBloco)}")
                    print(f"Conteúdo de RetornoBloco: {RetornoBloco}")

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
            #Gravacao na base
            ############################################################
            DadosConsulta = {
                'id_consulta': idConsulta,
                'id_analise': None,
                'DataConsulta': datetime.now(),
                'Bureau': 'SERASA-Relato',
                'Request': json.dumps(request.data),  # Serializa o dicionário
                'Response': json.dumps(RetornoSERASA)  # Serializa o dicionário
            }

            consultasSerializer = ConsultasSerializer(data=DadosConsulta)

            if consultasSerializer.is_valid():
                consultasSerializer.save()
            ############################################################
            #Gravacao na base
            ############################################################

            return Response(RetornoSERASA, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
