#DadosGastoEstimado_09.py
from datetime import datetime
from APICredMind.views.SERASA.mappingsSERASA import *

################################################################################################
#Bloco 100101 - Gasto Estimado – Valor
################################################################################################
def processaBloco100101(linha):
    DataConsulta = str(linha[7:15]).strip()
    HoraConsulta = str(linha[15:23]).strip()
    ValorGastoEstimadoAnual = str(linha[23:38]).strip()

    return {
        'DataConsulta' : DataConsulta,
        'HoraConsulta' : HoraConsulta,
        'ValorGastoEstimadoAnual' : ValorGastoEstimadoAnual
    }

################################################################################################
#Bloco 100102 - Gasto Estimado - Mensagem Default
################################################################################################
def processaBloco100102(linha):
    DataConsulta = str(linha[7:15]).strip()
    HoraConsulta = str(linha[15:23]).strip()
    Mensagem = str(linha[23:123]).strip()

    return {
        'DataConsulta' : DataConsulta,
        'HoraConsulta' : HoraConsulta,
        'Mensagem' : Mensagem
    }

################################################################################################
#Bloco 100199 - Gasto Estimado - Mensagem de não cálculo
#Obs.: As mensagens retornadas (GEPJ-MSG-FRASE) estão no item 5. Código das mensagens de retorno
################################################################################################
def processaBloco100199(linha):
    DataConsulta = str(linha[7:15]).strip()
    HoraConsulta = str(linha[15:23]).strip()
    Mensagem = str(linha[23:123]).strip()

    return {
        'DataConsulta' : DataConsulta,
        'HoraConsulta' : HoraConsulta,
        'Mensagem' : Mensagem
    }
