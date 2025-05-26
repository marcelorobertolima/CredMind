#DadosFaturamentoEstimado_30.py
from datetime import datetime
from APICredMind.views.SERASA.mappingsSERASA import *

################################################################################################
#Bloco 300201 - Identificação
################################################################################################
def processaBloco300201(linha):
    DataAualizacao = str(linha[7:16]).strip()
    CNPJ = str(linha[16:25]).strip()
    FilialCNPJ = str(linha[25:29]).strip()
    DigCNPJ = str(linha[29:31]).strip()
    RazaoSocial = str(linha[31:101]).strip()
    NomeUsuario = str(linha[101:121]).strip()
    DataConsulta = str(linha[121:129]).strip()
    HoraConsulta = str(linha[129:135]).strip()
    
    return {
        'DataAualizacao': DataAualizacao,
        'CNPJ': CNPJ,
        'FilialCNPJ': FilialCNPJ,
        'DigCNPJ': DigCNPJ,
        'RazaoSocial': RazaoSocial,
        'NomeUsuario': NomeUsuario,
        'DataConsulta': DataConsulta,
        'HoraConsulta': HoraConsulta
    }

################################################################################################
#Bloco 300202 - Valor
################################################################################################
def processaBloco300202(linha):
    DataAualizacao = str(linha[7:16]).strip()
    ValorFaturamentoEstimado = str(linha[16:25]).strip() #com Positivo (em milhares de Reais)
    Pontuacao = str(linha[25:29]).strip()
    FaixaDe = str(linha[29:33]).strip()
    FaixAte = str(linha[33:37]).strip()
    
    return {
        'DataAualizacao': DataAualizacao,
        'ValorFaturamentoEstimado': ValorFaturamentoEstimado,
        'Pontuacao': Pontuacao,
        'FaixaDe': FaixaDe,
        'FaixAte': FaixAte
    }

################################################################################################
#Bloco 300203 - Motivo do não cálculo
################################################################################################
def processaBloco300203(linha):
    DataAualizacao = str(linha[7:16]).strip()
    Mensagem = str(linha[16:116]).strip()
    
    return {
        'DataAualizacao': DataAualizacao,
        'Mensagem': Mensagem
    }

################################################################################################
#Bloco 300299 - Mensagens
################################################################################################
def processaBloco300299(linha):
    DataAualizacao = str(linha[7:16]).strip()
    Mensagem = str(linha[16:95]).strip()
    
    return {
        'DataAualizacao': DataAualizacao,
        'Mensagem': Mensagem
    }
