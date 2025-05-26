import requests

from rest_framework.response import Response
from rest_framework import status
from APICredMind.views.funcoesGerais import GeraIDs
from APICredMind.views.PoliticasRegras.Regra_ValidaDadosBasicos import Regra_ValidaDadosBasicos
from APICredMind.views.PoliticasRegras.Regra_ValidaCNAEs import Regra_ValidaCNAEs
from APICredMind.views.PoliticasRegras.Regra_ValidaSocios import *

def Fluxo_Principal(cnpj, 
                    auth,
                    idAnalise,
                    rTempoEmpresa,
                    rTipoExec):
    try:
        cnpjFluxo = cnpj
        auth_header = auth

        if not cnpjFluxo:
            return Response({'error': 'CNPJ não fornecido'}, status=status.HTTP_400_BAD_REQUEST)

        if not auth_header:
            return Response({"error": "Authorization header is missing."}, status=status.HTTP_401_UNAUTHORIZED)

        #http://maps.google.com/maps?q=24.197611,120.780512

        retFluxoPrincipal = []
        retDadosFluxosPrincipal = {}

        #######################################################################################
        #'PARAR' = Na primeira regra de REPROVAR já retorna sem validar o restante
        #'SEGUIR' = Mesmo que uma regra REPROVE o fluxo segue
        #######################################################################################

        #####
        #Regras de Dados Basicos
        #####
        RetRegraValidaDadosBasicos, Reprovado, retDadosBasicos = Regra_ValidaDadosBasicos(cnpj, auth_header, rTempoEmpresa, rTipoExec, idAnalise)
       
        retFluxoPrincipal.extend(RetRegraValidaDadosBasicos)
        retDadosFluxosPrincipal = retDadosBasicos

        if rTipoExec == 'PARAR' and Reprovado:
            return retFluxoPrincipal, retDadosFluxosPrincipal

        #####
        #Regras de CNAE
        #####
        RetRegraValidaDadosCNAEs, Reprovado = Regra_ValidaCNAEs(retDadosBasicos)

        retFluxoPrincipal.append(RetRegraValidaDadosCNAEs)

        if rTipoExec == 'PARAR' and Reprovado:
            return retFluxoPrincipal, retDadosFluxosPrincipal

        #####
        #Regras de Socios PEP
        #####
        RetRegraValidaDadosPEP, Reprovado, retDadosPEP = Regra_ValidaDadosPEP(cnpj, auth_header, rTipoExec, idAnalise)
        
        retFluxoPrincipal.append(RetRegraValidaDadosPEP)
        retDadosFluxosPrincipal = {'Dados Basicos': retDadosBasicos,
                                    'DadosPEP':  retDadosPEP
                                  }

        #if rTipoExec == 'PARAR' and Reprovado:
        #    return retFluxoPrincipal, retDadosFluxosPrincipal

        #Regras de Socios Processos Criminais
        #Regras de Socios com Obito
        #Aqu é preciso pegar todo o QSA da empresa e fazer um looping validando.

        RetRegraSocios, Reprovado, retDadosSocios = Regra_ValidaDadosSocios(cnpj, auth_header, rTipoExec, idAnalise)
        
        retFluxoPrincipal.append(RetRegraSocios)
        retDadosFluxosPrincipal = {'Dados Basicos': retDadosBasicos,
                                    'DadosPEP':  retDadosPEP,
                                    'DadosSocios': retDadosSocios
                                  }

        if rTipoExec == 'PARAR' and Reprovado:
            return retFluxoPrincipal, retDadosFluxosPrincipal

        return retFluxoPrincipal, retDadosFluxosPrincipal
    except requests.exceptions.RequestException as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
