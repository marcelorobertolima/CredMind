#DadosIndicadorRecuperacaoCredito_53.py
from datetime import datetime
from APICredMind.views.SERASA.mappingsSERASA import *

################################################################################################
#Bloco 530101 - Indicador de Recuperação de Crédito (COLLECTION SCORE)
################################################################################################
def processaBloco530101(linha):
    PontuacaoCS = str(linha[7:11]).strip()
    NumCNPJ = str(linha[11:19]).strip()
    FilialCNPJ = str(linha[19:23]).strip()
    DigCNPJ = str(linha[23:25]).strip()
    RazaoSocial = str(linha[25:104]).strip()
    ClasseCS = str(linha[104:105]).strip()
    MsgInterpretacao = str(linha[105:185]).strip()
    AreaReservada = str(linha[185:301]).strip()

    return {
        'PontuacaoCS' : PontuacaoCS,
        'NumCNPJ' : NumCNPJ,
        'FilialCNPJ' : FilialCNPJ,
        'DigCNPJ' : DigCNPJ,
        'RazaoSocial' : RazaoSocial,
        'ClasseCS' : ClasseCS,
        'MsgInterpretacao' : MsgInterpretacao,
        'AreaReservada' : AreaReservada
    }

################################################################################################
#Bloco 530199 - Indicador de Recuperação de Crédito (COLLECTION SCORE) – Mensagem
################################################################################################
def processaBloco530199(linha):
    NumCNPJ = str(linha[7:15]).strip()
    FilialCNPJ = str(linha[15:19]).strip()
    DigCNPJ = str(linha[19:21]).strip()
    CodMensagem = str(linha[21:25]).strip()
    Mensagem = str(linha[25:105]).strip()
    AreaReservada = str(linha[105:301]).strip()

    return {
        'NumCNPJ' : NumCNPJ,
        'FilialCNPJ' : FilialCNPJ,
        'DigCNPJ' : DigCNPJ,
        'CodMensagem' : CodMensagem,
        'Mensagem' : Mensagem,
        'AreaReservada' : AreaReservada
    }
