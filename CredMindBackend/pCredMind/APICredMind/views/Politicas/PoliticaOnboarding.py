import requests
import json

from datetime import datetime
from dateutil.relativedelta import relativedelta

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from APICredMind.views.funcoesGerais import GeraIDs

from rest_framework.permissions import IsAuthenticated

from datetime import datetime
from APICredMind.serializers import AnalisesSerializer

from APICredMind.views.PoliticaFluxos.Fluxo_Principal import *

class PoliticaOnboarding(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        try:
            cnpj = request.data.get('documento')
            url_callback = request.data.get('url_callback')
            
            if not cnpj:
                return Response({'error': 'CNPJ não informado'}, status=status.HTTP_400_BAD_REQUEST)

            #http://maps.google.com/maps?q=24.197611,120.780512

            auth_header = request.headers.get('Authorization')

            if not auth_header:
                return Response({"error": "Authorization header is missing."}, status=status.HTTP_401_UNAUTHORIZED)
            
            idAnalise = GeraIDs()

            #Regras de Dados Basicos
            #'PARAR' = Na primeira regra de REPROVAR já retorna sem validar o restante
            #'SEGUIR' = Mesmo que uma regra REPROVE o fluxo segue
            retFluxo, retDados = Fluxo_Principal(cnpj, auth_header, idAnalise, 6, 'PARAR')

            RetornoPolitica = {
                "RetornoPolitica": {
                    "idAnalise": idAnalise,
                    "messages": retFluxo
                },
                "consultas": retDados
            }

            ############################################################
            #Gravacao na base
            ############################################################
            DadosAnalise = {
                'id_analise': idAnalise,
                'DataConsulta': datetime.now(),
                'Request': request.data,
                'Response': RetornoPolitica
            }

            analisesSerializer = AnalisesSerializer(data=DadosAnalise)

            if analisesSerializer.is_valid():
                analisesSerializer.save()
            ############################################################
            #Gravacao na base
            ############################################################

            return Response(RetornoPolitica, status=status.HTTP_200_OK)
        except requests.exceptions.RequestException as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
