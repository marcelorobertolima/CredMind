import requests

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework.permissions import IsAuthenticated

import json

################################################################################################
#Dados Empresa
################################################################################################
class consultaDadosEmpresa(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request, *args, **kwargs):
        try:
            cnpj = request.data.get('cnpj')
            linhaBDCReq = request.data.get('linhaBDC')
            dataSet = request.data.get('dataSet')
            
            if (not cnpj or not cnpj.strip()) and (not linhaBDCReq or not linhaBDCReq.strip()):
                return Response({'error': 'CNPJ ou linhaBDC não fornecido'}, status=status.HTTP_400_BAD_REQUEST)

            if cnpj:
                # Consumir a API externa
                url = "https://plataforma.bigdatacorp.com.br/empresas"

                if not dataSet:
                    payload = {
                        "q": f"doc{{{cnpj}}}",
                        "Datasets": "basic_data, addresses_extended, kyc, processes, relationships"
                    }
                else:
                    payload = {
                        "q": f"doc{{{cnpj}}}",
                        "Datasets": f"{dataSet}"
                    }

                headers = {
                    "accept": "application/json",
                    "content-type": "application/json",
                    "AccessToken": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoiTUFSQ0VMTy5MSU1BIiwianRpIjoiNzkwMzNmNjktMjkwYi00Zjg1LTkwMTUtY2M3YTI4MWZkNzcyIiwibmFtZVVzZXIiOiJNYXJjZWxvIFJvYmVydG8gZGUgTGltYSIsInVuaXF1ZV9uYW1lIjoiTUFSQ0VMTy5MSU1BIiwiZG9tYWluIjoiT1BFUkEgQ0FQSVRBTCIsInByb2R1Y3RzIjpbIkJJR0JPT1NUIiwiQklHSUQiXSwibmJmIjoxNzQyOTA5ODcxLCJleHAiOjE3NzQ0NDU4NzEsImlhdCI6MTc0MjkwOTg3MSwiaXNzIjoiQmlnIERhdGEgQ29ycC4ifQ.edFn0ZzlGnROcL2jHGQSNjXbFy4o6pe2YX2k6uA9Tp8",
                    "TokenId": "67e2b1af633458880382addd"
                }

                ResponseBDC = requests.post(url, json=payload, headers=headers)

                if ResponseBDC.status_code == 200:
                    DadosBDC = ResponseBDC.json()
                else:
                    print('Erro ao consumir API da Big Data Corp')
                    return Response({'error': 'Erro ao consumir API da Big Data Corp'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            else:
                linhaBDC = json.loads(linhaBDCReq)
                DadosBDC = linhaBDC

            DadosEmpresa = { 
                            'DadosEmpresa': DadosBDC
                           }

            return Response(DadosEmpresa, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

################################################################################################
#Dados Pessoa
################################################################################################
class consultaDadosPessoa(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request, *args, **kwargs):
        try:
            cpf = request.data.get('cpf')
            linhaBDCReq = request.data.get('linhaBDC')
            dataSet = request.data.get('dataSet')
            
            if (not cpf or not cpf.strip()) and (not linhaBDCReq or not linhaBDCReq.strip()):
                return Response({'error': 'CPF ou linhaBDC não fornecido'}, status=status.HTTP_400_BAD_REQUEST)

            if cpf:
                # Consumir a API externa
                url = "https://plataforma.bigdatacorp.com.br/pessoas"

                if not dataSet:
                    payload = {
                        "q": f"doc{{{cpf}}}",
                        "Datasets": "basic_data, addresses_extended, kyc, processes, related_people"
                    }
                else:
                    payload = {
                        "q": f"doc{{{cpf}}}",
                        "Datasets": f"{dataSet}"
                    }

                headers = {
                    "accept": "application/json",
                    "content-type": "application/json",
                    "AccessToken": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoiTUFSQ0VMTy5MSU1BQE1STFNJU1RFTUFTLkNPTS5CUiIsImp0aSI6Ijk1YzJmOWFhLTU5MjgtNDJlNC1iZWNiLTQ4ZTBiZjk2MjQyYyIsIm5hbWVVc2VyIjoiTUFSQ0VMTyBST0JFUlRPIERFIExJTUEiLCJ1bmlxdWVfbmFtZSI6Ik1BUkNFTE8uTElNQUBNUkxTSVNURU1BUy5DT00uQlIiLCJkb21haW4iOiJNUkwgU0lTVEVNQVMiLCJwcm9kdWN0cyI6WyJCSUdCT09TVCIsIkJJR0lEIl0sIm5iZiI6MTcxNzg0ODMzMiwiZXhwIjoxNzQ5Mzg0MzMyLCJpYXQiOjE3MTc4NDgzMzIsImlzcyI6IkJpZyBEYXRhIENvcnAuIn0.z5hzY6OKbn6LzheFjiTRMMl7loFWnIY5YvjNWZbgMUc",
                    "TokenId": "6664490c21191200765bcf62"
                }

                ResponseBDC = requests.post(url, json=payload, headers=headers)

                if ResponseBDC.status_code == 200:
                    DadosBDC = ResponseBDC.json()
                else:
                    return Response({'error': 'Erro ao consumir API da Big Data Corp'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            else:
                linhaBDC = json.loads(linhaBDCReq)
                DadosBDC = linhaBDC

            DadosPessoa =   {
                                'DadosPessoa': DadosBDC
                            }
            
            return Response(DadosPessoa, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
