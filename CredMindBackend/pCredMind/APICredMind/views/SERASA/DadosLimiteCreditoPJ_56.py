#DadosLimiteCreditoPJ_56.py
from datetime import datetime
from APICredMind.views.SERASA.mappingsSERASA import *

################################################################################################
#Bloco 560102 - Limite de crédito PJ – Cálculo 
################################################################################################
def processaBloco560102(linha):
    DataCalculo = str(linha[7:15]).strip()
    HoraCalculo = str(linha[15:21]).strip()
    ValorLimite = str(linha[21:34]).strip()
    OBSValorLimiteSugerido = str(linha[34:64]).strip()
    
    return {
        'DataCalculo': DataCalculo,
        'HoraCalculo': HoraCalculo,
        'ValorLimite': ValorLimite,
        'OBSValorLimiteSugerido': OBSValorLimiteSugerido
    }

################################################################################################
#Bloco 560104 - Limite de crédito PJ – Mensagens
################################################################################################
def processaBloco560104(linha):
    OBSLimiteCredito = str(linha[7:79]).strip()
    
    return {
        'OBSLimiteCredito': OBSLimiteCredito
    }
