#DadosAnotacoesConsultasSPC_91.py
from datetime import datetime
from APICredMind.views.SERASA.mappingsSERASA import *

################################################################################################
#Bloco 911101 - Anotações e consultas SPC – Anotações 1ª parte
################################################################################################
def processaBloco911101(linha):
    DataInclusao = str(linha[7:15]).strip()
    DataVencimento = str(linha[15:23]).strip()
    TipoOperacao = str(linha[23:24]).strip()
    NumContrato = str(linha[24:54]).strip()
    ValorDebito = str(linha[54:69]).strip()
    NomeAssociado = str(linha[69:129]).strip()
    
    return {
        'DataInclusao': DataInclusao,
        'DataVencimento': DataVencimento,
        'TipoOperacao': TipoOperacao,
        'NumContrato': NumContrato,
        'ValorDebito': ValorDebito,
        'NomeAssociado': NomeAssociado
    }

################################################################################################
#Bloco 911102 - Anotações e consultas SPC - Anotações 2ª parte
################################################################################################
def processaBloco911102(linha):
    Cidade = str(linha[7:37]).strip()
    UF = str(linha[37:39]).strip()
    NomeContrato = str(linha[39:99]).strip()
    Origem = str(linha[99:129]).strip()
    
    return {
        'Cidade': Cidade,
        'UF': UF,
        'NomeContrato': NomeContrato,
        'Origem': Origem
    }

################################################################################################
#Bloco 911103 - Anotações e consultas SPC – Totais e quantidades
################################################################################################
def processaBloco911103(linha):
    QtdeOcorrencias = str(linha[7:22]).strip()
    ValorTotalDebito = str(linha[22:37]).strip()
    
    return {
        'QtdeOcorrencias': QtdeOcorrencias,
        'ValorTotalDebito': ValorTotalDebito
    }

################################################################################################
#Bloco 911199 - Anotações e consultas SPC – Mensagens anotações
################################################################################################
def processaBloco911199(linha):
    Mensagem = str(linha[7:87]).strip()
    
    return {
        'Mensagem': Mensagem
    }

################################################################################################
#Bloco 918001 - Anotações e consultas SPC – Consultas ao SPC 
################################################################################################
def processaBloco918001(linha):
    DataConsulta = str(linha[7:15]).strip()
    HoraConsulta = str(linha[15:19]).strip()
    NomeAssociado = str(linha[19:79]).strip()
    Cidade = str(linha[79:109]).strip()
    UF = str(linha[109:111]).strip()
    Origem = str(linha[111:141]).strip()
    QtdeConsultas = str(linha[141:145]).strip()
    CNPJConsultante = str(linha[145:159]).strip()
    
    return {
        'DataConsulta': DataConsulta,
        'HoraConsulta': HoraConsulta,
        'NomeAssociado': NomeAssociado,
        'Cidade': Cidade,
        'UF': UF,
        'Origem': Origem,
        'QtdeConsultas': QtdeConsultas,
        'CNPJConsultante': CNPJConsultante
    }

################################################################################################
#Bloco 918002 - Anotações e consultas SPC – Totais de consultas por mês
################################################################################################
def processaBloco918002(linha):
    AnoConsulta = str(linha[7:9]).strip()
    MesConsulta = str(linha[9:11]).strip()
    DescMesConsulta = str(linha[11:14]).strip()
    QtdeConsultas = str(linha[14:17]).strip()
    
    return {
        'AnoConsulta': AnoConsulta,
        'MesConsulta': MesConsulta,
        'DescMesConsulta': DescMesConsulta,
        'QtdeConsultas': QtdeConsultas
    }

################################################################################################
#Bloco 918099 - Anotações e consultas SPC – Mensagens Consulta ao SPC
################################################################################################
def processaBloco918099(linha):
    Mensagem = str(linha[7:87]).strip()
    
    return {
        'Mensagem': Mensagem
    }
