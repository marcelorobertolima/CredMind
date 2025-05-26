import requests
import json
from rest_framework import status

from APICredMind.views.funcoesGerais import GeraIDs
from APICredMind.views.dadosTestes import dadosTeste_BigDataCorp_DadosBasicos_Empresa

from datetime import datetime
from APICredMind.serializers import ConsultasSerializer

from APICredMind.configAPICredMind import *

def Consulta_DadosBasicosEmpresa(cnpj,
                                auth,
                                tipoConsulta = None,
                                idAnalise=None):
    try:
        cnpjRegra = cnpj

        if AMBIENTE == 'PRD':
            # URL da sua API interna
            url_interna = URL_APIs + 'consultaDadosEmpresa'
            auth_header = auth

            if not auth_header:
                return Response({"error": "Authorization header is missing."}, status=status.HTTP_401_UNAUTHORIZED)
            
            headers = {
                'Content-Type': 'application/json',
                'Authorization': auth_header,
            }
            
            dataset = "basic_data, addresses_extended" if tipoConsulta == None else tipoConsulta

            data = {
                "cnpj": cnpjRegra,
                "linhaBDC": "",
                "dataSet": dataset
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

            DadosBureau = dadosTeste_BigDataCorp_DadosBasicos_Empresa()

        idConsulta = GeraIDs()

        ############################################################
        #Gravacao na base
        ############################################################
        DadosConsulta = {
            'id_consulta': idConsulta,
            'id_analise': idAnalise,
            'DataConsulta': datetime.now(),
            'Bureau': 'BigDataCorp-Empresa-DadosBasicos',
            'Request': data,
            'Response': DadosBureau
        }

        consultasSerializer = ConsultasSerializer(data=DadosConsulta)

        if consultasSerializer.is_valid():
            consultasSerializer.save()
        ############################################################
        #Gravacao na base
        ############################################################

        return DadosBureau
    except requests.exceptions.RequestException as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
