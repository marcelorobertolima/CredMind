#DadosAlertaCadastralEmpresa_60.py
from datetime import datetime
from APICredMind.views.SERASA.mappingsSERASA import *

################################################################################################
#Bloco 600099 - Alerta Cadastral da Empresa – Mensagens geral 
################################################################################################
def processaBloco600099(linha):
    CodAlteracao = str(linha[7:10]).strip()
    Mensagem = str(linha[10:110]).strip()

    return {
        'CodAlteracao' : CodAlteracao,
        'Mensagem' : Mensagem
    }

################################################################################################
#Bloco 600101 - Alerta Cadastral da Empresa – Dados da Consulta do Alerta Alteração da Razão Social
################################################################################################
def processaBloco600101(linha):
    CodAlteracao = str(linha[7:10]).strip()
    QtdeAlertas = str(linha[10:19]).strip()
    DataGeracaoAlerta = str(linha[19:27]).strip()
    DataIncioPesq = str(linha[27:35]).strip()
    DataFinalPesq = str(linha[35:43]).strip()

    return {
        'CodAlteracao' : CodAlteracao,
        'QtdeAlertas' : QtdeAlertas,
        'DataGeracaoAlerta' : DataGeracaoAlerta,
        'DataIncioPesq' : DataIncioPesq,
        'DataFinalPesq' : DataFinalPesq
    }

################################################################################################
#Bloco 600102 - Alerta Cadastral da Empresa – Alteração da Razão Social
################################################################################################
def processaBloco600102(linha):
    CodAlteracao = str(linha[7:10]).strip()
    RazaoSocialAnterior = str(linha[10:80]).strip()
    RazaoSocialAtual = str(linha[80:150]).strip()
    DataAlteracao = str(linha[150:158]).strip()

    return {
        'CodAlteracao' : CodAlteracao,
        'RazaoSocialAnterior' : RazaoSocialAnterior,
        'RazaoSocialAtual' : RazaoSocialAtual,
        'DataAlteracao' : DataAlteracao
    }

################################################################################################
#Bloco 600199 - Alerta Cadastral da Empresa – Mensagens
################################################################################################
def processaBloco600199(linha):
    CodAlteracao = str(linha[7:10]).strip()
    Mensagem = str(linha[10:89]).strip()

    return {
        'CodAlteracao' : CodAlteracao,
        'Mensagem' : Mensagem
    }

################################################################################################
#Bloco 600201 - Alerta Cadastral da Empresa – Dados da Consulta do Alerta Alteração no Ramo de Atividade 
################################################################################################
def processaBloco600201(linha):
    CodAlteracao = str(linha[7:10]).strip()
    QtdeAlertas = str(linha[10:19]).strip()
    DataGeracaoAlerta = str(linha[19:27]).strip()
    DataInicioPesquisa = str(linha[27:35]).strip()
    DataFinalPesquisa = str(linha[35:43]).strip()

    return {
        'CodAlteracao' : CodAlteracao,
        'QtdeAlertas' : QtdeAlertas,
        'DataGeracaoAlerta' : DataGeracaoAlerta,
        'DataInicioPesquisa' : DataInicioPesquisa,
        'DataFinalPesquisa' : DataFinalPesquisa
    }

################################################################################################
#Bloco 600202 - Alerta Cadastral da Empresa – Alteração no Ramo de Atividade
################################################################################################
def processaBloco600202(linha):
    CodAlteracao = str(linha[7:10]).strip()
    CodCNAEAtual = str(linha[10:15]).strip()
    DigCNAEAtual = str(linha[15:17]).strip()
    DescCNAEAtual = str(linha[17:97]).strip()
    CodCNAEAnterior = str(linha[97:102]).strip()
    DigCNAEAnterior = str(linha[102:104]).strip()
    DescCNAEAnterior = str(linha[104:184]).strip()
    DataAlteracaoRamoAtividade = str(linha[184:192]).strip()

    return {
        'CodAlteracao' : CodAlteracao,
        'CodCNAEAtual' : CodCNAEAtual,
        'DigCNAEAtual' : DigCNAEAtual,
        'DescCNAEAtual' : DescCNAEAtual,
        'CodCNAEAnterior' : CodCNAEAnterior,
        'DigCNAEAnterior' : DigCNAEAnterior,
        'DescCNAEAnterior' : DescCNAEAnterior,
        'DataAlteracaoRamoAtividade' : DataAlteracaoRamoAtividade
    }

################################################################################################
#Bloco 600299 - Alerta Cadastral da Empresa – Mensagens
################################################################################################
def processaBloco600299(linha):
    CodAlteracao = str(linha[7:10]).strip()
    Mensagem = str(linha[10:89]).strip()

    return {
        'CodAlteracao' : CodAlteracao,
        'Mensagem' : Mensagem
    }

################################################################################################
#Bloco 600301 - Alerta Cadastral da Empresa – Dados da Consulta do Alerta Alteração no Endereço
################################################################################################
def processaBloco600301(linha):
    CodAlteracao = str(linha[7:10]).strip()
    QtdeAlertas = str(linha[10:19]).strip()
    DataGeracaoAlerta = str(linha[19:27]).strip()
    DataInicioPesquisa = str(linha[27:35]).strip()
    DataFinalPesquisa = str(linha[35:43]).strip()

    return {
        'CodAlteracao' : CodAlteracao,
        'QtdeAlertas' : QtdeAlertas,
        'DataGeracaoAlerta' : DataGeracaoAlerta,
        'DataInicioPesquisa' : DataInicioPesquisa,
        'DataFinalPesquisa' : DataFinalPesquisa
    }

################################################################################################
#Bloco 600302 - Alerta Cadastral da Empresa – Alteração no Endereço
################################################################################################
def processaBloco600302(linha):
    CodAlteracao = str(linha[7:10]).strip()
    LogradouroAtual = str(linha[10:40]).strip()
    ComplLogradouroAtual = str(linha[40:50]).strip()
    BairroAtual = str(linha[50:70]).strip()
    CEPAtual = str(linha[70:78]).strip()
    UFAtual = str(linha[78:80]).strip()
    CodPostalAtual = str(linha[80:88]).strip()
    CEPCodPostalAtual = str(linha[88:96]).strip()
    LogradouroAnterior = str(linha[96:126]).strip()
    ComplLogradouroAnterior = str(linha[126:136]).strip()
    BairroAnterior = str(linha[136:156]).strip()
    CEPAnterior = str(linha[156:164]).strip()
    UFAnterior = str(linha[164:166]).strip()
    CodPostalAnterior = str(linha[166:174]).strip()
    CEPCodPostalAnterior = str(linha[174:182]).strip()
    DataAlteracaoEndereco = str(linha[182:190]).strip()
    
    return {
        'CodAlteracao': CodAlteracao,
        'LogradouroAtual': LogradouroAtual,
        'ComplLogradouroAtual': ComplLogradouroAtual,
        'BairroAtual': BairroAtual,
        'CEPAtual': CEPAtual,
        'UFAtual': UFAtual,
        'CodPostalAtual': CodPostalAtual,
        'CEPCodPostalAtual': CEPCodPostalAtual,
        'LogradouroAnterior': LogradouroAnterior,
        'ComplLogradouroAnterior': ComplLogradouroAnterior,
        'BairroAnterior': BairroAnterior,
        'CEPAnterior': CEPAnterior,
        'UFAnterior': UFAnterior,
        'CodPostalAnterior': CodPostalAnterior,
        'CEPCodPostalAnterior': CEPCodPostalAnterior,
        'DataAlteracaoEndereco': DataAlteracaoEndereco
    }

################################################################################################
#Bloco 600399 - Alerta Cadastral da Empresa – Mensagens
################################################################################################
def processaBloco600399(linha):
    CodAlteracao = str(linha[7:10]).strip()
    Mensagem = str(linha[10:89]).strip()

    return {
        'CodAlteracao' : CodAlteracao,
        'Mensagem' : Mensagem
    }

################################################################################################
#Bloco 600401 - Alerta Cadastral da Empresa – Dados da Consulta do Alerta Alteração no Endereço
################################################################################################
def processaBloco600401(linha):
    CodAlteracao = str(linha[7:10]).strip()
    DataGeracaoAlerta = str(linha[10:18]).strip()
    DataInicioPesquisa = str(linha[18:26]).strip()
    DataFinalPesquisa = str(linha[26:34]).strip()

    return {
        'CodAlteracao' : CodAlteracao,
        'DataGeracaoAlerta' : DataGeracaoAlerta,
        'DataInicioPesquisa' : DataInicioPesquisa,
        'DataFinalPesquisa' : DataFinalPesquisa
    }

################################################################################################
#Bloco 600402 - Alerta Cadastral da Empresa – Alteração no Tipo Societário
################################################################################################
def processaBloco600402(linha):
    CodAlteracao = str(linha[7:10]).strip()
    AreaReservada = str(linha[10:11]).strip()
    TipoSocietarioAtual = str(linha[11:55]).strip()
    AreaReservada2 = str(linha[55:56]).strip()
    TipoSocietarioAnterior = str(linha[56:100]).strip()
    DataAltTipoSocietario = str(linha[100:108]).strip()

    return {
        'CodAlteracao' : CodAlteracao,
        'AreaReservada' : AreaReservada,
        'TipoSocietarioAtual' : TipoSocietarioAtual,
        'AreaReservada2' : AreaReservada2,
        'TipoSocietarioAnterior' : TipoSocietarioAnterior,
        'DataAltTipoSocietario' : DataAltTipoSocietario
    }

################################################################################################
#Bloco 600499 - Alerta Cadastral da Empresa – Mensagens
################################################################################################
def processaBloco600499(linha):
    CodAlteracao = str(linha[7:10]).strip()
    Mensagem = str(linha[10:89]).strip()

    return {
        'CodAlteracao' : CodAlteracao,
        'Mensagem' : Mensagem
    }

################################################################################################
#Bloco 600501 - Alerta Cadastral da Empresa – Dados da Consulta do Alerta Alteração no Endereço
################################################################################################
def processaBloco600501(linha):
    CodAlteracao = str(linha[7:10]).strip()
    DataGeracaoAlerta = str(linha[10:18]).strip()
    DataInicioPesquisa = str(linha[18:26]).strip()
    DataFinalPesquisa = str(linha[26:34]).strip()

    return {
        'CodAlteracao' : CodAlteracao,
        'DataGeracaoAlerta' : DataGeracaoAlerta,
        'DataInicioPesquisa' : DataInicioPesquisa,
        'DataFinalPesquisa' : DataFinalPesquisa
    }

################################################################################################
#Bloco 600502 - Alerta Cadastral da Empresa – Alteração no Enquadramento Fiscal
################################################################################################
def processaBloco600502(linha):
    CodAlteracao = str(linha[7:10]).strip()
    EnquadFiscalAtual = str(linha[10:13]).strip()
    EnquadFiscalAnterior = str(linha[13:16]).strip()
    DataAltEnquadFiscal = str(linha[16:24]).strip()

    return {
        'CodAlteracao' : CodAlteracao,
        'EnquadFiscalAtual' : EnquadFiscalAtual,
        'EnquadFiscalAnterior' : EnquadFiscalAnterior,
        'DataAltEnquadFiscal' : DataAltEnquadFiscal
    }

################################################################################################
#Bloco 600599 - Alerta Cadastral da Empresa – Mensagens
################################################################################################
def processaBloco600599(linha):
    CodAlteracao = str(linha[7:10]).strip()
    Mensagem = str(linha[10:89]).strip()

    return {
        'CodAlteracao' : CodAlteracao,
        'Mensagem' : Mensagem
    }

################################################################################################
#Bloco 600601 - Alerta Cadastral da Empresa – Dados da Consulta do Alerta Presença de Cadastro na CGU
################################################################################################
def processaBloco600601(linha):
    CodAlteracao = str(linha[7:10]).strip()
    MsgAlteracao = str(linha[10:89]).strip()
    DataInclusaoMsg = str(linha[89:97]).strip()

    return {
        'CodAlteracao' : CodAlteracao,
        'MsgAlteracao' : MsgAlteracao,
        'DataInclusaoMsg' : DataInclusaoMsg
    }

################################################################################################
#Bloco 600699 - Alerta Cadastral da Empresa – Mensagens
################################################################################################
def processaBloco600699(linha):
    CodAlteracao = str(linha[7:10]).strip()
    Mensagem = str(linha[10:89]).strip()

    return {
        'CodAlteracao' : CodAlteracao,
        'Mensagem' : Mensagem
    }

################################################################################################
#Bloco 600701 - Alerta Cadastral da Empresa – Dados da Consulta do Alerta Inconsistências Comerciais
################################################################################################
def processaBloco600701(linha):
    CodAlteracao = str(linha[7:10]).strip()
    QtdeAlertas = str(linha[10:19]).strip()
    DataGeracaoAlerta = str(linha[19:27]).strip()
    DataIncioPesq = str(linha[27:35]).strip()
    DataFinalPesq = str(linha[35:43]).strip()

    return {
        'CodAlteracao' : CodAlteracao,
        'QtdeAlertas' : QtdeAlertas,
        'DataGeracaoAlerta' : DataGeracaoAlerta,
        'DataIncioPesq' : DataIncioPesq,
        'DataFinalPesq' : DataFinalPesq
    }

################################################################################################
#Bloco 600702 - Alerta Cadastral da Empresa – Inconsistências Comerciais
################################################################################################
def processaBloco600702(linha):
    CodMensagem = str(linha[7:10]).strip()
    
    CodAlerta = str(linha[10:11]).strip()
    DescAlerta = buscaTipoCodAlerta(str(linha[10:11]).strip())
    
    FraseAlerta = str(linha[11:135]).strip()
    DataAlteracao = str(linha[135:143]).strip()

    return {
        'CodMensagem' : CodMensagem,
        'CodAlerta' : CodAlerta,
        'DescAlerta' : DescAlerta,
        'FraseAlerta' : FraseAlerta,
        'DataAlteracao' : DataAlteracao
    }

################################################################################################
#Bloco 600799 - Alerta Cadastral da Empresa – Mensagens
################################################################################################
def processaBloco600799(linha):
    CodAlteracao = str(linha[7:10]).strip()
    Mensagem = str(linha[10:89]).strip()

    return {
        'CodAlteracao' : CodAlteracao,
        'Mensagem' : Mensagem
    }
