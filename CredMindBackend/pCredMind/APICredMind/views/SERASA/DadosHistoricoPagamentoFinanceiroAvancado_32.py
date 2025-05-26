#DadosHistoricoPagamentoFinanceiroAvancado_32.py
from datetime import datetime
from APICredMind.views.SERASA.mappingsSERASA import *

################################################################################################
#Bloco 320101 - Compromisso por linha de crédito
################################################################################################
def processaBloco320101(linha):
    PercFinanciamento = str(linha[7:10]).strip()
    PercEmprestimo = str(linha[10:13]).strip()
    PercRotativo = str(linha[13:16]).strip()
    PercOutros = str(linha[16:19]).strip()
    CodFaixaTotalComprom = str(linha[19:22]).strip()
    ValorComprom = str(linha[22:43]).strip()
    
    return {
        'PercFinanciamento': PercFinanciamento,
        'PercEmprestimo': PercEmprestimo,
        'PercRotativo': PercRotativo,
        'PercOutros': PercOutros,
        'CodFaixaTotalComprom': CodFaixaTotalComprom,
        'ValorComprom': ValorComprom
    }

################################################################################################
#Bloco 320102 - Quantidade de compromissos e credores
################################################################################################
def processaBloco320102(linha):
    CodFaixaQtdeComprom = str(linha[7:10]).strip()
    QtdeComprom = str(linha[10:31]).strip()
    QtdeCredores = str(linha[31:41]).strip()
    
    return {
        'CodFaixaQtdeComprom': CodFaixaQtdeComprom,
        'QtdeComprom': QtdeComprom,
        'QtdeCredores': QtdeCredores
    }

################################################################################################
#Bloco 320103 - Percentual das parcelas dos compromissos
################################################################################################
def processaBloco320103(linha):
    PercParcPagas = str(linha[7:10]).strip()
    PercParcAVencer = str(linha[10:13]).strip()
    PercParcEmAberto = str(linha[13:16]).strip()
    
    return {
        'PercParcPagas': PercParcPagas,
        'PercParcAVencer': PercParcAVencer,
        'PercParcEmAberto': PercParcEmAberto
    }

################################################################################################
#Bloco 320104 - Compromissos pagos – últimos 5 anos (valores em reais)
#OBS: Caso o cliente não tenha nenhum compromisso pago, este bloco não retornará.
################################################################################################
def processaBloco320104(linha):
    CodFaixaTotalPago = str(linha[7:10]).strip()
    ValorTotalPago = str(linha[10:31]).strip()
    CodFaixaRotativo = str(linha[31:34]).strip()
    ValorPagoRotativo = str(linha[34:55]).strip()
    PercRotativo = str(linha[55:72]).strip()
    CodFaixaPontual = str(linha[72:75]).strip()
    ValorPagoPontual = str(linha[75:96]).strip()
    PercPontual = str(linha[96:113]).strip()
    CodFaixaAte30dias = str(linha[113:116]).strip()
    ValorPagoAte30dias = str(linha[116:137]).strip()
    PercAte30dias = str(linha[137:154]).strip()
    CodFaixaDe31a60 = str(linha[154:157]).strip()
    ValorPagoDe31a60 = str(linha[157:178]).strip()
    PercDe31a60 = str(linha[178:195]).strip()
    CodFaixaAcima60 = str(linha[195:198]).strip()
    ValorPagoAcima60 = str(linha[198:219]).strip()
    PercAcima60 = str(linha[219:236]).strip()
    
    return {
        'CodFaixaTotalPago': CodFaixaTotalPago,
        'ValorTotalPago': ValorTotalPago,
        'CodFaixaRotativo': CodFaixaRotativo,
        'ValorPagoRotativo': ValorPagoRotativo,
        'PercRotativo': PercRotativo,
        'CodFaixaPontual': CodFaixaPontual,
        'ValorPagoPontual': ValorPagoPontual,
        'PercPontual': PercPontual,
        'CodFaixaAte30dias': CodFaixaAte30dias,
        'ValorPagoAte30dias': ValorPagoAte30dias,
        'PercAte30dias': PercAte30dias,
        'CodFaixaDe31a60': CodFaixaDe31a60,
        'ValorPagoDe31a60': ValorPagoDe31a60,
        'PercDe31a60': PercDe31a60,
        'CodFaixaAcima60': CodFaixaAcima60,
        'ValorPagoAcima60': ValorPagoAcima60,
        'PercAcima60': PercAcima60
    }

################################################################################################
#Bloco 320199 - Mensagens da feature
################################################################################################
def processaBloco320199(linha):
    Mensagem = str(linha[7:107]).strip()
    
    return {
        'Mensagem': Mensagem
    }

################################################################################################
#Bloco 320201 - Compromissos ativos por linha de crédito
################################################################################################
def processaBloco320201(linha):
    PercFinanciamento = str(linha[7:10]).strip()
    PercEmprestimo = str(linha[10:13]).strip()
    PercRotativo = str(linha[13:16]).strip()
    PercOutros = str(linha[16:19]).strip()
    CodFaixaTotalComprom = str(linha[19:22]).strip()
    ValorComprom = str(linha[22:43]).strip()
    
    return {
        'PercFinanciamento': PercFinanciamento,
        'PercEmprestimo': PercEmprestimo,
        'PercRotativo': PercRotativo,
        'PercOutros': PercOutros,
        'CodFaixaTotalComprom': CodFaixaTotalComprom,
        'ValorComprom': ValorComprom
    }


################################################################################################
#Bloco 320202 - Quantidade de compromissos e credores ATIVOS
################################################################################################
def processaBloco320202(linha):
    CodFaixaQtdeComprom = str(linha[7:10]).strip()
    QtdeComprom = str(linha[10:31]).strip()
    QtdeCredores = str(linha[31:41]).strip()
    
    return {
        'CodFaixaQtdeComprom': CodFaixaQtdeComprom,
        'QtdeComprom': QtdeComprom,
        'QtdeCredores': QtdeCredores
    }

################################################################################################
#Bloco 320203 - Percentual de parcelas de compromissos ativos
################################################################################################
def processaBloco320203(linha):
    PercParcPagas = str(linha[7:10]).strip()
    PercParcAVencer = str(linha[10:13]).strip()
    PercParcEmAberto = str(linha[13:16]).strip()
    
    return {
        'PercParcPagas': PercParcPagas,
        'PercParcAVencer': PercParcAVencer,
        'PercParcEmAberto': PercParcEmAberto
    }

################################################################################################
#Bloco 320204 - Contratos ativos 
################################################################################################
def processaBloco320204(linha):
    PercContratosAtivosPagos = str(linha[7:10]).strip()
    PercContratosAtivosPagosAVencer = str(linha[10:13]).strip()
    PercContratosAtivosPagosEmAberto = str(linha[13:16]).strip()
    CodFaixaContratosAtivos = str(linha[16:19]).strip()
    ValorContratosAtivos = str(linha[19:40]).strip()
    
    return {
        'PercContratosAtivosPagos': PercContratosAtivosPagos,
        'PercContratosAtivosPagosAVencer': PercContratosAtivosPagosAVencer,
        'PercContratosAtivosPagosEmAberto': PercContratosAtivosPagosEmAberto,
        'CodFaixaContratosAtivos': CodFaixaContratosAtivos,
        'ValorContratosAtivos': ValorContratosAtivos
    }

################################################################################################
#Bloco 320205 - Pontualidade de pagamento
################################################################################################
def processaBloco320205(linha):
    PercRotativo = str(linha[7:10]).strip()
    PercPontual = str(linha[10:13]).strip()
    PercAte30 = str(linha[13:16]).strip()
    Perc31a60 = str(linha[16:19]).strip()
    PercAcima60 = str(linha[19:22]).strip()
    CodFaixaCompromPagos = str(linha[22:25]).strip()
    ValorCompromPagos = str(linha[25:46]).strip()
    
    return {
        'PercRotativo': PercRotativo,
        'PercPontual': PercPontual,
        'PercAte30': PercAte30,
        'Perc31a60': Perc31a60,
        'PercAcima60': PercAcima60,
        'CodFaixaCompromPagos': CodFaixaCompromPagos,
        'ValorCompromPagos': ValorCompromPagos
    }

################################################################################################
#Bloco 320206 - Vencimentos em aberto
################################################################################################
def processaBloco320206(linha):
    PercAbertos30 = str(linha[7:10]).strip()
    PercAberto31a60 = str(linha[10:13]).strip()
    PercAbertos61a90 = str(linha[13:16]).strip()
    PercAbertosAcima90 = str(linha[16:19]).strip()
    CodFaixaCompromAbertos = str(linha[19:22]).strip()
    ValorCompromAbertos = str(linha[22:43]).strip()
    
    return {
        'PercAbertos30': PercAbertos30,
        'PercAberto31a60': PercAberto31a60,
        'PercAbertos61a90': PercAbertos61a90,
        'PercAbertosAcima90': PercAbertosAcima90,
        'CodFaixaCompromAbertos': CodFaixaCompromAbertos,
        'ValorCompromAbertos': ValorCompromAbertos
    }

################################################################################################
#Bloco 320297 - Mensagem de pontualidade de pagamento
#Obs.: Sempre que retornar este bloco, o bloco 320205 não retornará.
################################################################################################
def processaBloco320297(linha):
    Mensagem = str(linha[7:107]).strip()
    
    return {
        'Mensagem': Mensagem
    }

################################################################################################
#Bloco 320298 - Mensagem de vencimentos em aberto
#Obs.: Sempre que retornar este bloco, o bloco 320206 não retornará.
################################################################################################
def processaBloco320298(linha):
    Mensagem = str(linha[7:107]).strip()
    
    return {
        'Mensagem': Mensagem
    }

################################################################################################
#Bloco 320299 - Mensagem de contratos ativos
#Obs.: Sempre que retornar este bloco, nenhum bloco 3202xx retornará.
################################################################################################
def processaBloco320299(linha):
    Mensagem = str(linha[7:107]).strip()
    
    return {
        'Mensagem': Mensagem
    }
