#DadosIndicadorRecuperacaoDividas_58.py
from datetime import datetime
from APICredMind.views.SERASA.mappingsSERASA import *

################################################################################################
#Bloco 580101 - Indicador (PEFIN/REFIN/Dívidas Vencidas) 
################################################################################################
def processaBloco580101(linha):
    IndPagtoEntre1e7Dias = str(linha[7:8]).strip() #A partir da data da consulta
    IndPagtoEntre7e30Dias = str(linha[8:9]).strip() #A partir da data da consulta
    IndPagtoEntre31e180Dias = str(linha[9:10]).strip() #A partir da data da consulta
    MsgClienteSemAnotOuRest = str(linha[10:130]).strip()

    return {
        'IndPagtoEntre1e7Dias' : IndPagtoEntre1e7Dias,
        'IndPagtoEntre7e30Dias' : IndPagtoEntre7e30Dias,
        'IndPagtoEntre31e180Dias' : IndPagtoEntre31e180Dias,
        'MsgClienteSemAnotOuRest' : MsgClienteSemAnotOuRest
    }

################################################################################################
#Bloco 580199 - Mensagens
################################################################################################
def processaBloco580199(linha):
    CodMsgBlocoRecupDividas = str(linha[7:8]).strip()
    MsgBlocoRecupDividas = str(linha[8:9]).strip()

    return {
        'CodMsgBlocoRecupDividas' : CodMsgBlocoRecupDividas,
        'MsgBlocoRecupDividas' : MsgBlocoRecupDividas
    }
