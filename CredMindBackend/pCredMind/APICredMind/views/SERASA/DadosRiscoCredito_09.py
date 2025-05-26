#DadosRiscoCredito_08.py
from datetime import datetime
from APICredMind.views.SERASA.mappingsSERASA import *

################################################################################################
#Bloco 090101 - Risco de Crédito do Setor – Cálculo
################################################################################################
def processaBloco090101(linha):
    DataConsulta = str(linha[7:15]).strip()
    HoraConsulta = str(linha[15:23]).strip()
    FatorScorePJ = str(linha[23:27]).strip()
    PercPrinad = str(linha[27:32]).strip()

    return {
        'DataConsulta' : DataConsulta,
        'HoraConsulta' : HoraConsulta,
        'FatorScorePJ' : FatorScorePJ,
        'PercPrinad' : PercPrinad
    }

################################################################################################
#Bloco 090199 - Risco de Crédito do Setor – Mensagem
################################################################################################
def processaBloco090199(linha):
    DataConsulta = str(linha[7:15]).strip()
    HoraConsulta = str(linha[15:23]).strip()
    Mensagem = str(linha[23:123]).strip()

    return {
        'DataConsulta' : DataConsulta,
        'HoraConsulta' : HoraConsulta,
        'Mensagem' : Mensagem
    }

################################################################################################
#Bloco 090201 - Risco de Crédito do Setor - “CRES” e Serasa Score Setorial - “CRE6”
################################################################################################
def processaBloco090201(linha):
    DataConsulta = str(linha[7:15]).strip()
    HoraConsulta = str(linha[15:23]).strip()
    FatorRiskScoringBrasil = str(linha[23:26]).strip()
    FatorPrinadBrasil = str(linha[26:33]).strip()
    FatorRiskScoringRegiao = str(linha[33:36]).strip()
    FatorPrinadRegiao = str(linha[36:43]).strip()
    FatorRiskScoringUF = str(linha[43:46]).strip()
    FatorPrinadUF = str(linha[46:53]).strip()
    UFMatriz = str(linha[53:55]).strip()
    Regiao = str(linha[55:57]).strip()
    Brasil = str(linha[57:67]).strip()
    ClasseBrasil = str(linha[67:69]).strip()
    ClasseRegiao = str(linha[69:71]).strip()
    ClasseUF = str(linha[71:73]).strip()

    return {
        'DataConsulta' : DataConsulta,
        'HoraConsulta' : HoraConsulta,
        'FatorRiskScoringBrasil' : FatorRiskScoringBrasil,
        'FatorPrinadBrasil' : FatorPrinadBrasil,
        'FatorRiskScoringRegiao' : FatorRiskScoringRegiao,
        'FatorPrinadRegiao' : FatorPrinadRegiao,
        'FatorRiskScoringUF' : FatorRiskScoringUF,
        'FatorPrinadUF' : FatorPrinadUF,
        'UFMatriz' : UFMatriz,
        'Regiao' : Regiao,
        'Brasil' : Brasil,
        'ClasseBrasil' : ClasseBrasil,
        'ClasseRegiao' : ClasseRegiao,
        'ClasseUF' : ClasseUF
    }

################################################################################################
#Bloco 090299 - Risco de Crédito do Setor - “CRES” e Serasa Score Setorial - “CRE6” – Mensagem Geral 
################################################################################################
def processaBloco090299(linha):
    DataConsulta = str(linha[7:15]).strip()
    HoraConsulta = str(linha[15:23]).strip()
    Mensagem = str(linha[23:123]).strip()

    return {
        'DataConsulta' : DataConsulta,
        'HoraConsulta' : HoraConsulta,
        'Mensagem' : Mensagem
    }

################################################################################################
#Bloco 090298 - Risco de Crédito do Setor - “CRES” e Serasa Score Setorial - “CRE6” – Mensagem Estado
################################################################################################
def processaBloco090298(linha):
    DataConsulta = str(linha[7:15]).strip()
    HoraConsulta = str(linha[15:23]).strip()
    Mensagem = str(linha[23:123]).strip()

    return {
        'DataConsulta' : DataConsulta,
        'HoraConsulta' : HoraConsulta,
        'Mensagem' : Mensagem
    }

################################################################################################
#Bloco 090297 - Risco de Crédito do Setor - “CRES” e Serasa Score Setorial - “CRE6” - Mensagem Estado e Região 
################################################################################################
def processaBloco090297(linha):
    DataConsulta = str(linha[7:15]).strip()
    HoraConsulta = str(linha[15:23]).strip()
    Mensagem = str(linha[23:123]).strip()

    return {
        'DataConsulta' : DataConsulta,
        'HoraConsulta' : HoraConsulta,
        'Mensagem' : Mensagem
    }

################################################################################################
#Bloco 930109 - Risco de Crédito – Empresa e Setor (COMBO SETOR) e Serasa Score Empresa e Setor – Cálculo 
################################################################################################
def processaBloco930109(linha):
    Data = str(linha[7:15]).strip()
    Hora = str(linha[15:23]).strip()
    FatorRiskScoring = str(linha[23:27]).strip()
    FatorPrinad = str(linha[27:32]).strip()
    AreaReservada = str(linha[32:37]).strip()

    return {
        'Data' : Data,
        'Hora' : Hora,
        'FatorRiskScoring' : FatorRiskScoring,
        'FatorPrinad' : FatorPrinad,
        'AreaReservada' : AreaReservada
    }

################################################################################################
#Bloco 930106 - Risco de Crédito – Empresa e Setor (COMBO SETOR) e Serasa Score Empresa e Setor – PRINAD
################################################################################################
def processaBloco930106(linha):
    DataConsulta = str(linha[7:15]).strip()
    HoraConsulta = str(linha[15:23]).strip()
    MensagemPrinad = str(linha[23:103]).strip()

    return {
        'DataConsulta' : DataConsulta,
        'HoraConsulta' : HoraConsulta,
        'MensagemPrinad' : MensagemPrinad
    }

################################################################################################
#Bloco 930114 - Informações de Riskscoring Classe e texto explicativo (Disponível apenas para o Modelo C56M)
################################################################################################
def processaBloco930114(linha):
    CodClasseC56M = str(linha[7:9]).strip()
    TextoExplicC56M = str(linha[9:109]).strip()

    return {
        'CodClasseC56M' : CodClasseC56M,
        'TextoExplicC56M' : TextoExplicC56M
    }

################################################################################################
#Bloco 930199 - Risco de Crédito – Empresa e Setor (COMBO SETOR) e Serasa Score Empresa e Setor 
################################################################################################
def processaBloco930199(linha):
    Data = str(linha[7:15]).strip()
    Hora = str(linha[15:23]).strip()
    Mensagens = str(linha[23:101]).strip()
    AreaReservada = str(linha[101:103]).strip()
    CodMensagens = str(linha[103:108]).strip()
    AreaReservada2 = str(linha[108:112]).strip()

    return {
        'Data' : Data,
        'Hora' : Hora,
        'Mensagens' : Mensagens,
        'AreaReservada' : AreaReservada,
        'CodMensagens' : CodMensagens,
        'AreaReservada2' : AreaReservada2
    }

################################################################################################
#Bloco 930201 - Risco de Crédito – Empresa e Setor (COMBO SETOR) e Serasa Score Empresa e Setor – PRINAD
################################################################################################
def processaBloco930201(linha):
    Data = str(linha[7:15]).strip()
    Hora = str(linha[15:23]).strip()
    FatorRiskScoringBrasil = str(linha[23:26]).strip()

    return {
        'Data' : Data,
        'Hora' : Hora,
        'FatorRiskScoringBrasil' : FatorRiskScoringBrasil
    }

################################################################################################
#Bloco 930299 - Empresa e Setor (COMBO SETOR) e Serasa Score Empresa e Setor - Mensagem Geral
################################################################################################
def processaBloco930299(linha):
    DataConsulta = str(linha[7:15]).strip()
    HoraConsulta = str(linha[15:23]).strip()
    Mensagem = str(linha[23:123]).strip()

    return {
        'DataConsulta' : DataConsulta,
        'HoraConsulta' : HoraConsulta,
        'MensagemPrMensageminad' : Mensagem
    }

################################################################################################
#Bloco 930298 - Risco de Crédito do Setor – Empresa e Setor (COMBO SETOR) e Serasa Score Empresa e Setor - Mensagem Estado
################################################################################################
def processaBloco930298(linha):
    DataConsulta = str(linha[7:15]).strip()
    HoraConsulta = str(linha[15:23]).strip()
    Mensagem = str(linha[23:123]).strip()

    return {
        'DataConsulta' : DataConsulta,
        'HoraConsulta' : HoraConsulta,
        'MensagemPrMensageminad' : Mensagem
    }

################################################################################################
#Bloco 930297 - Risco de Crédito do Setor – Empresa e Setor (COMBO SETOR) e Serasa Score Empresa e Setor - Mensagem Estado Região 
################################################################################################
def processaBloco930297(linha):
    DataConsulta = str(linha[7:15]).strip()
    HoraConsulta = str(linha[15:23]).strip()
    Mensagem = str(linha[23:123]).strip()

    return {
        'DataConsulta' : DataConsulta,
        'HoraConsulta' : HoraConsulta,
        'MensagemPrMensageminad' : Mensagem
    }
