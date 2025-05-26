#DadosAlertaCadastralSociosAdmin_61.py
from datetime import datetime
from APICredMind.views.SERASA.mappingsSERASA import *

################################################################################################
#Bloco 610101 - Alerta Cadastral dos Sócios e Administradores – Dados da Consulta do Alerta Alteração dos Sócios
################################################################################################
def processaBloco610101(linha):
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
#Bloco 610102 - Alerta Cadastral dos Sócios e Administradores – Alteração dos Sócios
################################################################################################
def processaBloco610102(linha):
    CodAlteracao = str(linha[7:10]).strip()
    NomeSocio = str(linha[10:80]).strip()
    NumCPFCNPJ = str(linha[80:89]).strip()
    FilialCPFCNPJ = str(linha[89:93]).strip()
    DigCPFCNPJ = str(linha[93:95]).strip()
    TipoDcto = str(linha[95:96]).strip()
    EntradaSaida = str(linha[96:97]).strip()
    DataEntradaSaida = str(linha[97:105]).strip()

    return {
        'CodAlteracao' : CodAlteracao,
        'NomeSocio' : NomeSocio,
        'NumCPFCNPJ' : NumCPFCNPJ,
        'FilialCPFCNPJ' : FilialCPFCNPJ,
        'DigCPFCNPJ' : DigCPFCNPJ,
        'TipoDcto' : TipoDcto,
        'EntradaSaida' : EntradaSaida,
        'DataEntradaSaida' : DataEntradaSaida
    }

################################################################################################
#Bloco 610199 - Alerta Cadastral dos Sócios e Administradores – Mensagens
################################################################################################
def processaBloco610199(linha):
    CodAlteracao = str(linha[7:10]).strip()
    Mensagem = str(linha[10:89]).strip()

    return {
        'CodAlteracao' : CodAlteracao,
        'Mensagem' : Mensagem
    }

################################################################################################
#Bloco 610201 - Alerta Cadastral dos Sócios e Administradores – Dados da Consulta do Alerta Alteração dos Administradores 
################################################################################################
def processaBloco610201(linha):
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
#Bloco 610202 - Alerta Cadastral dos Sócios e Administradores – Alteração dos Sócios
################################################################################################
def processaBloco610202(linha):
    CodAlteracao = str(linha[7:10]).strip()
    NomeSocio = str(linha[10:80]).strip()
    NumCPFCNPJ = str(linha[80:89]).strip()
    FilialCPFCNPJ = str(linha[89:93]).strip()
    DigCPFCNPJ = str(linha[93:95]).strip()
    TipoDcto = str(linha[95:96]).strip()
    EntradaSaida = str(linha[96:97]).strip()
    DataEntradaSaida = str(linha[97:105]).strip()

    return {
        'CodAlteracao' : CodAlteracao,
        'NomeSocio' : NomeSocio,
        'NumCPFCNPJ' : NumCPFCNPJ,
        'FilialCPFCNPJ' : FilialCPFCNPJ,
        'DigCPFCNPJ' : DigCPFCNPJ,
        'TipoDcto' : TipoDcto,
        'EntradaSaida' : EntradaSaida,
        'DataEntradaSaida' : DataEntradaSaida
    }

################################################################################################
#Bloco 610299 - Alerta Cadastral dos Sócios e Administradores – Mensagens
################################################################################################
def processaBloco610299(linha):
    CodAlteracao = str(linha[7:10]).strip()
    Mensagem = str(linha[10:89]).strip()

    return {
        'CodAlteracao' : CodAlteracao,
        'Mensagem' : Mensagem
    }

################################################################################################
#Bloco 610301 - Alerta Cadastral dos Sócios e Administradores – Dados da Consulta do Alerta Inconsistências Societárias PJ
################################################################################################
def processaBloco610301(linha):
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
#Bloco 610302 - Alerta Cadastral dos Sócios e Administradores – Alteração dos Sócios
################################################################################################
def processaBloco610302(linha):
    CodAlteracao = str(linha[7:10]).strip()

    CodAlerta = str(linha[10:11]).strip()
    DescAlerta = buscaTipoCodAlerta(str(linha[10:11]).strip())

    NomeSocio = str(linha[11:81]).strip()
    NumCPFCNPJ = str(linha[81:90]).strip()
    FilialCPFCNPJ = str(linha[90:94]).strip()
    DigCPFCNPJ = str(linha[94:96]).strip()
    TipoDcto = str(linha[96:97]).strip()
    FraseInconsistencia = str(linha[97:221]).strip()
    DataEntradaSaida = str(linha[221:229]).strip()

    return {
        'CodAlteracao' : CodAlteracao,
        'CodAlerta': CodAlerta,
        'DescAlerta': DescAlerta,
        'NomeSocio' : NomeSocio,
        'NumCPFCNPJ' : NumCPFCNPJ,
        'FilialCPFCNPJ' : FilialCPFCNPJ,
        'DigCPFCNPJ' : DigCPFCNPJ,
        'TipoDcto' : TipoDcto,
        'FraseInconsistencia' : FraseInconsistencia,
        'DataEntradaSaida' : DataEntradaSaida
    }

################################################################################################
#Bloco 610399 - Alerta Cadastral dos Sócios e Administradores – Mensagens
################################################################################################
def processaBloco610399(linha):
    CodAlteracao = str(linha[7:10]).strip()
    Mensagem = str(linha[10:89]).strip()

    return {
        'CodAlteracao' : CodAlteracao,
        'Mensagem' : Mensagem
    }

################################################################################################
#Bloco 610401 - Alerta Cadastral dos Sócios e Administradores – Dados da Consulta do Alerta Inconsistências Administrativa PJ
################################################################################################
def processaBloco610401(linha):
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
#Bloco 610402 - Alerta Cadastral dos Sócios e Administradores – Inconsistências Administrativa PJ
################################################################################################
def processaBloco610402(linha):
    CodAlteracao = str(linha[7:10]).strip()

    CodAlerta = str(linha[10:11]).strip()
    DescAlerta = buscaTipoCodAlerta(str(linha[10:11]).strip())

    NomeSocio = str(linha[11:81]).strip()
    NumCPFCNPJ = str(linha[81:90]).strip()
    FilialCPFCNPJ = str(linha[90:94]).strip()
    DigCPFCNPJ = str(linha[94:96]).strip()
    TipoDcto = str(linha[96:97]).strip()
    FraseInconsistencia = str(linha[97:221]).strip()
    DataEntradaSaida = str(linha[221:229]).strip()

    return {
        'CodAlteracao' : CodAlteracao,
        'CodAlerta': CodAlerta,
        'DescAlerta': DescAlerta,
        'NomeSocio' : NomeSocio,
        'NumCPFCNPJ' : NumCPFCNPJ,
        'FilialCPFCNPJ' : FilialCPFCNPJ,
        'DigCPFCNPJ' : DigCPFCNPJ,
        'TipoDcto' : TipoDcto,
        'FraseInconsistencia' : FraseInconsistencia,
        'DataEntradaSaida' : DataEntradaSaida
    }

################################################################################################
#Bloco 610499 - Alerta Cadastral dos Sócios e Administradores – Mensagens
################################################################################################
def processaBloco610499(linha):
    CodAlteracao = str(linha[7:10]).strip()
    Mensagem = str(linha[10:89]).strip()

    return {
        'CodAlteracao' : CodAlteracao,
        'Mensagem' : Mensagem
    }

################################################################################################
#Bloco 610501 - Alerta Cadastral dos Sócios e Administradores – Dados da Consulta do Alerta Presença de Óbitos dos Sócios PF
################################################################################################
def processaBloco610501(linha):
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
#Bloco 610502 - Alerta Cadastral dos Sócios e Administradores – Presença de Óbitos dos Sócios PF
################################################################################################
def processaBloco610502(linha):
    CodAlteracao = str(linha[7:10]).strip()
    NumCPF = str(linha[10:19]).strip()
    DigCPF = str(linha[19:21]).strip()
    CodObito = str(linha[21:25]).strip()

    return {
        'CodAlteracao' : CodAlteracao,
        'NumCPF' : NumCPF,
        'DigCPF' : DigCPF,
        'CodObito' : CodObito
    }

################################################################################################
#Bloco 610599 - Alerta Cadastral dos Sócios e Administradores – Mensagens
################################################################################################
def processaBloco610599(linha):
    CodAlteracao = str(linha[7:10]).strip()
    Mensagem = str(linha[10:89]).strip()

    return {
        'CodAlteracao' : CodAlteracao,
        'Mensagem' : Mensagem
    }

################################################################################################
#Bloco 610601 - Alerta Cadastral dos Sócios e Administradores – Dados da Consulta do Alerta Presença de Óbitos dos Administradores PF
################################################################################################
def processaBloco610601(linha):
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
#Bloco 610602 - Alerta Cadastral dos Sócios e Administradores – Presença de Óbitos dos Administradores PF
################################################################################################
def processaBloco610602(linha):
    CodAlteracao = str(linha[7:10]).strip()
    NumCPF = str(linha[10:19]).strip()
    DigCPF = str(linha[19:21]).strip()
    CodObito = str(linha[21:25]).strip()
    DataPrensObitoAdminPF = str(linha[25:33]).strip()

    return {
        'CodAlteracao' : CodAlteracao,
        'NumCPF' : NumCPF,
        'DigCPF' : DigCPF,
        'CodObito' : CodObito,
        'DataPrensObitoAdminPF': DataPrensObitoAdminPF
    }

################################################################################################
#Bloco 610699 - Alerta Cadastral dos Sócios e Administradores – Mensagens
################################################################################################
def processaBloco610699(linha):
    CodAlteracao = str(linha[7:10]).strip()
    Mensagem = str(linha[10:89]).strip()

    return {
        'CodAlteracao' : CodAlteracao,
        'Mensagem' : Mensagem
    }
