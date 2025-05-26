import requests

from datetime import datetime
from dateutil.relativedelta import relativedelta

from rest_framework.response import Response
from rest_framework import status

from APICredMind.views.PoliticaConsultas.Consulta_DadosBasicos import Consulta_DadosBasicosEmpresa

def Regra_ValidaDadosBasicos(cnpj, 
                            auth,
                            rTempoEmpresa,
                            rTipoExec,
                            idAnalise=None):
    try:
        cnpjRegra = cnpj
        
        # URL da sua API interna
        auth_header = auth

        if not auth_header:
            return Response({"error": "Authorization header is missing."}, status=status.HTTP_401_UNAUTHORIZED)
        
        messages = []
        Reprovado = False

        DadosRetorno = Consulta_DadosBasicosEmpresa(cnpjRegra, auth, None, idAnalise)

        ###############################################################
        result_list = DadosRetorno.get("DadosEmpresa", {}).get("Result", [])

        if result_list:
            basic_data = result_list[0].get("BasicData", {})
            SituacaoEmpresa = basic_data.get("TaxIdStatus")
            DataFundacao = basic_data.get("FoundedDate")
        else:
            SituacaoEmpresa = None
            DataFundacao = None

        ###############################################################
        #Regra SituacaoReceita
        ###############################################################
        if SituacaoEmpresa == 'ATIVA':
            messages.append({
                "text": "🟢 CNPJ está ATIVO na Receita Federal;",
                "type": "INFORMAR",
                "type_label": "🔵 INFORMAR"
            })
        else:
            messages.append({
                "text": "🔴 CNPJ está INATIVO na Receita Federal;",
                "type": "REPROVAR",
                "type_label": "🔴 REPROVAR"
            })
            Reprovado = True

        if rTipoExec == 'PARAR' and Reprovado:
            return messages, Reprovado, DadosRetorno
        ###############################################################
        #Regra SituacaoReceita
        ###############################################################

        #-----------------------------------------------------------------

        ###############################################################
        ##Regra tempo de empresa
        ###############################################################
        data_atual = datetime.now()
        data_fundacao = datetime.strptime(DataFundacao, "%Y-%m-%dT%H:%M:%SZ")
        DifDatas = relativedelta(data_atual, data_fundacao)

        TempoEmpresa = DifDatas.years * 12 + DifDatas.months

        if TempoEmpresa > rTempoEmpresa:
            messages.append({
                "text": "🟢 Data de abertura é SUPERIOR a 6 meses;",
                "type": "INFORMAR",
                "type_label": "🔵 INFORMAR"
            })
        else:
            messages.append({
                "text": "🔴 Data de abertura é INFERIOR a 6 meses;",
                "type": "REPROVAR",
                "type_label": "🔴 REPROVAR"
            })

        if rTipoExec == 'PARAR' and Reprovado:
            return messages, Reprovado, DadosRetorno
        ###############################################################
        ##Regra tempo de empresa
        ###############################################################

        return messages, Reprovado, DadosRetorno
    except requests.exceptions.RequestException as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
