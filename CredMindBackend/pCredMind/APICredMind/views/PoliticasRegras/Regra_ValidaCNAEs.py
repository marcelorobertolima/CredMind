import requests

from rest_framework.response import Response
from rest_framework import status

from APICredMind.models import BlackListCNAE

#Não precisa passar idAnalise pq ele usa dados Basicos já consultadod
#Só realiza a regra
def Regra_ValidaCNAEs(DadosBasicos):
    try:
        messages = {}
        Reprovado = False

        ###############################################################
        result_list = DadosBasicos.get("DadosEmpresa", {}).get("Result", [])

        if result_list:
            basic_data = result_list[0].get("BasicData", {})

            CNAES = basic_data.get("Activities")
        else:
            CNAES = None

        ###############################################################
        #Regra BlackList CNAES
        ###############################################################
        if CNAES:
            blacklistCNAES = list(BlackListCNAE.objects.values_list('idCNAE', flat=True))
            CNAEBlackList = False

            #Varre todos os CNAEs verificando se há algum em BlackList
            for ListaCNAEsBuerau in CNAES:
                listaCodigos = []

                itemCNAE = ListaCNAEsBuerau["Code"]

                for i in range(1, len(itemCNAE) + 1):
                    ItemLista = itemCNAE[:i]
                    listaCodigos.append(ItemLista)

                for CodCNAE in listaCodigos:
                    if CodCNAE in blacklistCNAES:
                        CNAEBlackList = True
                        break #Sai do Loop no primerio CNAE que encontrar em BlakList

            ##################################################################
            if not CNAEBlackList:
                messages = {
                    "text": "🟢 O(s) CNAE(s) não consta(m) na BlackList;",
                    "type": "INFORMAR",
                    "type_label": "🔵 INFORMAR"
                }
            else:
                messages = {
                    "text": "🔴 O(s) CNAE(s) consta(m) na BlackList;",
                    "type": "REPROVAR",
                    "type_label": "🔴 REPROVAR"
                }
                Reprovado = True
            ###############################################################
            #Regra BlackList CNAES
            ###############################################################

        return messages, Reprovado
    except requests.exceptions.RequestException as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
