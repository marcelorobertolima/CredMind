#DadosInscricaoEstadual_57.py
from datetime import datetime
from APICredMind.views.SERASA.mappingsSERASA import *

################################################################################################
#Bloco 571001 - Inscrição Estadual – Informações - Ocorre até 5 vezes
################################################################################################
def processaBloco571001(linha):
    NumInscEstadual = str(linha[7:15]).strip()
    
    return {
        'NumInscEstadual': NumInscEstadual
    }
