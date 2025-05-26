#DadosOrgaosPublicos_12.py
from datetime import datetime
from APICredMind.views.SERASA.mappingsSERASA import *

################################################################################################
#Bloco 120201 - Orgãos Publicos – Dados 
################################################################################################
def processaBloco120201(linha):
    DataAtualizacao = str(linha[7:15]).strip()
    HoraAtualizacao = str(linha[15:23]).strip()
    OrigemAnotacao = str(linha[23:90]).strip()
    SiglaEstado = str(linha[90:92]).strip()
    ContratoAnotacao = str(linha[92:112]).strip()
    ValorAnotacao = str(linha[112:129]).strip()
    Avalista = str(linha[129:130]).strip()
    Modalidade = str(linha[130:133]).strip()
    DataVencimento = str(linha[133:143]).strip()
    
    return {
        'DataAtualizacao': DataAtualizacao,
        'HoraAtualizacao': HoraAtualizacao,
        'OrigemAnotacao': OrigemAnotacao,
        'SiglaEstado': SiglaEstado,
        'ContratoAnotacao': ContratoAnotacao,
        'ValorAnotacao': ValorAnotacao,
        'Avalista': Avalista,
        'Modalidade': Modalidade,
        'DataVencimento': DataVencimento
    }

################################################################################################
#Bloco 120202 - Orgãos Publicos PJ – Totais
################################################################################################
def processaBloco120202(linha):
    DataAtualizacao = str(linha[7:15]).strip()
    HoraAtualizacao = str(linha[15:23]).strip()
    TotalOcorrencias = str(linha[23:28]).strip()
    TotalAnotacoes = str(linha[28:45]).strip()
    
    return {
        'DataAtualizacao': DataAtualizacao,
        'HoraAtualizacao': HoraAtualizacao,
        'TotalOcorrencias': TotalOcorrencias,
        'TotalAnotacoes': TotalAnotacoes
    }

################################################################################################
#Bloco 120299 - Orgãos Publicos PJ – Mensagem 
################################################################################################
def processaBloco120299(linha):
    DataAtualizacao = str(linha[7:15]).strip()
    HoraAtualizacao = str(linha[15:23]).strip()
    MensagemRetorno = str(linha[23:123]).strip()
    
    return {
        'DataAtualizacao': DataAtualizacao,
        'HoraAtualizacao': HoraAtualizacao,
        'MensagemRetorno': MensagemRetorno
    }
