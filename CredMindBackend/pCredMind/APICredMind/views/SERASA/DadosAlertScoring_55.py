#DadosAlertScoring_55.py
from datetime import datetime
from APICredMind.views.SERASA.mappingsSERASA import *

################################################################################################
#Bloco 550101 - Alertscoring – Cálculo 
################################################################################################
def processaBloco550101(linha):
    PontuacaoAS = str(linha[7:11]).strip()
    Data = str(linha[11:21]).strip()
    Hora = str(linha[21:29]).strip()
    ClasseAS = str(linha[29:30]).strip()
    MsgInterpretacao = str(linha[30:110]).strip()
    AreaReservada = str(linha[110:251]).strip()
    
    return {
        'PontuacaoAS': PontuacaoAS,
        'Data': Data,
        'Hora': Hora,
        'ClasseAS': ClasseAS,
        'MsgInterpretacao': MsgInterpretacao,
        'AreaReservada': AreaReservada
    }

################################################################################################
#Bloco 550199 - Alertscoring- Mensagens
################################################################################################
def processaBloco550199(linha):
    CodMensagem = str(linha[7:10]).strip()
    Mensagem = str(linha[10:90]).strip()
    Data = str(linha[90:100]).strip()
    Hora = str(linha[100:108]).strip()
    AreaReservada = str(linha[108:251]).strip()
    
    return {
        'CodMensagem': CodMensagem,
        'Mensagem': Mensagem,
        'Data': Data,
        'Hora': Hora,
        'AreaReservada': AreaReservada
    }
