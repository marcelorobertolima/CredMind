#DadosMensagensBloco_06.py
from datetime import datetime
from APICredMind.views.SERASA.mappingsSERASA import *

################################################################################################
#Bloco 010299 - EMPRESA NAO CADASTRADA
################################################################################################
def processaBloco010299(linha):
    MensagemBloco = str(linha[7:86]).strip()

    return {
        'MensagemBloco' : MensagemBloco
    }

################################################################################################
#Bloco 010999 - MENSAGEM QS
################################################################################################
def processaBloco010999(linha):
    MensagemBloco = str(linha[7:86]).strip()

    return {
        'MensagemBloco' : MensagemBloco
    }

################################################################################################
#Bloco 011199 - MENSAGEM ADM
################################################################################################
def processaBloco011199(linha):
    MensagemBloco = str(linha[7:86]).strip()

    return {
        'MensagemBloco' : MensagemBloco
    }

################################################################################################
#Bloco 011399 - MENSAGEM PARTICIPADADA
################################################################################################
def processaBloco011399(linha):
    MensagemBloco = str(linha[7:86]).strip()

    return {
        'MensagemBloco' : MensagemBloco
    }

################################################################################################
#Bloco 011499 - MENSAGEM PARTICIPANTE
################################################################################################
def processaBloco011499(linha):
    MensagemBloco = str(linha[7:86]).strip()

    return {
        'MensagemBloco' : MensagemBloco
    }

################################################################################################
#Bloco 040199 - MENSAGEM PENDENCIA FINANCEIRA
################################################################################################
def processaBloco040199(linha):
    MensagemBloco = str(linha[7:86]).strip()

    return {
        'MensagemBloco' : MensagemBloco
    }

################################################################################################
#Bloco 040299 - MENSAGEM CONCENTRE
################################################################################################
def processaBloco040299(linha):
    MensagemBloco = str(linha[7:86]).strip()

    return {
        'MensagemBloco' : MensagemBloco
    }

################################################################################################
#Bloco 041099 - MENSAGEM RECHEQUE
################################################################################################
def processaBloco041099(linha):
    MensagemBloco = str(linha[7:86]).strip()

    return {
        'MensagemBloco' : MensagemBloco
    }
