#DadosComerciaisConsolidados_02.py
from datetime import datetime
from APICredMind.views.SERASA.mappingsSERASA import *

################################################################################################
#Bloco 020100 - Principais Fornecedores – Data da Última Atualização
################################################################################################
def processaBloco020100(linha):
    DataUltimaAtualizacaoBloco = str(linha[7:15]).strip()
    SegmentoOrigemInformacao = str(linha[15:18]).strip()

    return {
        'DataUltimaAtualizacaoBloco' : DataUltimaAtualizacaoBloco,
        'SegmentoOrigemInformacao' : SegmentoOrigemInformacao
    }

################################################################################################
#Bloco 020101 - Principais Fornecedores
################################################################################################
def processaBloco020101(linha):
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
#Bloco 020102 - Relacionamento com Fornecedores 
################################################################################################
def processaBloco020102(linha):
    QtdeFontesInf = str(linha[7:11]).strip()
    QtdeFontesInfHistPagtosValor = str(linha[11:15]).strip()
    QtdeFontesInfEvolucaoCompromisso = str(linha[15:19]).strip()
    QtdeFontesInfRefNegocio = str(linha[19:23]).strip()
    QtdeFontesInfRefNegocioAVista = str(linha[23:27]).strip()
    AreaReservada = str(linha[27:30]).strip()
    QtdeFontesInfHistPagtos = str(linha[30:34]).strip()
    AreaReservada2 = str(linha[34:42]).strip()

    return {
        'QtdeFontesInf' : QtdeFontesInf,
        'QtdeFontesInfHistPagtosValor' : QtdeFontesInfHistPagtosValor,
        'QtdeFontesInfEvolucaoCompromisso' : QtdeFontesInfEvolucaoCompromisso,
        'QtdeFontesInfRefNegocio' : QtdeFontesInfRefNegocio,
        'QtdeFontesInfRefNegocioAVista' : QtdeFontesInfRefNegocioAVista,
        'AreaReservada' : AreaReservada,
        'QtdeFontesInfHistPagtos' : QtdeFontesInfHistPagtos,
        'AreaReservada2' : AreaReservada2
    }

################################################################################################
#Bloco 020103 - Relacionamento com Fornecedores – Por Período 
################################################################################################
def processaBloco020103(linha):
    DescPeriodoRelacionamento = str(linha[7:21]).strip()
    QtdeFontesRelacionamento = str(linha[21:25]).strip()
    AreaReservada = str(linha[25:36]).strip()

    return {
        'DescPeriodoRelacionamento' : DescPeriodoRelacionamento,
        'QtdeFontesRelacionamento' : QtdeFontesRelacionamento,
        'AreaReservada' : AreaReservada
    }

################################################################################################
#Bloco 020104 - Relacionamento com Fornecedores – Mais Antigo
################################################################################################
def processaBloco020104(linha):
    DescMesMaisAntigo = str(linha[7:10]).strip()
    AnoRelacionamentoMaisAntigo = str(linha[10:12]).strip()
    MesRelacionamentoMaisAntigo = str(linha[12:14]).strip()
    AnoRelacionamentoMaisAntigoSeculo = str(linha[14:18]).strip()

    return {
        'DescMesMaisAntigo' : DescMesMaisAntigo,
        'AnoRelacionamentoMaisAntigo' : AnoRelacionamentoMaisAntigo,
        'MesRelacionamentoMaisAntigo' : MesRelacionamentoMaisAntigo,
        'AnoRelacionamentoMaisAntigoSeculo' : AnoRelacionamentoMaisAntigoSeculo
    }

################################################################################################
#Bloco 021105 - Histórico de Pagamentos - valores em R$ 
################################################################################################
def processaBloco021105(linha):
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
    AreaReservada = str(linha[97:108]).strip()

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
        'AreaReservada' : AreaReservada
    }

################################################################################################
#Bloco 021106 - Evolução de Compromissos com Fornecedores
################################################################################################
def processaBloco021106(linha):
    AnoCompromisso = str(linha[7:9]).strip()
    MesCompromisso = str(linha[9:11]).strip()
    DescMesCompromisso = str(linha[11:14]).strip()
    CodFaixavencidos = str(linha[14:17]).strip()
    DescFaixaVencidos = str(linha[17:37]).strip()
    ValorCompromissosVencidosDe = str(linha[37:52]).strip()
    ValorCompromissosVencidosAte = str(linha[52:67]).strip()
    CodFaixaAVencer = str(linha[67:70]).strip()
    DescFaixaAVencer = str(linha[70:90]).strip()
    ValorCompromissosAVencerDe = str(linha[90:105]).strip()
    ValorCompromissosAVencerAte = str(linha[105:120]).strip()
    AreaReservada = str(linha[120:184]).strip()

    return {
        'AnoCompromisso' : AnoCompromisso,
        'MesCompromisso' : MesCompromisso,
        'DescMesCompromisso' : DescMesCompromisso,
        'CodFaixavencidos' : CodFaixavencidos,
        'DescFaixaVencidos' : DescFaixaVencidos,
        'ValorCompromissosVencidosDe' : ValorCompromissosVencidosDe,
        'ValorCompromissosVencidosAte' : ValorCompromissosVencidosAte,
        'CodFaixaAVencer' : CodFaixaAVencer,
        'DescFaixaAVencer' : DescFaixaAVencer,
        'ValorCompromissosAVencerDe' : ValorCompromissosAVencerDe,
        'ValorCompromissosAVencerAte' : ValorCompromissosAVencerAte,
        'AreaReservada' : AreaReservada
    }

################################################################################################
#Bloco 021107 - Referenciais de Negócios
################################################################################################
def processaBloco021107(linha):
    DescNegocio = str(linha[7:21]).strip()
    DataPotencial = str(linha[21:27]).strip()
    CodFaixaValorPotencial = str(linha[27:30]).strip()
    DescFaixaValorPotencial = str(linha[30:50]).strip()
    ValorPotencialDe = str(linha[50:65]).strip()
    ValorPotencialAte = str(linha[65:80]).strip()
    CodFaixaMediaPotencial = str(linha[80:83]).strip()
    DescFaixaMediaPotencial = str(linha[83:103]).strip()
    ValorFaixaMediaPotencialDe = str(linha[103:118]).strip()
    ValorFaixaMediaPotencialAte = str(linha[118:133]).strip()
    SegmentoOrigemInformacao = str(linha[133:136]).strip()
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
        'ValorFaixaMediaPotencialDe' : ValorFaixaMediaPotencialDe,
        'ValorFaixaMediaPotencialAte' : ValorFaixaMediaPotencialAte,
        'SegmentoOrigemInformacao' : SegmentoOrigemInformacao,
        'AreaReservada' : AreaReservada
    }

################################################################################################
#Bloco 021108 - Histórico de Pagamento
################################################################################################
def processaBloco021108(linha):
    DescPeriodo = str(linha[7:21]).strip()
    CodFaixaQtdePeriodo = str(linha[21:24]).strip()
    DescFaixaQtdePeriodo = str(linha[24:44]).strip()
    QtdePeriodoDe = str(linha[44:59]).strip()
    QtdePeriodoAte = str(linha[59:74]).strip()
    PercentualPeriodoDe = str(linha[74:79]).strip()
    PercentualPeriodoAte = str(linha[79:84]).strip()
    AreaReservada = str(linha[84:92]).strip()

    return {
        'DescPeriodo' : DescPeriodo,
        'CodFaixaQtdePeriodo' : CodFaixaQtdePeriodo,
        'DescFaixaQtdePeriodo' : DescFaixaQtdePeriodo,
        'QtdePeriodoDe' : QtdePeriodoDe,
        'QtdePeriodoAte' : QtdePeriodoAte,
        'PercentualPeriodoDe' : PercentualPeriodoDe,
        'PercentualPeriodoAte' : PercentualPeriodoAte,
        'AreaReservada' : AreaReservada
    }

################################################################################################
#Bloco 021109 - Referenciais de Negócios Analítico (Individual) 
################################################################################################
def processaBloco021109(linha):
    MneFornecedor = str(linha[7:17]).strip()
    DataAtualizacao = str(linha[17:23]).strip()
    DataUltima = str(linha[23:29]).strip()
    CodFaixaValorUltimaCompra = str(linha[29:32]).strip()
    DescFaixaValorUltimaCompra = str(linha[32:52]).strip()
    ValorUltimaCompraDe = str(linha[52:67]).strip()
    ValorUltimaCompraAte = str(linha[67:82]).strip()
    DataMaiorFatura = str(linha[82:88]).strip()
    CodFaixaValorMaiorFatura = str(linha[88:91]).strip()
    DescFaixaValorMaiorFatura = str(linha[91:111]).strip()
    MaiorValorFaturaDe = str(linha[111:126]).strip()
    MaiorValorFaturaAte = str(linha[126:141]).strip()
    DataMaiorAcumulo = str(linha[141:147]).strip()
    CodFaixaValorMaiorAcumulo = str(linha[147:150]).strip()
    DescFaixaValorMaiorAcumulo = str(linha[150:170]).strip()
    ValorMaiorAcumuloDe = str(linha[170:185]).strip()
    ValorMaiorAcumuloAte = str(linha[185:200]).strip()
    SegOrigemInf = str(linha[200:203]).strip()
    
    CodTipoPrazo = str(linha[203:204]).strip()
    DescTipoPrazo = buscaTipoPrazo(str(linha[203:204]).strip())
    
    AreaReservada = str(linha[204:212])

    return {
        'MneFornecedor' : MneFornecedor,
        'DataAtualizacao' : DataAtualizacao,
        'DataUltima' : DataUltima,
        'CodFaixaValorUltimaCompra' : CodFaixaValorUltimaCompra,
        'DescFaixaValorUltimaCompra' : DescFaixaValorUltimaCompra,
        'ValorUltimaCompraDe' : ValorUltimaCompraDe,
        'ValorUltimaCompraAte' : ValorUltimaCompraAte,
        'DataMaiorFatura' : DataMaiorFatura,
        'CodFaixaValorMaiorFatura' : CodFaixaValorMaiorFatura,
        'DescFaixaValorMaiorFatura' : DescFaixaValorMaiorFatura,
        'MaiorValorFaturaDe' : MaiorValorFaturaDe,
        'MaiorValorFaturaAte' : MaiorValorFaturaAte,
        'DataMaiorAcumulo' : DataMaiorAcumulo,
        'CodFaixaValorMaiorAcumulo' : CodFaixaValorMaiorAcumulo,
        'DescFaixaValorMaiorAcumulo' : DescFaixaValorMaiorAcumulo,
        'ValorMaiorAcumuloDe' : ValorMaiorAcumuloDe,
        'ValorMaiorAcumuloAte' : ValorMaiorAcumuloAte,
        'SegOrigemInf' : SegOrigemInf,
        'CodTipoPrazo' : CodTipoPrazo,
        'DescTipoPrazo' : DescTipoPrazo,
        'AreaReservada' : AreaReservada
    }

################################################################################################
#Bloco 021110 - Compromissos Analítico (Individual)
################################################################################################
def processaBloco021110(linha):
    MneFornecedor = str(linha[7:17]).strip()
    DataAtualizacao = str(linha[17:23]).strip()
    CodFaixaValoresVencidos = str(linha[23:26]).strip()
    DescFaixaValoresVencidos = str(linha[26:46]).strip()
    ValoresVencidosDe = str(linha[46:61]).strip()
    ValoresVencidosAte = str(linha[61:76]).strip()
    CodFaixaValorAVencer = str(linha[76:79]).strip()
    DescFaixaValorAVencer = str(linha[79:99]).strip()
    ValoresAVencerDe = str(linha[99:114]).strip()
    ValoresAVencerAte = str(linha[114:129]).strip()
    SegOrigemInf = str(linha[129:132]).strip()
    AreaReservada = str(linha[132:140]).strip()

    return {
        'MneFornecedor' : MneFornecedor,
        'DataAtualizacao' : DataAtualizacao,
        'CodFaixaValoresVencidos' : CodFaixaValoresVencidos,
        'DescFaixaValoresVencidos' : DescFaixaValoresVencidos,
        'ValoresVencidosDe' : ValoresVencidosDe,
        'ValoresVencidosAte' : ValoresVencidosAte,
        'CodFaixaValorAVencer' : CodFaixaValorAVencer,
        'DescFaixaValorAVencer' : DescFaixaValorAVencer,
        'ValoresAVencerDe' : ValoresAVencerDe,
        'ValoresAVencerAte' : ValoresAVencerAte,
        'SegOrigemInf' : SegOrigemInf,
        'AreaReservada' : AreaReservada
    }

################################################################################################
#Bloco 021118 - Histórico de Pagamentos (valores em R$) (Individual)
################################################################################################
def processaBloco021118(linha):
    MneFornecedor = str(linha[7:17]).strip()
    DataAtualizacao = str(linha[17:23]).strip()
    DataMaiorValor = str(linha[23:29]).strip()
    CodFaixaMaiorValor = str(linha[29:32]).strip()
    DescFaixaMaiorValor = str(linha[32:51]).strip()
    MaiorValorDe = str(linha[51:66]).strip()
    MaiorValorAte = str(linha[66:81]).strip()
    DataDiasAtraso = str(linha[81:87]).strip()
    CodFaixaDiasAtraso = str(linha[87:90]).strip()
    DescFaixaDiasAtraso = str(linha[90:109]).strip()
    QtdeDiasAtrasoDe = str(linha[109:122]).strip()
    QtdeDiasAtrasoAte = str(linha[122:135]).strip()
    
    CodSinalDiasAtraso = str(linha[135:136]).strip()
    DescSinalDiasAtraso = buscaTipoSinalDiasAtraso(str(linha[135:136]).strip())

    CodFaixaTotalPagtos = str(linha[136:139]).strip()
    DescFaixaTotalPagtos = str(linha[139:158]).strip()
    TotalPagtosDe = str(linha[158:171]).strip()
    TotalPagtosAte = str(linha[171:184]).strip()
    CodFaixaTotalPagtosAtraso = str(linha[184:187]).strip()
    DescFaixaTotalPagtosAtraso = str(linha[187:206]).strip()
    QtdePagtosAtrasadosDe = str(linha[206:219]).strip()
    QtdePagtosAtrasadosPara = str(linha[219:232]).strip()
    CodFaixaMediasDiasAtraso = str(linha[232:235]).strip()
    DescFaixaMediasDiasAtraso = str(linha[235:254]).strip()
    MediaDiasAtrasoDe = str(linha[254:267]).strip()
    MediaDiasAtrasoAte = str(linha[267:280]).strip()
    SegOrigemInf = str(linha[280:283]).strip()
    AreaReservada = str(linha[283:291]).strip()

    return {
        'MneFornecedor' : MneFornecedor,
        'DataAtualizacao' : DataAtualizacao,
        'DataMaiorValor' : DataMaiorValor,
        'CodFaixaMaiorValor' : CodFaixaMaiorValor,
        'DescFaixaMaiorValor' : DescFaixaMaiorValor,
        'MaiorValorDe' : MaiorValorDe,
        'MaiorValorAte' : MaiorValorAte,
        'DataDiasAtraso' : DataDiasAtraso,
        'CodFaixaDiasAtraso' : CodFaixaDiasAtraso,
        'DescFaixaDiasAtraso' : DescFaixaDiasAtraso,
        'QtdeDiasAtrasoDe' : QtdeDiasAtrasoDe,
        'QtdeDiasAtrasoAte' : QtdeDiasAtrasoAte,
        'CodSinalDiasAtraso' : CodSinalDiasAtraso,
        'DescSinalDiasAtraso' : DescSinalDiasAtraso,
        'CodFaixaTotalPagtos' : CodFaixaTotalPagtos,
        'DescFaixaTotalPagtos' : DescFaixaTotalPagtos,
        'TotalPagtosDe' : TotalPagtosDe,
        'TotalPagtosAte' : TotalPagtosAte,
        'CodFaixaTotalPagtosAtraso' : CodFaixaTotalPagtosAtraso,
        'DescFaixaTotalPagtosAtraso' : DescFaixaTotalPagtosAtraso,
        'QtdePagtosAtrasadosDe' : QtdePagtosAtrasadosDe,
        'QtdePagtosAtrasadosPara' : QtdePagtosAtrasadosPara,
        'CodFaixaMediasDiasAtraso' : CodFaixaMediasDiasAtraso,
        'DescFaixaMediasDiasAtraso' : DescFaixaMediasDiasAtraso,
        'MediaDiasAtrasoDe' : MediaDiasAtrasoDe,
        'MediaDiasAtrasoAte' : MediaDiasAtrasoAte,
        'SegOrigemInf' : SegOrigemInf,
        'AreaReservada' : AreaReservada
    }

################################################################################################
#Bloco 020119 - Relacionamento com Fornecedores (Individual)
################################################################################################
def processaBloco020119(linha):
    MneFornecedor = str(linha[7:17]).strip()
    DataAtualizacao = str(linha[17:25]).strip()
    DataClienteDesde = str(linha[25:33]).strip()
    SegOrigemInf = str(linha[33:36]).strip()

    return {
        'MneFornecedor' : MneFornecedor,
        'DataAtualizacao' : DataAtualizacao,
        'DataClienteDesde' : DataClienteDesde,
        'SegOrigemInf' : SegOrigemInf
    }

################################################################################################
#Bloco 023406 - Total do Evolução de compromisso (Mercado)
################################################################################################
def processaBloco023406(linha):
    IdentColuna = str(linha[7:21]).strip()
    CodFaixaTotalVencido = str(linha[21:24]).strip()
    DescFaixaTotalVencido = str(linha[24:44]).strip()
    TotalVencidosDe = str(linha[44:59]).strip()
    TotalVencidosAte = str(linha[59:74]).strip()
    CodFaixaAVencer = str(linha[74:77]).strip()
    DescFaixaAVencer = str(linha[77:97]).strip()
    TotalAVencerDe = str(linha[97:112]).strip()
    TotalAVencerAte = str(linha[112:127]).strip()
    CodFaixaTotalMercado = str(linha[127:130]).strip()
    DescFaixaTotalMercado = str(linha[130:150]).strip()
    TotalMercadoDe = str(linha[150:165]).strip()
    TotalMercadoAte = str(linha[165:180]).strip()
    SegOrigemInf = str(linha[180:183]).strip()
    SubGrupoOrigemInf = str(linha[183:187]).strip()

    return {
        'IdentColuna' : IdentColuna,
        'CodFaixaTotalVencido' : CodFaixaTotalVencido,
        'DescFaixaTotalVencido' : DescFaixaTotalVencido,
        'TotalVencidosDe' : TotalVencidosDe,
        'TotalVencidosAte' : TotalVencidosAte,
        'CodFaixaAVencer' : CodFaixaAVencer,
        'DescFaixaAVencer' : DescFaixaAVencer,
        'TotalAVencerDe' : TotalAVencerDe,
        'TotalAVencerAte' : TotalAVencerAte,
        'CodFaixaTotalMercado' : CodFaixaTotalMercado,
        'DescFaixaTotalMercado' : DescFaixaTotalMercado,
        'TotalMercadoDe' : TotalMercadoDe,
        'TotalMercadoAte' : TotalMercadoAte,
        'SegOrigemInf' : SegOrigemInf,
        'SubGrupoOrigemInf' : SubGrupoOrigemInf
    }

################################################################################################
#Bloco 023416 - Total do Evolução de compromisso (Segmento)
################################################################################################
def processaBloco023416(linha):
    IdentColuna = str(linha[7:21]).strip()
    CodFaixaTotalVencido = str(linha[21:24]).strip()
    DescFaixaTotalVencido = str(linha[24:44]).strip()
    TotalVencidosDe = str(linha[44:59]).strip()
    TotalVencidosAte = str(linha[59:74]).strip()
    CodFaixaAVencer = str(linha[74:77]).strip()
    DescFaixaAVencer = str(linha[77:97]).strip()
    TotalAVencerDe = str(linha[97:112]).strip()
    TotalAVencerAte = str(linha[112:127]).strip()
    CodFaixaTotalSegmento = str(linha[127:130]).strip()
    DescFaixaTotalSegmento = str(linha[130:150]).strip()
    TotalMercadoDe = str(linha[150:165]).strip()
    TotalMercadoAte = str(linha[165:180]).strip()
    SegOrigemInf = str(linha[180:183]).strip()
    SubGrupoOrigemInf = str(linha[183:187]).strip()

    return {
        'IdentColuna' : IdentColuna,
        'CodFaixaTotalVencido' : CodFaixaTotalVencido,
        'DescFaixaTotalVencido' : DescFaixaTotalVencido,
        'TotalVencidosDe' : TotalVencidosDe,
        'TotalVencidosAte' : TotalVencidosAte,
        'CodFaixaAVencer' : CodFaixaAVencer,
        'DescFaixaAVencer' : DescFaixaAVencer,
        'TotalAVencerDe' : TotalAVencerDe,
        'TotalAVencerAte' : TotalAVencerAte,
        'CodFaixaTotalSegmento' : CodFaixaTotalSegmento,
        'DescFaixaTotalSegmento' : DescFaixaTotalSegmento,
        'TotalMercadoDe' : TotalMercadoDe,
        'TotalMercadoAte' : TotalMercadoAte,
        'SegOrigemInf' : SegOrigemInf,
        'SubGrupoOrigemInf' : SubGrupoOrigemInf
    }

################################################################################################
#Bloco 023426 - Total do Evolução de compromisso (Cedente)
################################################################################################
def processaBloco023426(linha):
    IdentColuna = str(linha[7:21]).strip()
    CodFaixaTotalVencido = str(linha[21:24]).strip()
    DescFaixaTotalVencido = str(linha[24:44]).strip()
    TotalVencidosDe = str(linha[44:59]).strip()
    TotalVencidosAte = str(linha[59:74]).strip()
    CodFaixaAVencer = str(linha[74:77]).strip()
    DescFaixaAVencer = str(linha[77:97]).strip()
    TotalAVencerDe = str(linha[97:112]).strip()
    TotalAVencerAte = str(linha[112:127]).strip()
    CodFaixaTotalCedente = str(linha[127:130]).strip()
    DescFaixaTotalCedente = str(linha[130:150]).strip()
    TotalMercadoDe = str(linha[150:165]).strip()
    TotalMercadoAte = str(linha[165:180]).strip()
    SegOrigemInf = str(linha[180:183]).strip()
    SubGrupoOrigemInf = str(linha[183:187]).strip()

    return {
        'IdentColuna' : IdentColuna,
        'CodFaixaTotalVencido' : CodFaixaTotalVencido,
        'DescFaixaTotalVencido' : DescFaixaTotalVencido,
        'TotalVencidosDe' : TotalVencidosDe,
        'TotalVencidosAte' : TotalVencidosAte,
        'CodFaixaAVencer' : CodFaixaAVencer,
        'DescFaixaAVencer' : DescFaixaAVencer,
        'TotalAVencerDe' : TotalAVencerDe,
        'TotalAVencerAte' : TotalAVencerAte,
        'CodFaixaTotalCedente' : CodFaixaTotalCedente,
        'DescFaixaTotalCedente' : DescFaixaTotalCedente,
        'TotalMercadoDe' : TotalMercadoDe,
        'TotalMercadoAte' : TotalMercadoAte,
        'SegOrigemInf' : SegOrigemInf,
        'SubGrupoOrigemInf' : SubGrupoOrigemInf
    }

################################################################################################
#Bloco 025405 - Análise comparativa histórico de pagamentos  (Mercado)
################################################################################################
def processaBloco025405(linha):
    AnoCompromisso = str(linha[7:9]).strip()
    MesCompromisso = str(linha[9:11]).strip()
    DescMesCompromisso = str(linha[11:14]).strip()
    CodFaixaAVencer = str(linha[14:17]).strip()
    DescFaixaAVencer = str(linha[17:37]).strip()
    TotalAVencerDe = str(linha[37:52]).strip()
    TotalAVencerAte = str(linha[52:67]).strip()
    CodFaixaTotalAPrazo = str(linha[67:70]).strip()
    DescFaixaTotalAPrazo = str(linha[70:90]).strip()
    TotalAPrazoDe = str(linha[90:105]).strip()
    TotalAPrazoAte = str(linha[105:120]).strip()
    SegOrigemInf = str(linha[120:123]).strip()
    AreaReservada = str(linha[123:131]).strip()

    return {
        'AnoCompromisso' : AnoCompromisso,
        'MesCompromisso' : MesCompromisso,
        'DescMesCompromisso' : DescMesCompromisso,
        'CodFaixaAVencer' : CodFaixaAVencer,
        'DescFaixaAVencer' : DescFaixaAVencer,
        'TotalAVencerDe' : TotalAVencerDe,
        'TotalAVencerAte' : TotalAVencerAte,
        'CodFaixaTotalAPrazo' : CodFaixaTotalAPrazo,
        'DescFaixaTotalAPrazo' : DescFaixaTotalAPrazo,
        'TotalAPrazoDe' : TotalAPrazoDe,
        'TotalAPrazoAte' : TotalAPrazoAte,
        'SegOrigemInf' : SegOrigemInf,
        'AreaReservada' : AreaReservada
    }

################################################################################################
#Bloco 025415 - Análise comparativa histórico de pagamentos  (Segmento)
################################################################################################
def processaBloco025415(linha):
    AnoCompromisso = str(linha[7:9]).strip()
    MesCompromisso = str(linha[9:11]).strip()
    DescMesCompromisso = str(linha[11:14]).strip()
    CodFaixaAVencer = str(linha[14:17]).strip()
    DescFaixaAVencer = str(linha[17:37]).strip()
    TotalAVencerDe = str(linha[37:52]).strip()
    TotalAVencerAte = str(linha[52:67]).strip()
    CodFaixaTotalAPrazo = str(linha[67:70]).strip()
    DescFaixaTotalAPrazo = str(linha[70:90]).strip()
    TotalAPrazoDe = str(linha[90:105]).strip()
    TotalAPrazoAte = str(linha[105:120]).strip()
    SegOrigemInf = str(linha[120:123]).strip()
    AreaReservada = str(linha[123:131]).strip()

    return {
        'AnoCompromisso' : AnoCompromisso,
        'MesCompromisso' : MesCompromisso,
        'DescMesCompromisso' : DescMesCompromisso,
        'CodFaixaAVencer' : CodFaixaAVencer,
        'DescFaixaAVencer' : DescFaixaAVencer,
        'TotalAVencerDe' : TotalAVencerDe,
        'TotalAVencerAte' : TotalAVencerAte,
        'CodFaixaTotalAPrazo' : CodFaixaTotalAPrazo,
        'DescFaixaTotalAPrazo' : DescFaixaTotalAPrazo,
        'TotalAPrazoDe' : TotalAPrazoDe,
        'TotalAPrazoAte' : TotalAPrazoAte,
        'SegOrigemInf' : SegOrigemInf,
        'AreaReservada' : AreaReservada
    }
