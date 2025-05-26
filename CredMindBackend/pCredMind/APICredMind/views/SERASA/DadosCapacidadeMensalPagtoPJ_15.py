#DadosCapacidadeMensalPagtoPJ_15.py
from datetime import datetime
from APICredMind.views.SERASA.mappingsSERASA import *

################################################################################################
#Bloco 150101 - Bloco de Cálculo
################################################################################################
def processaBloco150101(linha):
    Data = str(linha[7:15]).strip()
    Hora = str(linha[15:23]).strip()
    ValorCapacMensalPagtoPJ = str(linha[23:39]).strip() #0 a 100
    Prinad = str(linha[39:44]).strip()
    
    return {
        'Data': Data,
        'Hora': Hora,
        'ValorCapacMensalPagtoPJ': ValorCapacMensalPagtoPJ,
        'Prinad': Prinad
    }

################################################################################################
#Bloco 150102 - Bloco de Cálculo com Filtro de Mensagem
################################################################################################
def processaBloco150102(linha):
    Data = str(linha[7:15]).strip()
    Hora = str(linha[15:23]).strip()
    Score = str(linha[23:30]).strip() #SITUAÇÃO DE CNPJ RETORNA 1 / SITUAÇÃO DEFAULT RETORNA 2
    MsgScoreMotor = 'SITUAÇÃO DE CNPJ RETORNA 1 /// SITUAÇÃO DEFAULT RETORNA 2'
    Prinad = str(linha[30:35]).strip()
    CodMsgErroRetorno = str(linha[35:38]).strip()
    MsgErroRetorno = str(linha[38:118]).strip()
    
    return {
        'Data': Data,
        'Hora': Hora,
        'Score': Score,
        'MsgScoreMotor': MsgScoreMotor,
        'Prinad': Prinad,
        'CodMsgErroRetorno': CodMsgErroRetorno,
        'MsgErroRetorno': MsgErroRetorno
    }

################################################################################################
#Bloco 150109 - Bloco de Não Cálculo ou Mensagens de Erro
################################################################################################
def processaBloco150109(linha):
    Data = str(linha[7:15]).strip()
    Hora = str(linha[15:23]).strip()
    CodMsgErro = str(linha[23:27]).strip() #0 a 100
    MsgErroRetorno = str(linha[27:107]).strip()
    
    return {
        'Data': Data,
        'Hora': Hora,
        'CodMsgErro': CodMsgErro,
        'MsgErroRetorno': MsgErroRetorno
    }

