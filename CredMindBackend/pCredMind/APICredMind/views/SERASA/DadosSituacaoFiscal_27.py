#DadosSituacaoFiscal_27.py
from datetime import datetime
from APICredMind.views.SERASA.mappingsSERASA import *

################################################################################################
#Bloco 270101 - Receita Federal – Identificação
################################################################################################
def processaBloco270101(linha):
    Data = str(linha[7:15]).strip()
    CNPJ = str(linha[15:30]).strip()
    RazaoSocial = str(linha[30:100]).strip()
    CodSituacao = str(linha[100:101]).strip()
    DescSituacao = str(linha[101:131]).strip()
    DataSituacao = str(linha[131:139]).strip()
    
    CodSimplesNacional = str(linha[139:140]).strip()
    DescSimplesNacional = buscaTipoSimplesNacional(str(linha[139:140]).strip())
    
    CodCNAEPrimario = str(linha[140:145]).strip()
    SegCNAEPrimario = str(linha[145:147]).strip()
    DescCNAEPrimario = str(linha[147:217]).strip()
    
    return {
        'Data': Data,
        'CNPJ': CNPJ,
        'RazaoSocial': RazaoSocial,
        'CodSituacao': CodSituacao,
        'DescSituacao': DescSituacao,
        'DataSituacao': DataSituacao,
        'CodSimplesNacional': CodSimplesNacional,
        'DescSimplesNacional': DescSimplesNacional,
        'CodCNAEPrimario': CodCNAEPrimario,
        'SegCNAEPrimario': SegCNAEPrimario,
        'DescCNAEPrimario': DescCNAEPrimario
    }

################################################################################################
#Bloco 270102 - Receita Federal – CNAEs Secundários
################################################################################################
def processaBloco270102(linha):
    CodCNAESecundario = str(linha[7:12]).strip()
    SegCNAESecundario = str(linha[12:14]).strip()
    DescCNAESecundario = str(linha[14:84]).strip()
    
    return {
        'CodCNAESecundario': CodCNAESecundario,
        'SegCNAESecundario': SegCNAESecundario,
        'DescCNAESecundario': DescCNAESecundario
    }

################################################################################################
#Bloco 270103 - Receita Federal – Mensagens
################################################################################################
def processaBloco270103(linha):
    MsgReceitaFederal = str(linha[7:87]).strip()
    
    return {
        'MsgReceitaFederal': MsgReceitaFederal
    }

################################################################################################
#Bloco 270104 - Sintegra/SEFAZ – Situação
################################################################################################
def processaBloco270104(linha):
    Data = str(linha[7:15]).strip()
    NumInscEstadual = str(linha[15:30]).strip()
    CodSituacao = str(linha[30:34]).strip()
    DescSituacao = str(linha[34:234]).strip()
    
    return {
        'Data': Data,
        'NumInscEstadual': NumInscEstadual,
        'CodSituacao': CodSituacao,
        'DescSituacao': DescSituacao
    }

################################################################################################
#Bloco 270105 - Sintegra/SEFAZ – Identificação
################################################################################################
def processaBloco270105(linha):
    DataUltAtualCadastral = str(linha[7:15]).strip()
    RazaoSocial = str(linha[15:115]).strip()
    DataConsulta = str(linha[115:123]).strip()
    NumConsultaSite = str(linha[123:133]).strip()
    
    return {
        'DataUltAtualCadastral': DataUltAtualCadastral,
        'RazaoSocial': RazaoSocial,
        'DataConsulta': DataConsulta,
        'NumConsultaSite': NumConsultaSite
    }

################################################################################################
#Bloco 270106 - Sintegra/SEFAZ – Atividade Econômica
################################################################################################
def processaBloco270106(linha):
    AtividadeEconomica = str(linha[7:157]).strip()
    
    return {
        'AtividadeEconomica': AtividadeEconomica
    }

################################################################################################
#Bloco 270107 - Sintegra/SEFAZ – Observações
################################################################################################
def processaBloco270107(linha):
    Observacoes = str(linha[7:257]).strip()
    
    return {
        'Observacoes': Observacoes
    }

################################################################################################
#Bloco 270108 - Sintegra/SEFAZ – Mensagens
################################################################################################
def processaBloco270108(linha):
    Mensagem = str(linha[7:87]).strip()
    
    return {
        'Mensagem': Mensagem
    }

################################################################################################
#Bloco 270109 - SUFRAMA – Identificação/Situação
################################################################################################
def processaBloco270109(linha):
    DataConsulta = str(linha[7:15]).strip()
    NumInscSUFRAMA = str(linha[15:30]).strip()
    CodNumSUFRAMA = str(linha[30:39]).strip()
    DescSituacao = str(linha[39:239]).strip()
    
    return {
        'DataConsulta': DataConsulta,
        'NumInscSUFRAMA': NumInscSUFRAMA,
        'CodNumSUFRAMA': CodNumSUFRAMA,
        'DescSituacao': DescSituacao
    }

################################################################################################
#Bloco 270110 - SUFRAMA – Mensagens
################################################################################################
def processaBloco270110(linha):
    Mensagem = str(linha[7:87]).strip()
    
    return {
        'Mensagem': Mensagem
    }

################################################################################################
#Bloco 270199 - Situação Fiscal – Mensagem Geral
#Mensagem geral informando a quantidade de blocos Sintegra/Sefaz e/ou quantidade de CNAES
################################################################################################
def processaBloco270199(linha):
    Mensagem = str(linha[7:207]).strip()
    
    return {
        'Mensagem': Mensagem
    }
