import requests

from datetime import datetime
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from APICredMind.views.funcoesGerais import *

from rest_framework.permissions import IsAuthenticated

class PoliticaAnalise(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request, *args, **kwargs):
        cnpj = request.data.get('documentoCedente')
        
        #url_nfe = r'E:\XML\NFeTeste.xml'
        url_nfe = request.data["titulos"][0].get("nfe")
        
        if not cnpj:
            return Response({'error': 'CNPJ do Cedente não fornecido'}, status=status.HTTP_400_BAD_REQUEST)

        # Cabeçalhos da requisição
        headers = {
            "Authorization": "Basic cGFyY2Vpcm9yOm5lb2NyZWRAMjAyMw==",
            "Cookie": "PHPSESSID=engjrvmqlohh336blabonl1r57"
        }

        response = requests.get(url_nfe, headers=headers)

        xml_content = response.content
        xml_string = xml_content.decode('utf-8')

        json_nfe = convertXMLFromURL(xml_string)

        return Response(json_nfe, status=status.HTTP_200_OK)

        # URL da sua API interna
        url_interna = 'http://localhost:8000/api/consultaEmpresaLemit'

        # Parâmetros da requisição POST
        PayLoad = {'cnpj': cnpj}

        # Faz a requisição POST à sua API interna como se fosse uma API externa
        DadosEmpresa = requests.get(url_interna, data=PayLoad)

        # Filtra os campos desejados da empresa
        cnpj = DadosEmpresa.get('cnpj')
        situacao = DadosEmpresa.get('situacao')
        cnae = DadosEmpresa.get('cnae', {})
        socios = DadosEmpresa.get('socios', [])
        emails = DadosEmpresa.get('emails', [])

        # Cria um novo objeto JSON com os campos filtrados
        DadosEmpresaResponse = {
            'cnpj' : cnpj,
            'situacao': situacao,
            'cnae': cnae,
            'socios': socios,
            'emails': emails
        }

        # Verifica se a requisição foi bem-sucedida
        if DadosEmpresa.status_code == 200:
            # Retorna os dados da empresa obtidos da sua API interna
           return Response(DadosEmpresaResponse, status=status.HTTP_200_OK)
        else:
            # Retorna um erro se a requisição não foi bem-sucedida
            return Response({'error': 'Erro ao chamar a API interna'}, status=500)

        # Consumir a API externa
        return Response(resultado_consulta, status=status.HTTP_200_OK)
