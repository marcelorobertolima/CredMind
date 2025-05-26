import requests

from datetime import datetime

from rest_framework.response import Response
from rest_framework import status

from APICredMind.views.PoliticaConsultas.Consulta_Empresa_KYC import Consulta_Empresa_KYC
from APICredMind.views.PoliticaConsultas.Consulta_Socios import ConsultaDadosQSA

##############################################################################################
#Regra para validação de PEP
##############################################################################################
def Regra_ValidaDadosPEP(cnpj, 
                        auth,
                        rTipoExec,
                        idAnalise=None):
    try:
        cnpjRegra = cnpj
        
        # URL da sua API interna
        auth_header = auth

        if not auth_header:
            return Response({"error": "Authorization header is missing."}, status=status.HTTP_401_UNAUTHORIZED)
        
        messages = {}
        Reprovado = False

        DadosRetorno = Consulta_Empresa_KYC(cnpjRegra, auth, idAnalise)

        ###############################################################
        result_list = DadosRetorno.get("DadosEmpresa", {}).get("Result", [])

        if result_list:
            KycData = result_list[0].get("KycData", {})
            PEP = KycData.get("IsCurrentlyPEP")
        else:
            PEP = None

        ###############################################################
        #Regra PEP
        ###############################################################
        if not PEP:
            messages = {
                "text": "🟢 Nenhum sócio politicamente exposto;",
                "type": "INFORMAR",
                "type_label": "🔵 INFORMAR"
            }
        else:
            messages = {
                "text": "🔴 Possui sócio politicamente exposto",
                "type": "REPROVAR",
                "type_label": "🔴 REPROVAR"
            }
            Reprovado = True

        if rTipoExec == 'PARAR' and Reprovado:
            return messages, Reprovado, DadosRetorno
        ###############################################################
        #Regra PEP
        ###############################################################

        return messages, Reprovado, DadosRetorno
    except requests.exceptions.RequestException as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

##############################################################################################
#Regra para validação de Socios => Obito e Processo Criminal
##############################################################################################
def Regra_ValidaDadosSocios(cnpj, 
                            auth,
                            rTipoExec,
                            idAnalise=None):
    try:
        cnpjRegra = cnpj
        
        # URL da sua API interna
        auth_header = auth

        if not auth_header:
            return Response({"error": "Authorization header is missing."}, status=status.HTTP_401_UNAUTHORIZED)
        
        messages = {}
        Reprovado = False

        #Busca no Bureau externo os dados dos socios do CNPJ
        Socios = ConsultaDadosQSA(cnpjRegra, auth, idAnalise)

        #Retorna lista de CPFs dos Socios
        #Se socio PJ, sistema faz as buscas para chegar até o CPF

        #Validar CPFSocios

        ###############################################################
        #Regra Obito
        ###############################################################
        #if not PEP:
        #    messages = {
        #        "text": "🟢 Nenhum sócio politicamente exposto;",
        #        "type": "INFORMAR",
        #        "type_label": "🔵 INFORMAR"
        #    }
        #else:
        #    messages = {
        #        "text": "🔴 Possui sócio politicamente exposto",
        #        "type": "REPROVAR",
        #        "type_label": "🔴 REPROVAR"
        #    }
        #    Reprovado = True

        #if rTipoExec == 'PARAR' and Reprovado:
        #    return messages, Reprovado, DadosRetorno
        ###############################################################
        #Regra Obito
        ###############################################################

        return messages, Reprovado, Socios
    except requests.exceptions.RequestException as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
