#DadosRiscoNovasEmpresas_14.py
from datetime import datetime
from APICredMind.views.SERASA.mappingsSERASA import *

################################################################################################
#Bloco 140101 - Risco de Novas Empresas  – Dados
################################################################################################
def processaBloco140101(linha):
    Data = str(linha[7:15]).strip()
    Hora = str(linha[15:23]).strip()
    MsgClassifRisco = str(linha[23:103]).strip() #0 a 100
    MsgComplementar = str(linha[103:183]).strip()
    
    return {
        'Data': Data,
        'Hora': Hora,
        'MsgClassifRisco': MsgClassifRisco,
        'MsgComplementar': MsgComplementar
    }

################################################################################################
#Bloco 140103 - Risco de Novas Empresas  – Filtros
################################################################################################
def processaBloco140103(linha):
    Data = str(linha[7:15]).strip()
    Hora = str(linha[15:23]).strip()
    FatorScore = str(linha[23:29]).strip() #0 a 100
    FatorPrinad = str(linha[29:34]).strip()
    Mensagem = str(linha[34:111]).strip()
    
    return {
        'Data': Data,
        'Hora': Hora,
        'FatorScore': FatorScore,
        'FatorPrinad': FatorPrinad,
        'Mensagem': Mensagem
    }

################################################################################################
#Bloco 140199 - Risco de Novas Empresas  – Mensagem
################################################################################################
def processaBloco140199(linha):
    Data = str(linha[7:15]).strip()
    Hora = str(linha[15:23]).strip()
    Mensagem = str(linha[23:103]).strip() #0 a 100
    CodMensagem = str(linha[103:106]).strip()
    
    return {
        'Data': Data,
        'Hora': Hora,
        'Mensagem': Mensagem,
        'CodMensagem': CodMensagem
    }
