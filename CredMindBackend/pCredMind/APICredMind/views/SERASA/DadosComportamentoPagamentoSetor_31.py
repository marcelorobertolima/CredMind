#DadosComportamentoPagamentoSetor_31.py
from datetime import datetime
from APICredMind.views.SERASA.mappingsSERASA import *

################################################################################################
#Bloco 310101 - Pagamentos - Atraso em dias – % e Valor médio
################################################################################################
def processaBloco310101(linha):
    DataReferencia = str(linha[7:15]).strip()
    PercAVista = str(linha[15:20]).strip()
    ValorMedioAVista = str(linha[20:37]).strip()
    PercDe8a15dias = str(linha[37:42]).strip()
    ValorMedioDe8a15dias = str(linha[42:59]).strip()
    PercDe16a30dias = str(linha[59:64]).strip()
    ValorMedioDe16a30dias = str(linha[64:81]).strip()
    PercDe31a60dias = str(linha[81:86]).strip()
    ValorMedioDe31a60dias = str(linha[86:103]).strip()
    PercAcima60dias = str(linha[103:108]).strip()
    ValorMedioAcima60dias = str(linha[108:125]).strip()
    PercTotal = str(linha[125:130]).strip()
    ValorMedioTotal = str(linha[130:147]).strip()
    PrazoMediodeAtrasoDias = str(linha[147:152]).strip()
    
    return {
        'DataReferencia': DataReferencia,
        'PercAVista': PercAVista,
        'ValorMedioAVista': ValorMedioAVista,
        'PercDe8a15dias': PercDe8a15dias,
        'ValorMedioDe8a15dias': ValorMedioDe8a15dias,
        'PercDe16a30dias': PercDe16a30dias,
        'ValorMedioDe16a30dias': ValorMedioDe16a30dias,
        'PercDe31a60dias': PercDe31a60dias,
        'ValorMedioDe31a60dias': ValorMedioDe31a60dias,
        'PercAcima60dias': PercAcima60dias,
        'ValorMedioAcima60dias': ValorMedioAcima60dias,
        'PercTotal': PercTotal,
        'ValorMedioTotal': ValorMedioTotal,
        'PrazoMediodeAtrasoDias': PrazoMediodeAtrasoDias
    }

################################################################################################
#Bloco 310102 - Vencimentos Futuros - A vencer em dias – % e Valor médio
################################################################################################
def processaBloco310102(linha):
    DataReferencia = str(linha[7:15]).strip()
    PercAte10dias = str(linha[15:20]).strip()
    ValorMedioAte10dias = str(linha[20:37]).strip()
    PercDe11a30dias = str(linha[37:42]).strip()
    ValorMedioDe11a30dias = str(linha[42:59]).strip()
    PercDe31a45dias = str(linha[59:64]).strip()
    ValorMedioDe31a45dias = str(linha[64:81]).strip()
    PercDe45a60dias = str(linha[81:86]).strip()
    ValorMedioDe45a60dias = str(linha[86:103]).strip()
    PercAcima60dias = str(linha[103:108]).strip()
    ValorMedioAcima60dias = str(linha[108:125]).strip()
    PercTotal = str(linha[125:130]).strip()
    ValorMedioTotal = str(linha[130:147]).strip()
    
    return {
        'DataReferencia': DataReferencia,
        'PercAte10dias': PercAte10dias,
        'ValorMedioAte10dias': ValorMedioAte10dias,
        'PercDe11a30dias': PercDe11a30dias,
        'ValorMedioDe11a30dias': ValorMedioDe11a30dias,
        'PercDe31a45dias': PercDe31a45dias,
        'ValorMedioDe31a45dias': ValorMedioDe31a45dias,
        'PercDe45a60dias': PercDe45a60dias,
        'ValorMedioDe45a60dias': ValorMedioDe45a60dias,
        'PercAcima60dias': PercAcima60dias,
        'ValorMedioAcima60dias': ValorMedioAcima60dias,
        'PercTotal': PercTotal,
        'ValorMedioTotal': ValorMedioTotal
    }

################################################################################################
#Bloco 310199 - Mensagem de não cálculo 
################################################################################################
def processaBloco310199(linha):
    DataReferencia = str(linha[7:15]).strip()
    CodMensagem = str(linha[15:20]).strip()
    TextoMensagem = str(linha[20:100]).strip()
    
    return {
        'DataReferencia': DataReferencia,
        'CodMensagem': CodMensagem,
        'TextoMensagem': TextoMensagem
    }
