import requests
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


NEOCREDIT_URL = 'https://app-api.neocredit.com.br/empresa-esteira-solicitacao/152/integracao'
NEOCREDIT_TOKEN = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzbHVnIjoiZmI2YTcyNjktZDFmNS00ODVmLTk2ZjgtZmRlNDMyYWVjZjA0IiwiZW1wcmVzYUlkIjoxMDcsIm5vbWUiOiJPcGVyYSJ9.RGRigsqtfj7H6XZtcJNeAZniUUarySIGejKXqMajxZg'  # Coloque seu token aqui ou use .env

class esteiraInativosNeoCredit(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        try:
            auth_header = request.headers.get('Authorization')

            if not auth_header:
                return Response({"error": "Authorization header is missing."}, status=status.HTTP_401_UNAUTHORIZED)

            cnpjs = request.data.get('cnpjs', [])
            resultados = []
            i = 1

            #Faz loop por CNPJ
            for cnpj in cnpjs:
                payload = {"documento": cnpj}
                headers =   {
                                "accept": "application/json",
                                "Content-Type": "application/json",
                                "Authorization": f"Bearer {NEOCREDIT_TOKEN}"
                            }

                try:
                    response = requests.post(NEOCREDIT_URL, json=payload, headers=headers)
                    response_data = response.json()

                    resultados.append({
                        "cnpj": cnpj,
                        "status_code": response.status_code,
                        "resposta": response_data
                    })
                except Exception as e:
                    resultados.append({
                        "cnpj": cnpj,
                        "erro": str(e)
                    })

                print(f"id: ", i, " - CNPJ: ", cnpj)

                i += 1

            return Response(resultados, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
