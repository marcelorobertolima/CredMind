#DadosRiskScoring_07.py
from datetime import datetime
from APICredMind.views.SERASA.mappingsSERASA import *

################################################################################################
#Bloco 070101 - Informações de Riskscoring/PRINAD com 1 casa decimal
#TP INF:   01–CÁLCULO DO RISKSCORING (QUANDO CAMPO RISKSCORING = ‘S’)
#TP INF:   01–CÁLCULO DO RISKSCORING  
#          (QUANDO CAMPO RISKSCORING = ‘E’ e MODELO DIFERENTE DE 'CK30' e 'RK6M')
################################################################################################
def processaBloco070101(linha):
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
#Bloco 070109 - Informações de Riskscoring/PRINAD
#TP INF: 09 – CÁLCULO DO RISKSCORING 
#        (QUANDO CAMPO RISKSCORING = ‘K’ OU ‘M)’ OU 
#        (CAMPO RISKSCORING = ‘E’ e MODELO = 'CK30', 'RK6M', ‘C56M’, ‘C66M’, ‘C61A’) OU 
#        (CAMPO CDOPÇÃO = IPHS)
#----------------------------------------------------------------------------------------------
#Serasa Score com positivo – Empresas – Cálculo
################################################################################################
def processaBloco070109(linha):
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
#Bloco 070102 - Informações de Autorizador (B)
################################################################################################
def processaBloco070102(linha):
    Data = str(linha[7:15]).strip()
    Hora = str(linha[15:23]).strip()
    FatorAutorizadorB = str(linha[23:83]).strip()
    CNAE = str(linha[83:92]).strip()
    AreaReservada = str(linha[92:103]).strip()

    return {
        'Data' : Data,
        'Hora' : Hora,
        'FatorAutorizadorB' : FatorAutorizadorB,
        'CNAE' : CNAE,
        'AreaReservada' : AreaReservada
    }

################################################################################################
#Bloco 070103 - Informações de Autorizador (P) (Q)
################################################################################################
def processaBloco070103(linha):
    Data = str(linha[7:15]).strip()
    Hora = str(linha[15:23]).strip()
    FatorAutorizadorPQ = str(linha[23:83]).strip()
    CNAE = str(linha[83:92]).strip()
    AreaReservada = str(linha[92:103]).strip()

    return {
        'Data' : Data,
        'Hora' : Hora,
        'FatorAutorizadorPQ' : FatorAutorizadorPQ,
        'CNAE' : CNAE,
        'AreaReservada' : AreaReservada
    }

################################################################################################
#Bloco 070104 - Informações de Autorizador (H) 
################################################################################################
def processaBloco070104(linha):
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
#Bloco 070105 - Informações de Autorizador (E)
################################################################################################
def processaBloco070105(linha):
    Data = str(linha[7:15]).strip()
    Hora = str(linha[15:23]).strip()
    FatorAutorizador = str(linha[23:103]).strip()

    return {
        'Data' : Data,
        'Hora' : Hora,
        'FatorAutorizador' : FatorAutorizador
    }

################################################################################################
#Bloco 070106 - Informações de Riskscoring/PRINAD 
################################################################################################
def processaBloco070106(linha):
    Data = str(linha[7:15]).strip()
    Hora = str(linha[15:23]).strip()
    MensagemPrinad = str(linha[23:103]).strip()

    return {
        'Data' : Data,
        'Hora' : Hora,
        'MensagemPrinad' : MensagemPrinad
    }

################################################################################################
#Bloco 070110 - Informações de Riskscoring Customizado (campo score customizado preenchido)
################################################################################################
def processaBloco070110(linha):
    Data = str(linha[7:15]).strip()
    Hora = str(linha[15:23]).strip()
    FatorRiskScoring = str(linha[23:27]).strip()
    FatorPrinad = str(linha[23:31]).strip()
    AreaReservada = str(linha[31:37]).strip()

    return {
        'Data' : Data,
        'Hora' : Hora,
        'FatorRiskScoring' : FatorRiskScoring,
        'FatorPrinad' : FatorPrinad,
        'AreaReservada' : AreaReservada
    }

################################################################################################
#Bloco 070111 - Informações de Riskscoring/PRINAD Customizado (campo score customizado preenchido)
################################################################################################
def processaBloco070111(linha):
    Data = str(linha[7:15]).strip()
    Hora = str(linha[15:23]).strip()
    MensagemPrinad = str(linha[23:103]).strip()

    return {
        'Data' : Data,
        'Hora' : Hora,
        'MensagemPrinad' : MensagemPrinad
    }

################################################################################################
#Bloco 070199 - Informações de Riskscoring/Autorizador 
#Bloco 070199 - Serasa Score com positivo – Empresas – Cálculo
#Bloco 070199 - Serasa Score com positivo – Empresas – Mensagens de não cálculo 
################################################################################################
def processaBloco070199(linha):
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
#Bloco 071099 - Informações de Riskscoring/Autorizador 
################################################################################################
def processaBloco071099(linha):
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
#Bloco 070114 - Informações de Riskscoring Classe e texto explicativo (Disp. apenas p/ Modelo C56M)
################################################################################################
def processaBloco070114(linha):
    CodClasseC56M = str(linha[7:9]).strip()
    TextoExplicC56M = str(linha[9:109]).strip()

    return {
        'CodClasseC56M' : CodClasseC56M,
        'TextoExplicC56M' : TextoExplicC56M
    }

################################################################################################
#Bloco 070195 - Serasa Score com positivo – Empresas – Mensagens informativas
#(HPJ4 – SESARA SCORE COM POSITIVO / HPJ5 – SERASA SCORE EMPRESAS)
#OBS.: Sempre que devolver HPJ5 no campo MOD-POSITIVO significa que o Serasa Score com Positivo 
#      não foi calculado (motivo no campo MSG-POSITIVO – mais informações no item 6. Código das
#      mensagens de retorno) e por isso foi retornado o Serasa Score Empresas. Este bloco não 
#      retorna para HPJ8
################################################################################################
def processaBloco070195(linha):
    CodModelo = str(linha[7:11]).strip()
    CodMsgRetorno = str(linha[11:15]).strip()
    AreaReservada = str(linha[15:301]).strip()

    return {
        'CodModelo' : CodModelo,
        'CodMsgRetorno' : CodMsgRetorno,
        'AreaReservada' : AreaReservada
    }

################################################################################################
#Bloco 070401 - Score Sócios
################################################################################################
def processaBloco070401(linha):
    TipoPessoa = str(linha[7:8]).strip()
    CPFSocio = str(linha[8:17]).strip()
    FilialSocio = str(linha[17:21]).strip()
    DigCPFSocio = str(linha[21:23]).strip()
    SequenciaSocio = str(linha[23:27]).strip()
    
    CodVinculoSocio = str(linha[27:28]).strip()
    DescVinculoSocio = str(linha[27:28]).strip()

    NomeSocio = str(linha[28:98]).strip()
    FatorSocio = str(linha[98:104]).strip()
    FaixaSocio = str(linha[104:110]).strip()
    TaxaSocio = str(linha[110:115]).strip()
    Data = str(linha[115:123]).strip()
    Hora = str(linha[123:131]).strip()
    CodMensagem = str(linha[131:137]).strip()
    DescMensagem = str(linha[137:187]).strip()
    AreaReservada = str(linha[187:193]).strip()

    return {
        'TipoPessoa' : TipoPessoa,
        'CPFSocio' : CPFSocio,
        'FilialSocio' : FilialSocio,
        'DigCPFSocio' : DigCPFSocio,
        'SequenciaSocio' : SequenciaSocio,
        'CodVinculoSocio' : CodVinculoSocio,
        'DescVinculoSocio' : DescVinculoSocio,
        'NomeSocio' : NomeSocio,
        'FatorSocio' : FatorSocio,
        'FaixaSocio' : FaixaSocio,
        'TaxaSocio' : TaxaSocio,
        'Data' : Data,
        'Hora' : Hora,
        'CodMensagem' : CodMensagem,
        'DescMensagem' : DescMensagem,
        'AreaReservada' : AreaReservada
    }
