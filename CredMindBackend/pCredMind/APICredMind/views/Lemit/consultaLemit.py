import requests

from datetime import datetime
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from APICredMind.views.funcoesGerais import GeraIDs
from rest_framework.permissions import IsAuthenticated

class consultaEmpresaLemit(APIView):

    permission_classes = [IsAuthenticated]
    
    def get(self, request, *args, **kwargs):
        cnpj = request.data.get('cnpj')
        
        if not cnpj:
            return Response({'error': 'CNPJ não fornecido'}, status=status.HTTP_400_BAD_REQUEST)

        idConsulta = GeraIDs()

        # Consumir a API externa
        url = f'https://api.lemit.com.br/api/v1/consulta/empresa/{cnpj}'
        headers = {'Authorization': 'Bearer sfe2iZOYZtgqknvHGlQnqyOGRQCHQYg09dzAjFV6'}

        ResponseLemit = requests.get(url, headers=headers)

        DadosLemit = {}
        DadosLemit = ResponseLemit.json()

        DadosLemitRetorno = {'idConsulta': idConsulta,
                             'DadosLemit': DadosLemit
                             }

        if ResponseLemit.status_code == 200:
            # Deserializar o response
            return Response(DadosLemitRetorno, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Erro ao consumir API externa'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
