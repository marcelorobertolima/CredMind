#DadosInformacoesMonitoreGerencieCarteira_08.py
from datetime import datetime
from APICredMind.views.SERASA.mappingsSERASA import *

################################################################################################
#Bloco 080102 - Monitore Gerencie Carteira 
################################################################################################
def processaBloco080102(linha):
    CodRetorno = str(linha[7:9]).strip()
    DescRetorno = buscaTipoCodRetornoMonitore(str(linha[7:9]).strip())

    MsgRetornoGerencie = str(linha[9:89]).strip()
    MsgRetornoConfie = str(linha[89:169]).strip()
    
    return {
        'CodRetorno': CodRetorno,
        'DescRetorno': DescRetorno,
        'MsgRetornoGerencie': MsgRetornoGerencie,
        'MsgRetornoConfie': MsgRetornoConfie
    }
