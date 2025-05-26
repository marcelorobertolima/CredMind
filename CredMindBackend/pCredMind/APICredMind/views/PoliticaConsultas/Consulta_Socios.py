import requests
import json

from rest_framework.response import Response
from rest_framework import status
from APICredMind.views.funcoesGerais import GeraIDs
from APICredMind.views.dadosTestes import dadosTeste_BigDataCorp_Socios_Empresa

from datetime import datetime
from APICredMind.serializers import ConsultasSerializer

from APICredMind.configAPICredMind import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

################################################################################################
################################################################################################
################################################################################################
class ConsultaDadosQSA(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        try:
            cnpj = request.data.get('cnpj')
            idAnalise = request.data.get('idAnalise')

            auth_header = request.headers.get('Authorization')

            print(auth_header)

            if not auth_header:
                return Response({"error": "Authorization header is missing."}, status=status.HTTP_401_UNAUTHORIZED)

            print("CNPJ: ", cnpj)

            Socios = ConsultaDadosQSA.extrair_socios(cnpj, auth_header, idAnalise)
            
            return Response(Socios, status=status.HTTP_200_OK)
        except requests.exceptions.RequestException as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    ################################################################################################
    ################################################################################################
    ################################################################################################
    def extrair_socios(cnpj, 
                       auth,
                       idAnalise=None,
                       visitados=None):
        
        if visitados is None:
            visitados = set()

        if cnpj in visitados:
            return None

        visitados.add(cnpj)
        
        nomeEmpresaCNPJ, socios = ConsultaDadosQSA.buscar_socios(cnpj, auth, idAnalise)

        socios_cpfs = []
        socios_cnpjs = []
        
        for socio in socios:
            if socio['TipoID'] == 'CPF':
                socios_cpfs.append({"Nome": socio['Nome'], 
                                    "CPF": socio['CPFCNPJ'],
                                    "TipoSocio": socio['TipoSocio']})
            elif socio['TipoID'] == 'CNPJ':
                socios_cnpjs.append({"Nome": socio['Nome'], 
                                     "CNPJ": socio['CPFCNPJ'],
                                     "TipoSocio": socio['TipoSocio']
                                     })

        Socios = {
            "CNPJ": cnpj,
            "Nome": nomeEmpresaCNPJ,
            "Socios": []
        }

        # Adiciona os sócios CPF diretamente ao array "Socios"
        Socios["Socios"].extend(socios_cpfs)

        # Adiciona os sócios CNPJ, processando-os recursivamente
        for sub_cnpj in socios_cnpjs:
            sub_cnpj_cnpj = sub_cnpj["CNPJ"]

            print("sub_cnpj-CNPJ => ", sub_cnpj_cnpj)

            sub_socios = ConsultaDadosQSA.extrair_socios(sub_cnpj_cnpj, auth, idAnalise, visitados)
            
            if sub_socios:
                Socios["Socios"].append(sub_socios)

        return Socios

    ################################################################################################
    ################################################################################################
    ################################################################################################
    def buscar_socios(cnpj,
                    auth,
                    idAnalise=None):
        try:
            cnpjRegra = cnpj

            if AMBIENTE == 'PRD':
                # URL da sua API interna
                url_interna = URL_APIs + 'consultaDadosEmpresa'
                auth_header = auth

                headers = {
                    'Content-Type': 'application/json',
                    'Authorization': auth_header,
                }
                
                data = {
                    "cnpj": cnpjRegra,
                    "linhaBDC": "",
                    "dataSet": "basic_data, relationships"
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

                DadosBureau = dadosTeste_BigDataCorp_Socios_Empresa()

            idConsulta = GeraIDs()

            ############################################################
            #Gravacao na base
            ############################################################
            DadosConsulta = {
                'id_consulta': idConsulta,
                'id_analise': idAnalise,
                'DataConsulta': datetime.now(),
                'Bureau': 'BigDataCorp-Socios-Empresa',
                'Request': data,
                'Response': DadosBureau
            }

            consultasSerializer = ConsultasSerializer(data=DadosConsulta)

            if consultasSerializer.is_valid():
                consultasSerializer.save()
            ############################################################
            #Gravacao na base
            ############################################################

            Socios = []

            #Retorna Somente os Socios
            ResultDadosQSA = DadosBureau.get("DadosEmpresa", {}).get("Result", [])

            basicData = ResultDadosQSA[0].get("BasicData", {})
            nomeEmpresaCNPJ = basicData["OfficialName"]

            if ResultDadosQSA:
                DadosQSA = ResultDadosQSA[0].get("Relationships", {}).get("CurrentRelationships", [])

                for socio in DadosQSA:
                    if socio["RelationshipType"] == "QSA" or socio["RelationshipType"] == "REPRESENTANTELEGAL":
                        tipoID = socio["RelatedEntityTaxIdType"]
                        cpfcnpj = socio["RelatedEntityTaxIdNumber"]
                        nome = socio["RelatedEntityName"]
                        tipoSocio = socio["RelationshipType"]

                        Socios.append({
                            "TipoID": tipoID,
                            "CPFCNPJ": cpfcnpj,
                            "Nome": nome,
                            "TipoSocio": tipoSocio
                        })

            print("Socios do CNPJ: ", cnpjRegra, "JSON", Socios)

            return nomeEmpresaCNPJ, Socios
        except requests.exceptions.RequestException as e:
            return f"RequestException occurred: {e}"
