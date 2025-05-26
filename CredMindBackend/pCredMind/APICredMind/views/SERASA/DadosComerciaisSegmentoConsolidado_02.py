#DadosComerciaisSegmentoConsolidado_03.py
from datetime import datetime
from APICredMind.views.SERASA.mappingsSERASA import *

################################################################################################
#Bloco 020111 - Principais Fornecedores – Data da Última Atualização (Segmento Consolidado) 
################################################################################################
def processaBloco020111(linha):
    DataUltimaAtualizacaoBloco = str(linha[7:15]).strip()
    SegmentoOrigemInformacao = str(linha[15:18]).strip()

    return {
        'DataUltimaAtualizacaoBloco' : DataUltimaAtualizacaoBloco,
        'SegmentoOrigemInformacao' : SegmentoOrigemInformacao
    }

################################################################################################
#Bloco 020112 - Principais Fornecedores (Segmento Consolidado)
################################################################################################
def processaBloco020112(linha):
    NomeFonteInf = str(linha[7:77]).strip()
    CNPJFonteInf = str(linha[77:86]).strip()
    FilialFonteInf = str(linha[86:90]).strip()
    DigCNPJFonteInf = str(linha[90:92]).strip()
    AreaReservada = str(linha[92:95]).strip()

    return {
        'NomeFonteInf' : NomeFonteInf,
        'CNPJFonteInf' : CNPJFonteInf,
        'FilialFonteInf' : FilialFonteInf,
        'DigCNPJFonteInf' : DigCNPJFonteInf,
        'AreaReservada' : AreaReservada
    }

################################################################################################
#Bloco 020113 - Relacionamento com Fornecedores (Segmento Consolidado)
################################################################################################
def processaBloco020113(linha):
    QtdeFontesInf = str(linha[7:11]).strip()
    QtdeFontesInfHistPagtosValor = str(linha[11:15]).strip()
    QtdeFontesInfEvolucaoCompromisso = str(linha[15:19]).strip()
    QtdeFontesInfRefNegocio = str(linha[19:23]).strip()
    QtdeFontesInfRefNegocioAVista = str(linha[23:27]).strip()
    SegOrigemInfo = str(linha[27:30]).strip()
    QtdeFontesInfHistPagtos = str(linha[30:34]).strip()
    DataSensibilizacao = str(linha[34:42]).strip()

    return {
        'QtdeFontesInf' : QtdeFontesInf,
        'QtdeFontesInfHistPagtosValor' : QtdeFontesInfHistPagtosValor,
        'QtdeFontesInfEvolucaoCompromisso' : QtdeFontesInfEvolucaoCompromisso,
        'QtdeFontesInfRefNegocio' : QtdeFontesInfRefNegocio,
        'QtdeFontesInfRefNegocioAVista' : QtdeFontesInfRefNegocioAVista,
        'SegOrigemInfo' : SegOrigemInfo,
        'QtdeFontesInfHistPagtos' : QtdeFontesInfHistPagtos,
        'DataSensibilizacao' : DataSensibilizacao
    }

################################################################################################
#Bloco 020134 - Relacionamento com Fornecedores – Subgrupo (Segmento Consolidado)
################################################################################################
def processaBloco020134(linha):
    QtdeFontesInf = str(linha[7:11]).strip()
    QtdeFontesInfHistPagtosValor = str(linha[11:15]).strip()
    QtdeFontesInfEvolucaoCompromisso = str(linha[15:19]).strip()
    QtdeFontesInfRefNegocio = str(linha[19:23]).strip()
    QtdeFontesInfRefNegocioAVista = str(linha[23:27]).strip()
    QtdeFontesInfHistPagtos = str(linha[27:31]).strip()
    SegOrigemInfo = str(linha[31:34]).strip()
    SubSegOrigemInfo = str(linha[34:38]).strip()

    return {
        'QtdeFontesInf' : QtdeFontesInf,
        'QtdeFontesInfHistPagtosValor' : QtdeFontesInfHistPagtosValor,
        'QtdeFontesInfEvolucaoCompromisso' : QtdeFontesInfEvolucaoCompromisso,
        'QtdeFontesInfRefNegocio' : QtdeFontesInfRefNegocio,
        'QtdeFontesInfRefNegocioAVista' : QtdeFontesInfRefNegocioAVista,
        'QtdeFontesInfHistPagtos' : QtdeFontesInfHistPagtos,
        'SegOrigemInfo' : SegOrigemInfo,
        'SubSegOrigemInfo' : SubSegOrigemInfo
    }

################################################################################################
#Bloco 020114 - Relacionamento com Fornecedores – por Período - (Segmento Consolidado)
################################################################################################
def processaBloco020114(linha):
    DescPeriodoRelacionamento = str(linha[7:21]).strip()
    QtdeFontesRelacionamento = str(linha[21:25]).strip()
    SegOrigemInfo = str(linha[25:28]).strip()
    SubSegOrigemInfo = str(linha[28:32]).strip()
    DataSensibilizacao = str(linha[32:40]).strip()

    return {
        'DescPeriodoRelacionamento' : DescPeriodoRelacionamento,
        'QtdeFontesRelacionamento' : QtdeFontesRelacionamento,
        'SegOrigemInfo' : SegOrigemInfo,
        'SubSegOrigemInfo' : SubSegOrigemInfo,
        'DataSensibilizacao' : DataSensibilizacao
    }

################################################################################################
#Bloco 020135 - Relacionamento com Fornecedores – Por Período- Subgrupo - (Segmento Consolidado) 
################################################################################################
def processaBloco020135(linha):
    DescPeriodoRelacionamento = str(linha[7:21]).strip()
    QtdeFontesRelacionamento = str(linha[21:25]).strip()
    SegOrigemInfo = str(linha[25:28]).strip()
    SubSegOrigemInfo = str(linha[28:32]).strip()

    return {
        'DescPeriodoRelacionamento' : DescPeriodoRelacionamento,
        'QtdeFontesRelacionamento' : QtdeFontesRelacionamento,
        'SegOrigemInfo' : SegOrigemInfo,
        'SubSegOrigemInfo' : SubSegOrigemInfo
    }

################################################################################################
#Bloco 021115 - Histórico de Pagamentos (valores em R$) - (Segmento Consolidado) 
################################################################################################
def processaBloco021115(linha):
    DescPeriodoHistPagto = str(linha[7:21]).strip()
    AnoPagto = str(linha[21:23]).strip()
    MesPagto = str(linha[23:25]).strip()
    DescMesPagto = str(linha[25:28]).strip()
    CodFaixa = str(linha[28:31]).strip()
    DescFaixa = str(linha[31:51]).strip()
    ValorPagtoDe = str(linha[51:66]).strip()
    ValorPagtoAte = str(linha[66:81]).strip()
    PercPagtoDe = str(linha[81:86]).strip()
    PercPagtoAte = str(linha[86:91]).strip()
    PrazoMedioAtrasoDe = str(linha[91:94]).strip()
    PrazoMedioAtrasoAte = str(linha[94:97]).strip()
    SegOrigemInfo = str(linha[97:100]).strip()
    AreaReservada = str(linha[100:108]).strip()

    return {
        'DescPeriodoHistPagto' : DescPeriodoHistPagto,
        'AnoPagto' : AnoPagto,
        'MesPagto' : MesPagto,
        'DescMesPagto' : DescMesPagto,
        'CodFaixa' : CodFaixa,
        'DescFaixa' : DescFaixa,
        'ValorPagtoDe' : ValorPagtoDe,
        'ValorPagtoAte' : ValorPagtoAte,
        'PercPagtoDe' : PercPagtoDe,
        'PercPagtoAte' : PercPagtoAte,
        'PrazoMedioAtrasoDe' : PrazoMedioAtrasoDe,
        'PrazoMedioAtrasoAte' : PrazoMedioAtrasoAte,
        'SegOrigemInfo' : SegOrigemInfo,
        'AreaReservada' : AreaReservada
    }

################################################################################################
#Bloco 021136 - Histórico de Pagamentos (valores em R$) - Subgrupo (Segmento Consolidado) 
################################################################################################
def processaBloco021136(linha):
    DescPeriodoHistPagto = str(linha[7:21]).strip()
    AnoPagto = str(linha[21:23]).strip()
    MesPagto = str(linha[23:25]).strip()
    DescMesPagto = str(linha[25:28]).strip()
    CodFaixa = str(linha[28:31]).strip()
    DescFaixa = str(linha[31:51]).strip()
    ValorPagtoDe = str(linha[51:66]).strip()
    ValorPagtoAte = str(linha[66:81]).strip()
    PercPagtoDe = str(linha[81:86]).strip()
    PercPagtoAte = str(linha[86:91]).strip()
    PrazoMedioAtrasoDe = str(linha[91:94]).strip()
    PrazoMedioAtrasoAte = str(linha[94:97]).strip()
    SegOrigemInfo = str(linha[97:100]).strip()
    SubOrigemInfo = str(linha[100:104]).strip()
    AreaReservada = str(linha[104:112]).strip()

    return {
        'DescPeriodoHistPagto' : DescPeriodoHistPagto,
        'AnoPagto' : AnoPagto,
        'MesPagto' : MesPagto,
        'DescMesPagto' : DescMesPagto,
        'CodFaixa' : CodFaixa,
        'DescFaixa' : DescFaixa,
        'ValorPagtoDe' : ValorPagtoDe,
        'ValorPagtoAte' : ValorPagtoAte,
        'PercPagtoDe' : PercPagtoDe,
        'PercPagtoAte' : PercPagtoAte,
        'PrazoMedioAtrasoDe' : PrazoMedioAtrasoDe,
        'PrazoMedioAtrasoAte' : PrazoMedioAtrasoAte,
        'SegOrigemInfo' : SegOrigemInfo,
        'SubOrigemInfo' : SubOrigemInfo,
        'AreaReservada' : AreaReservada
    }

################################################################################################
#Bloco 021116 - Evolução de Compromissos com Fornecedores - (Segmento Consolidado)
################################################################################################
def processaBloco021116(linha):
    AnoCompromisso = str(linha[7:9]).strip()
    MesCompromisso = str(linha[9:11]).strip()
    DescMesCompromisso = str(linha[11:14]).strip()
    CodFaixaVencidos = str(linha[14:17]).strip()
    DescFaixaVencidos = str(linha[17:37]).strip()
    ValorCompromissosVencidosDe = str(linha[37:52]).strip()
    ValorCompromissosVencidosAte = str(linha[52:67]).strip()
    CodFaixaAVencer = str(linha[67:70]).strip()
    DescFaixaAVencer = str(linha[70:90]).strip()
    ValorCompromissosAVencerDe = str(linha[90:105]).strip()
    ValorCompromissosAVencerAte = str(linha[105:120]).strip()
    AreaReservada = str(linha[120:173]).strip()
    SegOrigemInfo = str(linha[173:176]).strip()
    AreaReservada2 = str(linha[176:184]).strip()

    return {
        'AnoCompromisso' : AnoCompromisso,
        'MesCompromisso' : MesCompromisso,
        'DescMesCompromisso' : DescMesCompromisso,
        'CodFaixaVencidos' : CodFaixaVencidos,
        'DescFaixaVencidos' : DescFaixaVencidos,
        'ValorCompromissosVencidosDe' : ValorCompromissosVencidosDe,
        'ValorCompromissosVencidosAte' : ValorCompromissosVencidosAte,
        'CodFaixaAVencer' : CodFaixaAVencer,
        'DescFaixaAVencer' : DescFaixaAVencer,
        'ValorCompromissosAVencerDe' : ValorCompromissosAVencerDe,
        'ValorCompromissosAVencerAte' : ValorCompromissosAVencerAte,
        'AreaReservada' : AreaReservada,
        'SegOrigemInfo': SegOrigemInfo,
        'AreaReservada2': AreaReservada2
    }

################################################################################################
#Bloco 021137 - Evolução de Compromissos com Fornecedores- Subgrupo (Segmento Consolidado)
################################################################################################
def processaBloco021137(linha):
    AnoCompromisso = str(linha[7:9]).strip()
    MesCompromisso = str(linha[9:11]).strip()
    DescMesCompromisso = str(linha[11:14]).strip()
    CodFaixaVencidos = str(linha[14:17]).strip()
    DescFaixaVencidos = str(linha[17:37]).strip()
    ValorCompromissosVencidosDe = str(linha[37:52]).strip()
    ValorCompromissosVencidosAte = str(linha[52:67]).strip()
    CodFaixaAVencer = str(linha[67:70]).strip()
    DescFaixaAVencer = str(linha[70:90]).strip()
    ValorCompromissosAVencerDe = str(linha[90:105]).strip()
    ValorCompromissosAVencerAte = str(linha[105:120]).strip()
    SegOrigemInfo = str(linha[120:123]).strip()
    SubSegOrigemInfo = str(linha[123:127]).strip()
    AreaReservada = str(linha[127:135]).strip()

    return {
        'AnoCompromisso' : AnoCompromisso,
        'MesCompromisso' : MesCompromisso,
        'DescMesCompromisso' : DescMesCompromisso,
        'CodFaixaVencidos' : CodFaixaVencidos,
        'DescFaixaVencidos' : DescFaixaVencidos,
        'ValorCompromissosVencidosDe' : ValorCompromissosVencidosDe,
        'ValorCompromissosVencidosAte' : ValorCompromissosVencidosAte,
        'CodFaixaAVencer' : CodFaixaAVencer,
        'DescFaixaAVencer' : DescFaixaAVencer,
        'ValorCompromissosAVencerDe' : ValorCompromissosAVencerDe,
        'ValorCompromissosAVencerAte' : ValorCompromissosAVencerAte,
        'SegOrigemInfo': SegOrigemInfo,
        'SubSegOrigemInfo' : SubSegOrigemInfo,
        'AreaReservada': AreaReservada
    }

################################################################################################
#Bloco 021120 - Evolução de Compromissos Vencidos - (Segmento Consolidado)
################################################################################################
def processaBloco021120(linha):
    DescPeriodoEvolucao = str(linha[7:21]).strip()
    AnoVencidos = str(linha[21:23]).strip()
    MesVencidos = str(linha[23:25]).strip()
    DescMesVencidos = str(linha[25:28]).strip()
    CodFaixaValorVencidos = str(linha[28:31]).strip()
    DescFaixaValorVencidos = str(linha[31:51]).strip()
    ValorVencidosDe = str(linha[51:66]).strip()
    ValorVencidosAte = str(linha[66:81]).strip()
    PercVencidosDe = str(linha[81:86]).strip()
    PercVencidosAte = str(linha[86:91]).strip()
    SegOrigemInfo = str(linha[91:94]).strip()
    AreaReservada = str(linha[94:102]).strip()

    return {
        'DescPeriodoEvolucao' : DescPeriodoEvolucao,
        'AnoVencidos' : AnoVencidos,
        'MesVencidos' : MesVencidos,
        'DescMesVencidos' : DescMesVencidos,
        'CodFaixaValorVencidos' : CodFaixaValorVencidos,
        'DescFaixaValorVencidos' : DescFaixaValorVencidos,
        'ValorVencidosDe' : ValorVencidosDe,
        'ValorVencidosAte' : ValorVencidosAte,
        'PercVencidosDe' : PercVencidosDe,
        'PercVencidosAte' : PercVencidosAte,
        'SegOrigemInfo': SegOrigemInfo,
        'AreaReservada': AreaReservada
    }

################################################################################################
#Bloco 021121 - Evolução de Compromissos a Vencer - (Segmento Consolidado) 
################################################################################################
def processaBloco021121(linha):
    DescPeriodoEvolucao = str(linha[7:21]).strip()
    AnoAVencer = str(linha[21:23]).strip()
    MesAVencer = str(linha[23:25]).strip()
    DescMesAVencer = str(linha[25:28]).strip()
    CodFaixaValorAVencer = str(linha[28:31]).strip()
    DescFaixaValorAVencer = str(linha[31:51]).strip()
    ValorAVencerDe = str(linha[51:66]).strip()
    ValorAVencerAte = str(linha[66:81]).strip()
    PercAVencerDe = str(linha[81:86]).strip()
    PercAVencerAte = str(linha[86:91]).strip()
    SegOrigemInfo = str(linha[91:94]).strip()
    AreaReservada = str(linha[94:102]).strip()

    return {
        'DescPeriodoEvolucao' : DescPeriodoEvolucao,
        'AnoAVencer' : AnoAVencer,
        'MesAVencer' : MesAVencer,
        'DescMesAVencer' : DescMesAVencer,
        'CodFaixaValorAVencer' : CodFaixaValorAVencer,
        'DescFaixaValorAVencer' : DescFaixaValorAVencer,
        'ValorAVencerDe' : ValorAVencerDe,
        'ValorAVencerAte' : ValorAVencerAte,
        'PercAVencerDe' : PercAVencerDe,
        'PercAVencerAte' : PercAVencerAte,
        'SegOrigemInfo': SegOrigemInfo,
        'AreaReservada': AreaReservada
    }

################################################################################################
#Bloco 021122 - Referenciais de Negócios à Vista 
################################################################################################
def processaBloco021122(linha):
    DescNegocio = str(linha[7:21]).strip()
    DataAVista = str(linha[21:27]).strip()
    CodFaixaValorAVista = str(linha[27:30]).strip()
    DescFaixaValorAVista = str(linha[30:50]).strip()
    ValorAVistaDe = str(linha[50:65]).strip()
    ValorAVistaAte = str(linha[65:80]).strip()
    CodFaixaMediaAVista = str(linha[80:83]).strip()
    DescFaixaMediaVista = str(linha[83:103]).strip()
    ValorFaixaMediaAVistaDe = str(linha[103:118]).strip()
    ValorFaixaMediaAVistaAte = str(linha[118:133]).strip()
    SegOrigemInfo = str(linha[133:136]).strip()
    AreaReservada = str(linha[136:144]).strip()

    return {
        'DescNegocio' : DescNegocio,
        'DataAVista' : DataAVista,
        'CodFaixaValorAVista' : CodFaixaValorAVista,
        'DescFaixaValorAVista' : DescFaixaValorAVista,
        'ValorAVistaDe' : ValorAVistaDe,
        'ValorAVistaAte' : ValorAVistaAte,
        'CodFaixaMediaAVista' : CodFaixaMediaAVista,
        'DescFaixaMediaVista' : DescFaixaMediaVista,
        'ValorFaixaMediaAVistaDe' : ValorFaixaMediaAVistaDe,
        'ValorFaixaMediaAVistaAte' : ValorFaixaMediaAVistaAte,
        'SegOrigemInfo' : SegOrigemInfo,
        'AreaReservada' : AreaReservada
    }

################################################################################################
#Bloco 021117 - Referenciais de Negócios - (Segmento Consolidado) 
################################################################################################
def processaBloco021117(linha):
    DescNegocio = str(linha[7:21]).strip()
    DataPotencial = str(linha[21:27]).strip()
    CodFaixaValorPotencial = str(linha[27:30]).strip()
    DescFaixaValorPotencial = str(linha[30:50]).strip()
    ValorPotencialDe = str(linha[50:65]).strip()
    ValorPotencialAte = str(linha[65:80]).strip()
    CodFaixaMediaPotencial = str(linha[80:83]).strip()
    DescFaixaMediaPotencial = str(linha[83:103]).strip()
    ValorMediaPotencialDe = str(linha[103:118]).strip()
    ValorMediaPotencialAte = str(linha[118:133]).strip()
    SegOrigemInfo = str(linha[133:136]).strip()
    AreaReservada = str(linha[136:144]).strip()

    return {
        'DescNegocio' : DescNegocio,
        'DataPotencial' : DataPotencial,
        'CodFaixaValorPotencial' : CodFaixaValorPotencial,
        'DescFaixaValorPotencial' : DescFaixaValorPotencial,
        'ValorPotencialDe' : ValorPotencialDe,
        'ValorPotencialAte' : ValorPotencialAte,
        'CodFaixaMediaPotencial' : CodFaixaMediaPotencial,
        'DescFaixaMediaPotencial' : DescFaixaMediaPotencial,
        'ValorMediaPotencialDe' : ValorMediaPotencialDe,
        'ValorMediaPotencialAte' : ValorMediaPotencialAte,
        'SegOrigemInfo' : SegOrigemInfo,
        'AreaReservada' : AreaReservada
    }

################################################################################################
#Bloco 021138 - Referenciais de Negócios – Subgrupo (Segmento Consolidado)
################################################################################################
def processaBloco021138(linha):
    DescNegocio = str(linha[7:21]).strip()
    DataPotencial = str(linha[21:29]).strip()
    CodFaixaValorPotencial = str(linha[29:32]).strip()
    DescFaixaValorPotencial = str(linha[32:52]).strip()
    ValorPotencialDe = str(linha[52:67]).strip()
    ValorPotencialAte = str(linha[67:82]).strip()
    CodFaixaMediaPotencial = str(linha[82:85]).strip()
    DescFaixaMediaPotencial = str(linha[85:105]).strip()
    MediaPotencialDe = str(linha[105:120]).strip()
    MediaPotencialAte = str(linha[120:135]).strip()
    SegOrigemInfo = str(linha[135:138]).strip()
    SubSegOrigemInfo = str(linha[138:142]).strip()
    AreaReservada = str(linha[142:150]).strip()

    return {
        'DescNegocio' : DescNegocio,
        'DataPotencial' : DataPotencial,
        'CodFaixaValorPotencial' : CodFaixaValorPotencial,
        'DescFaixaValorPotencial' : DescFaixaValorPotencial,
        'ValorPotencialDe' : ValorPotencialDe,
        'ValorPotencialAte' : ValorPotencialAte,
        'CodFaixaMediaPotencial' : CodFaixaMediaPotencial,
        'DescFaixaMediaPotencial' : DescFaixaMediaPotencial,
        'MediaPotencialDe' : MediaPotencialDe,
        'MediaPotencialAte' : MediaPotencialAte,
        'SegOrigemInfo' : SegOrigemInfo,
        'SubSegOrigemInfo' : SubSegOrigemInfo,
        'AreaReservada' : AreaReservada
    }

################################################################################################
#Bloco 021125 - Histórico de Pagamentos visão cedente (valores em R$)
################################################################################################
def processaBloco021125(linha):
    DescPeriodoHistPagto = str(linha[7:21]).strip()
    AnoPagamento = str(linha[21:23]).strip()
    MesPagamento = str(linha[23:25]).strip()
    DescMesPagto = str(linha[25:28]).strip()
    CodFaixa = str(linha[28:31]).strip()
    DescFaixa = str(linha[31:51]).strip()
    ValorPagtoDe = str(linha[51:66]).strip()
    ValorPagtoAte = str(linha[66:81]).strip()
    PercentualPagtoDe = str(linha[81:86]).strip()
    PercentualPagtoAte = str(linha[86:91]).strip()
    PrazoMedioAtrasoDe = str(linha[91:94]).strip()
    PrazoMedioAtrasoAte = str(linha[94:97]).strip()
    AreaReservada = str(linha[97:108]).strip()

    return {
        'DescPeriodoHistPagto' : DescPeriodoHistPagto,
        'AnoPagamento' : AnoPagamento,
        'MesPagamento' : MesPagamento,
        'DescMesPagto' : DescMesPagto,
        'CodFaixa' : CodFaixa,
        'DescFaixa' : DescFaixa,
        'ValorPagtoDe' : ValorPagtoDe,
        'ValorPagtoAte' : ValorPagtoAte,
        'PercentualPagtoDe' : PercentualPagtoDe,
        'PercentualPagtoAte' : PercentualPagtoAte,
        'PrazoMedioAtrasoDe' : PrazoMedioAtrasoDe,
        'PrazoMedioAtrasoAte' : PrazoMedioAtrasoAte,
        'AreaReservada' : AreaReservada
    }

################################################################################################
#Bloco 021126 - Evolução de Compromissos com Fornecedores visão cedente
################################################################################################
def processaBloco021126(linha):
    AnoCompromisso = str(linha[21:23]).strip()
    MesCompromisso = str(linha[23:25]).strip()
    DescMesCompromisso = str(linha[25:28]).strip()
    CodFaixaVencidos = str(linha[28:31]).strip()
    DescFaixaVencidos = str(linha[31:51]).strip()
    ValorCompromissoVencidosDe = str(linha[51:66]).strip()
    ValorCompromissoVencidosAte = str(linha[66:81]).strip()
    CodFaixaAVencer = str(linha[81:86]).strip()
    DescFaixaAVencer = str(linha[86:91]).strip()
    ValorCompromissoAVencersDe = str(linha[51:66]).strip()
    ValorCompromissoAVencerAte = str(linha[66:81]).strip()
    AreaReservada = str(linha[97:108]).strip()

    return {
        'AnoCompromisso' : AnoCompromisso,
        'MesCompromisso' : MesCompromisso,
        'DescMesCompromisso' : DescMesCompromisso,
        'CodFaixaVencidos' : CodFaixaVencidos,
        'DescFaixaVencidos' : DescFaixaVencidos,
        'ValorCompromissoVencidosDe' : ValorCompromissoVencidosDe,
        'ValorCompromissoVencidosAte' : ValorCompromissoVencidosAte,
        'CodFaixaAVencer' : CodFaixaAVencer,
        'DescFaixaAVencer' : DescFaixaAVencer,
        'ValorCompromissoAVencersDe' : ValorCompromissoAVencersDe,
        'ValorCompromissoAVencerAte' : ValorCompromissoAVencerAte,
        'AreaReservada' : AreaReservada
    }

################################################################################################
#Bloco 021127 - Referenciais de Negócios visão cedente 
################################################################################################
def processaBloco021127(linha):
    DescNegocio = str(linha[7:21]).strip()
    DataPotencial = str(linha[21:27]).strip()
    CodFaixaValorPotencial = str(linha[27:30]).strip()
    DescFaixaValorPotencial = str(linha[30:50]).strip()
    ValorPotencialDe = str(linha[50:65]).strip()
    ValorPotencialAte = str(linha[65:80]).strip()
    CodFaixaMediaPotencial = str(linha[80:83]).strip()
    DescFaixaMediaPotencial = str(linha[83:103]).strip()
    MediaPotencialDe = str(linha[103:118]).strip()
    MediaPotencialAte = str(linha[118:133]).strip()
    AreaReservada = str(linha[133:144]).strip()

    return {
        'DescNegocio' : DescNegocio,
        'DataPotencial' : DataPotencial,
        'CodFaixaValorPotencial' : CodFaixaValorPotencial,
        'DescFaixaValorPotencial' : DescFaixaValorPotencial,
        'ValorPotencialDe' : ValorPotencialDe,
        'ValorPotencialAte' : ValorPotencialAte,
        'CodFaixaMediaPotencial' : CodFaixaMediaPotencial,
        'DescFaixaMediaPotencial' : DescFaixaMediaPotencial,
        'MediaPotencialDe' : MediaPotencialDe,
        'MediaPotencialAte' : MediaPotencialAte,
        'AreaReservada' : AreaReservada
    }

##########################################################################################################
#Bloco 021139 - Histórico de Pagamentos (valores em R$) - Subgrupo (Segmento Consolidado) visão cedente
##########################################################################################################
def processaBloco021139(linha):
    DescPeriodoHistPagto = str(linha[7:21]).strip()
    AnoPagto = str(linha[21:23]).strip()
    MesPagto = str(linha[23:25]).strip()
    DescMesPagto = str(linha[25:28]).strip()
    CodFaixaValorPagto = str(linha[28:31]).strip()
    DescFaixaValorPagto = str(linha[31:51]).strip()
    ValorPagtoDe = str(linha[51:66]).strip()
    ValorPagtoAte = str(linha[66:81]).strip()
    PercPagtoDe = str(linha[81:86]).strip()
    PercPagtoAte = str(linha[86:91]).strip()
    PrazoMedioAtrasoDe = str(linha[91:94]).strip()
    PrazoMedioAtrasoAte = str(linha[94:97]).strip()
    SegOrigemInfo = str(linha[97:100]).strip()
    SubOrigemInfo = str(linha[100:104]).strip()
    AreaReservada = str(linha[104:112]).strip()

    return {
        'DescPeriodoHistPagto' : DescPeriodoHistPagto,
        'AnoPagto' : AnoPagto,
        'MesPagto' : MesPagto,
        'DescMesPagto' : DescMesPagto,
        'CodFaixaValorPagto' : CodFaixaValorPagto,
        'DescFaixaValorPagto' : DescFaixaValorPagto,
        'ValorPagtoDe' : ValorPagtoDe,
        'ValorPagtoAte' : ValorPagtoAte,
        'PercPagtoDe' : PercPagtoDe,
        'PercPagtoAte' : PercPagtoAte,
        'PrazoMedioAtrasoDe' : PrazoMedioAtrasoDe,
        'PrazoMedioAtrasoAte' : PrazoMedioAtrasoAte,
        'SegOrigemInfo' : SegOrigemInfo,
        'SubOrigemInfo' : SubOrigemInfo,
        'AreaReservada' : AreaReservada
    }

##########################################################################################################
#Bloco 021140 - Evolução de Compromissos com Fornecedores- Subgrupo (Segmento Consolidado) visão cedente
##########################################################################################################
def processaBloco021140(linha):
    AnoCompromisso = str(linha[7:9]).strip()
    MesCompromisso = str(linha[9:11]).strip()
    DescMesCompromisso = str(linha[11:14]).strip()
    CodFaixaVencidos = str(linha[14:17]).strip()
    DescFaixaVencidos = str(linha[17:37]).strip()
    ValorCompromissosVencidosDe = str(linha[37:52]).strip()
    ValorCompromissosVencidosAte = str(linha[52:67]).strip()
    CodFaixaAVencer = str(linha[67:70]).strip()
    DescFaixaAVencer = str(linha[70:90]).strip()
    ValorCompromissosAVencerDe = str(linha[90:105]).strip()
    ValorCompromissosAVencerAte = str(linha[105:120]).strip()
    SegOrigemInfo = str(linha[120:123]).strip()
    SubSegOrigemInfo = str(linha[123:127]).strip()
    AreaReservada = str(linha[127:135]).strip()

    return {
        'AnoCompromisso' : AnoCompromisso,
        'MesCompromisso' : MesCompromisso,
        'DescMesCompromisso' : DescMesCompromisso,
        'CodFaixaVencidos' : CodFaixaVencidos,
        'DescFaixaVencidos' : DescFaixaVencidos,
        'ValorCompromissosVencidosDe' : ValorCompromissosVencidosDe,
        'ValorCompromissosVencidosAte' : ValorCompromissosVencidosAte,
        'CodFaixaAVencer' : CodFaixaAVencer,
        'DescFaixaAVencer' : DescFaixaAVencer,
        'ValorCompromissosAVencerDe' : ValorCompromissosAVencerDe,
        'ValorCompromissosAVencerAte' : ValorCompromissosAVencerAte,
        'SegOrigemInfo': SegOrigemInfo,
        'SubSegOrigemInfo' : SubSegOrigemInfo,
        'AreaReservada': AreaReservada
    }

################################################################################################
#Bloco 021141 - Referenciais de Negócios – Subgrupo (Segmento Consolidado) visão cedente 
################################################################################################
def processaBloco021141(linha):
    DescNegocio = str(linha[7:21]).strip()
    DataPotencial = str(linha[21:29]).strip()
    CodFaixaValorPotencial = str(linha[29:32]).strip()
    DescFaixaValorPotencial = str(linha[32:52]).strip()
    ValorPotencialDe = str(linha[52:67]).strip()
    ValorPotencialAte = str(linha[67:82]).strip()
    CodFaixaMediaPotencial = str(linha[82:85]).strip()
    DescFaixaMediaPotencial = str(linha[85:105]).strip()
    MediaPotencialDe = str(linha[105:120]).strip()
    MediaPotencialAte = str(linha[120:135]).strip()
    SegOrigemInfo = str(linha[135:138]).strip()
    SubSegOrigemInfo = str(linha[138:142]).strip()
    AreaReservada = str(linha[142:150]).strip()

    return {
        'DescNegocio' : DescNegocio,
        'DataPotencial' : DataPotencial,
        'CodFaixaValorPotencial' : CodFaixaValorPotencial,
        'DescFaixaValorPotencial' : DescFaixaValorPotencial,
        'ValorPotencialDe' : ValorPotencialDe,
        'ValorPotencialAte' : ValorPotencialAte,
        'CodFaixaMediaPotencial' : CodFaixaMediaPotencial,
        'DescFaixaMediaPotencial' : DescFaixaMediaPotencial,
        'MediaPotencialDe' : MediaPotencialDe,
        'MediaPotencialAte' : MediaPotencialAte,
        'SegOrigemInfo' : SegOrigemInfo,
        'SubSegOrigemInfo' : SubSegOrigemInfo,
        'AreaReservada' : AreaReservada
    }

################################################################################################
#Bloco 020133 - Módulo de Verificação do Título
################################################################################################
def processaBloco020133(linha):
    CodRetornoModVerifTitulo = str(linha[7:9]).strip()
    DesRetornoModVerifTitulo = str(linha[7:9]).strip()
    MsgModVerifTitulo = buscaRetornoModVerifTitulo(str(linha[9:89]).strip())

    return {
        'CodRetornoModVerifTitulo' : CodRetornoModVerifTitulo,
        'DesRetornoModVerifTitulo' : DesRetornoModVerifTitulo,
        'MsgModVerifTitulo' : MsgModVerifTitulo
    }

################################################################################################
#Bloco 023405 - Total do Histórico de Pagamentos (Valores em R$) - TOTAIS DE MERCADO
################################################################################################
def processaBloco023405(linha):
    IdentColuna = str(linha[7:21]).strip()
    CodFaixaValorPagamento = str(linha[21:24]).strip()
    DescFaixaValorPagamento = str(linha[24:44]).strip()
    ValorPagamentoDe = str(linha[44:59]).strip()
    ValorPagamentoAte = str(linha[59:74]).strip()
    CodFaixaMedia = str(linha[74:77]).strip()
    DescFaixaMedia = str(linha[77:97]).strip()
    MediaHistoricoDe = str(linha[97:112]).strip()
    MediaHistoricoAte = str(linha[112:127]).strip()
    PercFaixaDe = str(linha[127:132]).strip()
    PercFaixaAte = str(linha[132:137]).strip()
    AreaReservada = str(linha[137:143]).strip()
    SegOrigemInf = str(linha[143:146]).strip()
    SubSegOrigemInf = str(linha[146:150]).strip()
    
    CodTipoPrazo = str(linha[150:151]).strip()
    DescTipoPrazo = buscaTipoPrazo(str(linha[150:151]).strip())
    
    return {
        'IdentColuna' : IdentColuna,
        'CodFaixaValorPagamento' : CodFaixaValorPagamento,
        'DescFaixaValorPagamento' : DescFaixaValorPagamento,
        'ValorPagamentoDe' : ValorPagamentoDe,
        'ValorPagamentoAte' : ValorPagamentoAte,
        'CodFaixaMedia' : CodFaixaMedia,
        'DescFaixaMedia' : DescFaixaMedia,
        'MediaHistoricoDe' : MediaHistoricoDe,
        'MediaHistoricoAte' : MediaHistoricoAte,
        'PercFaixaDe' : PercFaixaDe,
        'PercFaixaAte' : PercFaixaAte,
        'AreaReservada' : AreaReservada,
        'SegOrigemInf' : SegOrigemInf,
        'SubSegOrigemInf' : SubSegOrigemInf,
        'CodTipoPrazo' : CodTipoPrazo,
        'DescTipoPrazo' : DescTipoPrazo
    }

################################################################################################
#Bloco 023409 - Total do Histórico de Pagamentos (Valores em R$) - REFERENCIAIS DE NEGOCIOS VISAO INDIVIDUAL
################################################################################################
def processaBloco023409(linha):
    IdentColuna = str(linha[7:21]).strip()
    CodFaixaValorPagamento = str(linha[21:24]).strip()
    DescFaixaValorPagamento = str(linha[24:44]).strip()
    ValorPagamentoDe = str(linha[44:59]).strip()
    ValorPagamentoAte = str(linha[59:74]).strip()
    CodFaixaMedia = str(linha[74:77]).strip()
    DescFaixaMedia = str(linha[77:97]).strip()
    MediaHistoricoDe = str(linha[97:112]).strip()
    MediaHistoricoAte = str(linha[112:127]).strip()
    PercFaixaDe = str(linha[127:132]).strip()
    PercFaixaAte = str(linha[132:137]).strip()
    AreaReservada = str(linha[137:143]).strip()
    SegOrigemInf = str(linha[143:146]).strip()
    SubSegOrigemInf = str(linha[146:150]).strip()
    
    CodTipoPrazo = str(linha[150:151]).strip()
    DescTipoPrazo = buscaTipoPrazo(str(linha[150:151]).strip())
    
    return {
        'IdentColuna' : IdentColuna,
        'CodFaixaValorPagamento' : CodFaixaValorPagamento,
        'DescFaixaValorPagamento' : DescFaixaValorPagamento,
        'ValorPagamentoDe' : ValorPagamentoDe,
        'ValorPagamentoAte' : ValorPagamentoAte,
        'CodFaixaMedia' : CodFaixaMedia,
        'DescFaixaMedia' : DescFaixaMedia,
        'MediaHistoricoDe' : MediaHistoricoDe,
        'MediaHistoricoAte' : MediaHistoricoAte,
        'PercFaixaDe' : PercFaixaDe,
        'PercFaixaAte' : PercFaixaAte,
        'AreaReservada' : AreaReservada,
        'SegOrigemInf' : SegOrigemInf,
        'SubSegOrigemInf' : SubSegOrigemInf,
        'CodTipoPrazo' : CodTipoPrazo,
        'DescTipoPrazo' : DescTipoPrazo
    }

################################################################################################
#Bloco 023410 - Total do Histórico de Pagamentos (Valores em R$) - EVOLUCAO DE COMPROMISSOS VISAO INDIVIDUAL
################################################################################################
def processaBloco023410(linha):
    IdentColuna = str(linha[7:21]).strip()
    CodFaixaValorPagamento = str(linha[21:24]).strip()
    DescFaixaValorPagamento = str(linha[24:44]).strip()
    ValorPagamentoDe = str(linha[44:59]).strip()
    ValorPagamentoAte = str(linha[59:74]).strip()
    CodFaixaMedia = str(linha[74:77]).strip()
    DescFaixaMedia = str(linha[77:97]).strip()
    MediaHistoricoDe = str(linha[97:112]).strip()
    MediaHistoricoAte = str(linha[112:127]).strip()
    PercFaixaDe = str(linha[127:132]).strip()
    PercFaixaAte = str(linha[132:137]).strip()
    AreaReservada = str(linha[137:143]).strip()
    SegOrigemInf = str(linha[143:146]).strip()
    SubSegOrigemInf = str(linha[146:150]).strip()
    
    CodTipoPrazo = str(linha[150:151]).strip()
    DescTipoPrazo = buscaTipoPrazo(str(linha[150:151]).strip())
    
    return {
        'IdentColuna' : IdentColuna,
        'CodFaixaValorPagamento' : CodFaixaValorPagamento,
        'DescFaixaValorPagamento' : DescFaixaValorPagamento,
        'ValorPagamentoDe' : ValorPagamentoDe,
        'ValorPagamentoAte' : ValorPagamentoAte,
        'CodFaixaMedia' : CodFaixaMedia,
        'DescFaixaMedia' : DescFaixaMedia,
        'MediaHistoricoDe' : MediaHistoricoDe,
        'MediaHistoricoAte' : MediaHistoricoAte,
        'PercFaixaDe' : PercFaixaDe,
        'PercFaixaAte' : PercFaixaAte,
        'AreaReservada' : AreaReservada,
        'SegOrigemInf' : SegOrigemInf,
        'SubSegOrigemInf' : SubSegOrigemInf,
        'CodTipoPrazo' : CodTipoPrazo,
        'DescTipoPrazo' : DescTipoPrazo
    }

################################################################################################
#Bloco 023415 - Total do Histórico de Pagamentos (Valores em R$) - TOTAIS DE SEGMENTO
################################################################################################
def processaBloco023415(linha):
    IdentColuna = str(linha[7:21]).strip()
    CodFaixaValorPagamento = str(linha[21:24]).strip()
    DescFaixaValorPagamento = str(linha[24:44]).strip()
    ValorPagamentoDe = str(linha[44:59]).strip()
    ValorPagamentoAte = str(linha[59:74]).strip()
    CodFaixaMedia = str(linha[74:77]).strip()
    DescFaixaMedia = str(linha[77:97]).strip()
    MediaHistoricoDe = str(linha[97:112]).strip()
    MediaHistoricoAte = str(linha[112:127]).strip()
    PercFaixaDe = str(linha[127:132]).strip()
    PercFaixaAte = str(linha[132:137]).strip()
    AreaReservada = str(linha[137:143]).strip()
    SegOrigemInf = str(linha[143:146]).strip()
    SubSegOrigemInf = str(linha[146:150]).strip()
    
    CodTipoPrazo = str(linha[150:151]).strip()
    DescTipoPrazo = buscaTipoPrazo(str(linha[150:151]).strip())
    
    return {
        'IdentColuna' : IdentColuna,
        'CodFaixaValorPagamento' : CodFaixaValorPagamento,
        'DescFaixaValorPagamento' : DescFaixaValorPagamento,
        'ValorPagamentoDe' : ValorPagamentoDe,
        'ValorPagamentoAte' : ValorPagamentoAte,
        'CodFaixaMedia' : CodFaixaMedia,
        'DescFaixaMedia' : DescFaixaMedia,
        'MediaHistoricoDe' : MediaHistoricoDe,
        'MediaHistoricoAte' : MediaHistoricoAte,
        'PercFaixaDe' : PercFaixaDe,
        'PercFaixaAte' : PercFaixaAte,
        'AreaReservada' : AreaReservada,
        'SegOrigemInf' : SegOrigemInf,
        'SubSegOrigemInf' : SubSegOrigemInf,
        'CodTipoPrazo' : CodTipoPrazo,
        'DescTipoPrazo' : DescTipoPrazo
    }

################################################################################################
#Bloco 023418 - Total do Histórico de Pagamentos (Valores em R$) - TOTAIS SEGMENTO VISAO INDIVIDUAL
################################################################################################
def processaBloco023418(linha):
    IdentColuna = str(linha[7:21]).strip()
    CodFaixaValorPagamento = str(linha[21:24]).strip()
    DescFaixaValorPagamento = str(linha[24:44]).strip()
    ValorPagamentoDe = str(linha[44:59]).strip()
    ValorPagamentoAte = str(linha[59:74]).strip()
    CodFaixaMedia = str(linha[74:77]).strip()
    DescFaixaMedia = str(linha[77:97]).strip()
    MediaHistoricoDe = str(linha[97:112]).strip()
    MediaHistoricoAte = str(linha[112:127]).strip()
    PercFaixaDe = str(linha[127:132]).strip()
    PercFaixaAte = str(linha[132:137]).strip()
    AreaReservada = str(linha[137:143]).strip()
    SegOrigemInf = str(linha[143:146]).strip()
    SubSegOrigemInf = str(linha[146:150]).strip()
    
    CodTipoPrazo = str(linha[150:151]).strip()
    DescTipoPrazo = buscaTipoPrazo(str(linha[150:151]).strip())
    
    return {
        'IdentColuna' : IdentColuna,
        'CodFaixaValorPagamento' : CodFaixaValorPagamento,
        'DescFaixaValorPagamento' : DescFaixaValorPagamento,
        'ValorPagamentoDe' : ValorPagamentoDe,
        'ValorPagamentoAte' : ValorPagamentoAte,
        'CodFaixaMedia' : CodFaixaMedia,
        'DescFaixaMedia' : DescFaixaMedia,
        'MediaHistoricoDe' : MediaHistoricoDe,
        'MediaHistoricoAte' : MediaHistoricoAte,
        'PercFaixaDe' : PercFaixaDe,
        'PercFaixaAte' : PercFaixaAte,
        'AreaReservada' : AreaReservada,
        'SegOrigemInf' : SegOrigemInf,
        'SubSegOrigemInf' : SubSegOrigemInf,
        'CodTipoPrazo' : CodTipoPrazo,
        'DescTipoPrazo' : DescTipoPrazo
    }

################################################################################################
#Bloco 023425 - Total do Histórico de Pagamentos (Valores em R$) - TOTAIS DE CEDENTE
################################################################################################
def processaBloco023425(linha):
    IdentColuna = str(linha[7:21]).strip()
    CodFaixaValorPagamento = str(linha[21:24]).strip()
    DescFaixaValorPagamento = str(linha[24:44]).strip()
    ValorPagamentoDe = str(linha[44:59]).strip()
    ValorPagamentoAte = str(linha[59:74]).strip()
    CodFaixaMedia = str(linha[74:77]).strip()
    DescFaixaMedia = str(linha[77:97]).strip()
    MediaHistoricoDe = str(linha[97:112]).strip()
    MediaHistoricoAte = str(linha[112:127]).strip()
    PercFaixaDe = str(linha[127:132]).strip()
    PercFaixaAte = str(linha[132:137]).strip()
    AreaReservada = str(linha[137:143]).strip()
    SegOrigemInf = str(linha[143:146]).strip()
    SubSegOrigemInf = str(linha[146:150]).strip()
    
    CodTipoPrazo = str(linha[150:151]).strip()
    DescTipoPrazo = buscaTipoPrazo(str(linha[150:151]).strip())
    
    return {
        'IdentColuna' : IdentColuna,
        'CodFaixaValorPagamento' : CodFaixaValorPagamento,
        'DescFaixaValorPagamento' : DescFaixaValorPagamento,
        'ValorPagamentoDe' : ValorPagamentoDe,
        'ValorPagamentoAte' : ValorPagamentoAte,
        'CodFaixaMedia' : CodFaixaMedia,
        'DescFaixaMedia' : DescFaixaMedia,
        'MediaHistoricoDe' : MediaHistoricoDe,
        'MediaHistoricoAte' : MediaHistoricoAte,
        'PercFaixaDe' : PercFaixaDe,
        'PercFaixaAte' : PercFaixaAte,
        'AreaReservada' : AreaReservada,
        'SegOrigemInf' : SegOrigemInf,
        'SubSegOrigemInf' : SubSegOrigemInf,
        'CodTipoPrazo' : CodTipoPrazo,
        'DescTipoPrazo' : DescTipoPrazo
    }

################################################################################################
#Bloco 023436 - Total do Histórico de Pagamentos (Valores em R$) - TOTAIS DE SUB-GRUPO
################################################################################################
def processaBloco023436(linha):
    IdentColuna = str(linha[7:21]).strip()
    CodFaixaValorPagamento = str(linha[21:24]).strip()
    DescFaixaValorPagamento = str(linha[24:44]).strip()
    ValorPagamentoDe = str(linha[44:59]).strip()
    ValorPagamentoAte = str(linha[59:74]).strip()
    CodFaixaMedia = str(linha[74:77]).strip()
    DescFaixaMedia = str(linha[77:97]).strip()
    MediaHistoricoDe = str(linha[97:112]).strip()
    MediaHistoricoAte = str(linha[112:127]).strip()
    PercFaixaDe = str(linha[127:132]).strip()
    PercFaixaAte = str(linha[132:137]).strip()
    AreaReservada = str(linha[137:143]).strip()
    SegOrigemInf = str(linha[143:146]).strip()
    SubSegOrigemInf = str(linha[146:150]).strip()
    
    CodTipoPrazo = str(linha[150:151]).strip()
    DescTipoPrazo = buscaTipoPrazo(str(linha[150:151]).strip())
    
    return {
        'IdentColuna' : IdentColuna,
        'CodFaixaValorPagamento' : CodFaixaValorPagamento,
        'DescFaixaValorPagamento' : DescFaixaValorPagamento,
        'ValorPagamentoDe' : ValorPagamentoDe,
        'ValorPagamentoAte' : ValorPagamentoAte,
        'CodFaixaMedia' : CodFaixaMedia,
        'DescFaixaMedia' : DescFaixaMedia,
        'MediaHistoricoDe' : MediaHistoricoDe,
        'MediaHistoricoAte' : MediaHistoricoAte,
        'PercFaixaDe' : PercFaixaDe,
        'PercFaixaAte' : PercFaixaAte,
        'AreaReservada' : AreaReservada,
        'SegOrigemInf' : SegOrigemInf,
        'SubSegOrigemInf' : SubSegOrigemInf,
        'CodTipoPrazo' : CodTipoPrazo,
        'DescTipoPrazo' : DescTipoPrazo
    }

################################################################################################
#Bloco 023439 - Total do Histórico de Pagamentos (Valores em R$) - TOTAIS DE SUB-GRUPO NA MODALIDADE CEDENTE
################################################################################################
def processaBloco023439(linha):
    IdentColuna = str(linha[7:21]).strip()
    CodFaixaValorPagamento = str(linha[21:24]).strip()
    DescFaixaValorPagamento = str(linha[24:44]).strip()
    ValorPagamentoDe = str(linha[44:59]).strip()
    ValorPagamentoAte = str(linha[59:74]).strip()
    CodFaixaMedia = str(linha[74:77]).strip()
    DescFaixaMedia = str(linha[77:97]).strip()
    MediaHistoricoDe = str(linha[97:112]).strip()
    MediaHistoricoAte = str(linha[112:127]).strip()
    PercFaixaDe = str(linha[127:132]).strip()
    PercFaixaAte = str(linha[132:137]).strip()
    AreaReservada = str(linha[137:143]).strip()
    SegOrigemInf = str(linha[143:146]).strip()
    SubSegOrigemInf = str(linha[146:150]).strip()
    
    CodTipoPrazo = str(linha[150:151]).strip()
    DescTipoPrazo = buscaTipoPrazo(str(linha[150:151]).strip())
    
    return {
        'IdentColuna' : IdentColuna,
        'CodFaixaValorPagamento' : CodFaixaValorPagamento,
        'DescFaixaValorPagamento' : DescFaixaValorPagamento,
        'ValorPagamentoDe' : ValorPagamentoDe,
        'ValorPagamentoAte' : ValorPagamentoAte,
        'CodFaixaMedia' : CodFaixaMedia,
        'DescFaixaMedia' : DescFaixaMedia,
        'MediaHistoricoDe' : MediaHistoricoDe,
        'MediaHistoricoAte' : MediaHistoricoAte,
        'PercFaixaDe' : PercFaixaDe,
        'PercFaixaAte' : PercFaixaAte,
        'AreaReservada' : AreaReservada,
        'SegOrigemInf' : SegOrigemInf,
        'SubSegOrigemInf' : SubSegOrigemInf,
        'CodTipoPrazo' : CodTipoPrazo,
        'DescTipoPrazo' : DescTipoPrazo
    }
