#DadosPontualidadePagamentos_13.py
from datetime import datetime
from APICredMind.views.SERASA.mappingsSERASA import *

################################################################################################
#Bloco 130101 - Pontualidade de pagamentos PJ  – Dados
################################################################################################
def processaBloco130101(linha):
    Data = str(linha[7:15]).strip()
    Hora = str(linha[15:23]).strip()
    PontualidadePagamentos = str(linha[23:27]).strip() #0 a 100
    MensagemCodigo = str(linha[27:30]).strip()
    MensagemTexto = str(linha[30:110]).strip()
    
    return {
        'Data': Data,
        'Hora': Hora,
        'PontualidadePagamentos': PontualidadePagamentos,
        'MensagemCodigo': MensagemCodigo,
        'MensagemTexto': MensagemTexto
    }

################################################################################################
#Bloco 130199 - Pontualidade de pagamentos PJ  – Mensagem
################################################################################################
def processaBloco130199(linha):
    Data = str(linha[7:15]).strip()
    Hora = str(linha[15:23]).strip()
    
    CodMensagem = str(linha[23:27]).strip() #0 a 100
    DescMensagem = buscaTipoMensagemPontualidade(str(linha[23:27]).strip()) #0 a 100
    
    MensagemCodigo = str(linha[27:30]).strip()
    MensagemTexto = str(linha[30:110]).strip()
    
    return {
        'Data': Data,
        'Hora': Hora,
        'CodMensagem': CodMensagem,
        'DescMensagem': DescMensagem,
        'MensagemCodigo': MensagemCodigo,
        'MensagemTexto': MensagemTexto
    }
