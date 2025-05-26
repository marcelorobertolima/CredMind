#DadosMosaicPJ_11.py
from datetime import datetime
from APICredMind.views.SERASA.mappingsSERASA import *

################################################################################################
#Bloco 120101 - Mosaic PJ – Dados
################################################################################################
def processaBloco120101(linha):
    CNPJCliente = str(linha[7:15]).strip()
    CodMosaic = str(linha[15:18]).strip()
    DataAtualizacao = str(linha[18:26]).strip()
    
    return {
        'CNPJCliente': CNPJCliente,
        'CodMosaic': CodMosaic,
        'DataAtualizacao': DataAtualizacao
    }

################################################################################################
#Bloco 120199 - Mosaic PJ – Mensagem
################################################################################################
def processaBloco120199(linha):
    DataAtualizacao = str(linha[7:15]).strip()
    HoraAtualizacao = str(linha[15:23]).strip()
    MensagemRetorno = str(linha[23:123]).strip()
    
    return {
        'DataAtualizacao': DataAtualizacao,
        'HoraAtualizacao': HoraAtualizacao,
        'MensagemRetorno': MensagemRetorno
    }
