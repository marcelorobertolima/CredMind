#DadosApontamentos_05.py
from datetime import datetime
from APICredMind.views.SERASA.mappingsSERASA import *

################################################################################################
#Bloco 040101 - Pendências Financeiras – PEFIN
################################################################################################
def processaBloco040101(linha):
    QtdePEFIN = str(linha[7:16]).strip()
    QtdeUltimaOcorrencia = str(linha[16:25]).strip()
    DataOcorrencia = str(linha[25:33]).strip()
    TituloOcorrencia = str(linha[33:45]).strip()
    Avalista = str(linha[45:46]).strip()
    ValorPendencia = str(linha[46:59]).strip()
    Contrato = str(linha[59:75]).strip()
    OrigemPendencia = str(linha[75:95]).strip()
    FilialOcorrencia = str(linha[95:99]).strip()
    SubJudicePraca = str(linha[99:103]).strip()
    SubJudiceDistrito = str(linha[103:105]).strip()
    SubJudiceVara = str(linha[105:107]).strip()
    SubJudiceData = str(linha[107:115]).strip()
    SubJudiceProcesso = str(linha[115:131]).strip()
   
    CodNatureza = str(linha[131:134]).strip()
    DescNatureza = buscaTipoNaturezaModalidadeCONVEMPEFIN(str(linha[131:134]).strip())

    AreaReservada = str(linha[134:158]).strip()
    MsgSubJudice = str(linha[158:234]).strip()
    ValorTotalPendenciaFinan = str(linha[234:247]).strip()
    AreaReservada2 = str(linha[247:248]).strip()

    return {
        'QtdePEFIN' : QtdePEFIN,
        'QtdeUltimaOcorrencia' : QtdeUltimaOcorrencia,
        'DataOcorrencia' : DataOcorrencia,
        'TituloOcorrencia' : TituloOcorrencia,
        'Avalista' : Avalista,
        'ValorPendencia' : ValorPendencia,
        'Contrato' : Contrato,
        'OrigemPendencia' : OrigemPendencia,
        'FilialOcorrencia' : FilialOcorrencia,
        'SubJudicePraca' : SubJudicePraca,
        'SubJudiceDistrito' : SubJudiceDistrito,
        'SubJudiceVara' : SubJudiceVara,
        'SubJudiceData' : SubJudiceData,
        'SubJudiceProcesso' : SubJudiceProcesso,
        'CodNatureza' : CodNatureza,
        'DescNatureza' : DescNatureza,
        'AreaReservada' : AreaReservada,
        'MsgSubJudice' : MsgSubJudice,
        'ValorTotalPendenciaFinan' : ValorTotalPendenciaFinan,
        'AreaReservada2' : AreaReservada2
    }

################################################################################################
#Bloco 040102 - Pendências Financeiras - REFIN
################################################################################################
def processaBloco040102(linha):
    QtdeREFIN = str(linha[7:16]).strip()
    QtdeUltimaOcorrencia = str(linha[16:25]).strip()
    DataOcorrencia = str(linha[25:33]).strip()
    TituloOcorrencia = str(linha[33:45]).strip()
    Avalista = str(linha[45:46]).strip()
    ValorPendencia = str(linha[46:59]).strip()
    Contrato = str(linha[59:75]).strip()
    OrigemPendencia = str(linha[75:95]).strip()
    FilialOcorrencia = str(linha[95:99]).strip()

    SubJudicePraca = str(linha[99:103]).strip()
    SubJudiceDistrito = str(linha[103:105]).strip()
    SubJudiceVara = str(linha[105:107]).strip()
    SubJudiceData = str(linha[107:115]).strip()
    SubJudiceProcesso = str(linha[115:131]).strip()

    CodNatureza = str(linha[131:134]).strip()
    DescNatureza = buscaTipoNaturezaRestricoesFinanREFIN(str(linha[131:134]).strip())

    AreaReservada = str(linha[134:158]).strip()
    MsgSubJudice = str(linha[158:234]).strip()
    ValorTotalPendenciaFinan = str(linha[234:247]).strip()
    AreaReservada2 = str(linha[247:248]).strip()

    return {
        'QtdeREFIN' : QtdeREFIN,
        'QtdeUltimaOcorrencia' : QtdeUltimaOcorrencia,
        'DataOcorrencia' : DataOcorrencia,
        'TituloOcorrencia' : TituloOcorrencia,
        'Avalista' : Avalista,
        'ValorPendencia' : ValorPendencia,
        'Contrato' : Contrato,
        'OrigemPendencia' : OrigemPendencia,
        'FilialOcorrencia' : FilialOcorrencia,
        'SubJudicePraca' : SubJudicePraca,
        'SubJudiceDistrito' : SubJudiceDistrito,
        'SubJudiceVara' : SubJudiceVara,
        'SubJudiceData' : SubJudiceData,
        'SubJudiceProcesso' : SubJudiceProcesso,
        'CodNatureza' : CodNatureza,
        'DescNatureza' : DescNatureza,
        'AreaReservada' : AreaReservada,
        'MsgSubJudice' : MsgSubJudice,
        'ValorTotalPendenciaFinan' : ValorTotalPendenciaFinan,
        'AreaReservada2' : AreaReservada2
    }
   

################################################################################################
#Bloco 040201 - Informações do Concentre – Grafias
################################################################################################
def processaBloco040201(linha):
    Grafias = str(linha[7:77]).strip()
 
    return {
        'Grafias' : Grafias
    }

################################################################################################
#Bloco 040202 - Informações do Concentre – Resumo
################################################################################################
def processaBloco040202(linha):
    QtdeOcorrencias = str(linha[7:16]).strip()
    GrupoOcorrencia = str(linha[16:43]).strip()
    DescMesInicialOcorrencia = str(linha[43:46]).strip()
    MesInicialOcorrencia = str(linha[46:48]).strip()
    AnoInicialOcorrencia = str(linha[48:50]).strip()
    DescMesFinalOcorrencia = str(linha[50:53]).strip()
    MesFinalOcorrencia = str(linha[53:55]).strip()
    AnoFinalOcorrencia = str(linha[55:57]).strip()
    MoedaOcorrencia = str(linha[57:60]).strip()
    ValorOcorrencia = str(linha[60:73]).strip()
    OrigemOcorrencia = str(linha[73:93]).strip()
    AgenciaOcorrencia = str(linha[93:97]).strip()
    TotalValor = str(linha[97:110]).strip()
    
    CodNatureza = str(linha[110:113]).strip()
    DescNatureza = buscaTipoNaturezaCONCENTRE(str(linha[110:113]).strip())
 
    return {
        'QtdeOcorrencias' : QtdeOcorrencias,
        'GrupoOcorrencia' : GrupoOcorrencia,
        'DescMesInicialOcorrencia' : DescMesInicialOcorrencia,
        'MesInicialOcorrencia' : MesInicialOcorrencia,
        'AnoInicialOcorrencia' : AnoInicialOcorrencia,
        'DescMesFinalOcorrencia' : DescMesFinalOcorrencia,
        'MesFinalOcorrencia' : MesFinalOcorrencia,
        'AnoFinalOcorrencia' : AnoFinalOcorrencia,
        'MoedaOcorrencia' : MoedaOcorrencia,
        'ValorOcorrencia' : ValorOcorrencia,
        'OrigemOcorrencia' : OrigemOcorrencia,
        'AgenciaOcorrencia' : AgenciaOcorrencia,
        'TotalValor' : TotalValor,
        'CodNatureza' : CodNatureza,
        'DescNatureza' : DescNatureza
    }

################################################################################################
#Bloco 040301 - Informações do Concentre – Protestos
################################################################################################
def processaBloco040301(linha):
    QtdeOcorrencias = str(linha[7:16]).strip()
    DataProtesto = str(linha[16:24]).strip()
    MoedaOcorrencia = str(linha[24:27]).strip()
    ValorProtesto = str(linha[27:40]).strip()
    Cartorio = str(linha[40:42]).strip()
    CidadeOcorrencia = str(linha[42:72]).strip()
    UFOcorrencia = str(linha[72:74]).strip()
    
    SubJudicePraca = str(linha[74:78]).strip()
    SubJudiceDistrito = str(linha[78:80]).strip()
    SubJudiceVara = str(linha[80:82]).strip()
    SubJudiceData = str(linha[82:90]).strip()
    SubJudiceProcesso = str(linha[90:106]).strip()

    CodNatureza = str(linha[106:109]).strip()
    DescNatureza = buscaTipoProtesto(str(linha[106:109]).strip())

    AreaReservada = str(linha[109:133]).strip()
    
    CodTipoCartaAnuencia = str(linha[133:134]).strip()
    DescTipoCartaAnuencia = buscaTipoCartaAnuencia(str(linha[133:134]).strip())

    DataRecebCartaAnuencia = str(linha[134:142]).strip()
    
    MsgSubJudice = str(linha[142:218]).strip()
    AreaReservada2 = str(linha[218:219]).strip()
    
    return {
        'QtdeOcorrencias' : QtdeOcorrencias,
        'DataProtesto' : DataProtesto,
        'MoedaOcorrencia' : MoedaOcorrencia,
        'ValorProtesto' : ValorProtesto,
        'Cartorio' : Cartorio,
        'CidadeOcorrencia' : CidadeOcorrencia,
        'UFOcorrencia' : UFOcorrencia,
        'SubJudicePraca' : SubJudicePraca,
        'SubJudiceDistrito' : SubJudiceDistrito,
        'SubJudiceVara' : SubJudiceVara,
        'SubJudiceData' : SubJudiceData,
        'SubJudiceProcesso' : SubJudiceProcesso,
        'CodNatureza': CodNatureza,
        'DescNatureza': DescNatureza,
        'AreaReservada': AreaReservada,
        'CodTipoCartaAnuencia': CodTipoCartaAnuencia,
        'DescTipoCartaAnuencia': DescTipoCartaAnuencia,
        'DataRecebCartaAnuencia': DataRecebCartaAnuencia,
        'MsgSubJudice': MsgSubJudice,
        'AreaReservada2': AreaReservada2
    }

################################################################################################
#Bloco 040401 - Informações do Concentre - Ação Judicial
################################################################################################
def processaBloco040401(linha):
    QtdeOcorrencias = str(linha[7:16]).strip()
    DataAcao = str(linha[16:24]).strip()
    NaturezaAcao = str(linha[24:44]).strip()
    AvalistaAcao = str(linha[44:45]).strip()
    MoedaAcao = str(linha[45:48]).strip()
    ValorAcao = str(linha[48:61]).strip()
    DistritoAcao = str(linha[61:63]).strip()
    VaraCivelAcao = str(linha[63:67]).strip()
    CidadeAcao = str(linha[67:97]).strip()
    UFAcao = str(linha[97:99]).strip()
    
    SubJudicePraca = str(linha[99:103]).strip()
    SubJudiceDistrito = str(linha[103:105]).strip()
    SubJudiceVara = str(linha[105:107]).strip()
    SubJudiceData = str(linha[107:115]).strip()
    SubJudiceProcesso = str(linha[115:131]).strip()

    CodNatureza = str(linha[131:134]).strip()
    DescNatureza = buscaTipoAcao(str(linha[131:134]).strip())

    AreaReservada = str(linha[134:158]).strip()
    
    MsgSubJudice = str(linha[158:234]).strip()
    AreaReservada2 = str(linha[234:235]).strip()
    
    return {
        'QtdeOcorrencias' : QtdeOcorrencias,
        'DataAcao' : DataAcao,
        'NaturezaAcao' : NaturezaAcao,
        'AvalistaAcao' : AvalistaAcao,
        'MoedaAcao' : MoedaAcao,
        'ValorAcao' : ValorAcao,
        'DistritoAcao' : DistritoAcao,
        'VaraCivelAcao' : VaraCivelAcao,
        'CidadeAcao' : CidadeAcao,
        'UFAcao' : UFAcao,
        'SubJudicePraca' : SubJudicePraca,
        'SubJudiceDistrito' : SubJudiceDistrito,
        'SubJudiceVara' : SubJudiceVara,
        'SubJudiceData' : SubJudiceData,
        'SubJudiceProcesso' : SubJudiceProcesso,
        'CodNatureza': CodNatureza,
        'DescNatureza': DescNatureza,
        'AreaReservada': AreaReservada,
        'MsgSubJudice': MsgSubJudice,
        'AreaReservada2': AreaReservada2
    }

################################################################################################
#Bloco 040501 - Informações do Concentre - Participação em Falência
################################################################################################
def processaBloco040501(linha):
    QtdeOcorrencias = str(linha[7:16]).strip()
    DataAcao = str(linha[16:24]).strip()
    TipoParticipacao = str(linha[24:44]).strip()
    CNPJParticipacao = str(linha[44:53]).strip()
    EmpresaParticipacao = str(linha[53:121]).strip()

    CodNatureza = str(linha[121:124]).strip()
    DescNatureza = buscaTipoPIE(str(linha[121:124]).strip())
 
    AreaReservada = str(linha[124:148]).strip()

    return {
        'QtdeOcorrencias' : QtdeOcorrencias,
        'DataAcao' : DataAcao,
        'TipoParticipacao' : TipoParticipacao,
        'CNPJParticipacao' : CNPJParticipacao,
        'EmpresaParticipacao' : EmpresaParticipacao,
        'CodNatureza' : CodNatureza,
        'DescNatureza' : DescNatureza,
        'AreaReservada': AreaReservada
    }

################################################################################################
#Bloco 040601 - Informações do Concentre - Falência e Concordata
################################################################################################
def processaBloco040601(linha):
    QtdeOcorrencias = str(linha[7:16]).strip()
    DataFalenciaConcordata = str(linha[16:24]).strip()
    TipoFalenciaConcordata = str(linha[24:44]).strip()
    OrigemFalenciaConcordata = str(linha[44:49]).strip()
    VaraCivel = str(linha[49:53]).strip()
    CidadeFalenciaConcordata = str(linha[53:83]).strip()
    UFFalenciaConcordata = str(linha[83:85]).strip()

    CodNatureza = str(linha[85:88]).strip()
    DescNatureza = buscaTipoFalenciaConcordata(str(linha[85:88]).strip())
 
    AreaReservada = str(linha[88:112]).strip()

    return {
        'QtdeOcorrencias' : QtdeOcorrencias,
        'DataFalenciaConcordata' : DataFalenciaConcordata,
        'TipoFalenciaConcordata' : TipoFalenciaConcordata,
        'OrigemFalenciaConcordata' : OrigemFalenciaConcordata,
        'VaraCivel' : VaraCivel,
        'CidadeFalenciaConcordata' : CidadeFalenciaConcordata,
        'UFFalenciaConcordata' : UFFalenciaConcordata,
        'CodNatureza' : CodNatureza,
        'DescNatureza' : DescNatureza,
        'AreaReservada': AreaReservada
    }

################################################################################################
#Bloco 040701 - Informações do Concentre - Dívidas Vencidas
################################################################################################
def processaBloco040701(linha):
    QtdeOcorrencias = str(linha[7:16]).strip()
    DataOcorrencia = str(linha[16:24]).strip()
    Modalidade = str(linha[24:39]).strip()
    Moeda = str(linha[39:42]).strip()
    ValorDividas = str(linha[42:55]).strip()
    TituloDivida = str(linha[55:70]).strip()
    InstituicaoFinanceira = str(linha[70:85]).strip()
    Local = str(linha[85:88]).strip()
    
    CodNatureza = str(linha[88:91]).strip()
    #23/11/2024 - Marcelo - Ao testar as strings os código DM, DS, etc não foram localizados
    #Não tem na documentação este De/Para de código
    #DescNatureza = TipoCONVEMDevedores(str(linha[88:91]).strip())
    
    AreaReservada = str(linha[91:115]).strip()
    
    SubJudicePraca = str(linha[115:119]).strip()
    SubJudiceDistrito = str(linha[119:121]).strip()
    SubJudiceVara = str(linha[121:123]).strip()
    SubJudiceData = str(linha[123:131]).strip()
    SubJudiceProcesso = str(linha[131:147]).strip()

    MsgSubJudice = str(linha[147:223]).strip()
    AreaReservada2 = str(linha[223:224]).strip()
    
    return {
        'QtdeOcorrencias' : QtdeOcorrencias,
        'DataOcorrencia' : DataOcorrencia,
        'Modalidade' : Modalidade,
        'Moeda' : Moeda,
        'ValorDividas' : ValorDividas,
        'TituloDivida' : TituloDivida,
        'InstituicaoFinanceira' : InstituicaoFinanceira,
        'Local' : Local,
        'CodNatureza': CodNatureza,
        #'DescNatureza': DescNatureza,
        'AreaReservada': AreaReservada,
        'SubJudicePraca' : SubJudicePraca,
        'SubJudiceDistrito' : SubJudiceDistrito,
        'SubJudiceVara' : SubJudiceVara,
        'SubJudiceData' : SubJudiceData,
        'SubJudiceProcesso' : SubJudiceProcesso,
        'MsgSubJudice': MsgSubJudice,
        'AreaReservada2': AreaReservada2
    }

################################################################################################
#Bloco 040801 - Informações do Recheque - Cheque sem Fundo-Achei
################################################################################################
def processaBloco040801(linha):
    QtdeOcorrencias = str(linha[7:16]).strip()
    DataOcorrencia = str(linha[16:24]).strip()
    NumeroCheque = str(linha[24:30]).strip()
    Alinea = str(linha[30:32]).strip()
    QtdeNoBanco = str(linha[32:37]).strip()
    Moeda = str(linha[37:40]).strip()
    Valor = str(linha[40:53]).strip()
    Banco = str(linha[53:65]).strip()
    Agencia = str(linha[65:69]).strip()
    Cidade = str(linha[69:99]).strip()
    UF = str(linha[99:101]).strip()

    CodNatureza = str(linha[101:104]).strip()
    DescNatureza = buscaTipoACHEI(str(linha[101:104]).strip())
 
    AreaReservada = str(linha[104:128]).strip()

    return {
        'QtdeOcorrencias' : QtdeOcorrencias,
        'DataOcorrencia' : DataOcorrencia,
        'NumeroCheque' : NumeroCheque,
        'Alinea' : Alinea,
        'QtdeNoBanco' : QtdeNoBanco,
        'Moeda' : Moeda,
        'Valor' : Valor,
        'Banco' : Banco,
        'Agencia' : Agencia,
        'Cidade' : Cidade,
        'UF' : UF,
        'CodNatureza' : CodNatureza,
        'DescNatureza' : DescNatureza,
        'AreaReservada': AreaReservada
    }

################################################################################################
#Bloco 040901 - Informações do Recheque - Cheque sem Fundo-Achei CCF
################################################################################################
def processaBloco040901(linha):
    QtdeOcorrencias = str(linha[7:16]).strip()
    DataOcorrencia = str(linha[16:24]).strip()
    NumeroCheque = str(linha[24:30]).strip()
    QtdeNoBanco = str(linha[30:35]).strip()
    Banco = str(linha[35:51]).strip()
    Agencia = str(linha[51:55]).strip()
    Cidade = str(linha[55:85]).strip()
    UF = str(linha[85:87]).strip()

    CodNatureza = str(linha[87:90]).strip()
    DescNatureza = buscaTipoCCF(str(linha[87:90]).strip())
 
    AreaReservada = str(linha[90:114]).strip()

    return {
        'QtdeOcorrencias' : QtdeOcorrencias,
        'DataOcorrencia' : DataOcorrencia,
        'NumeroCheque' : NumeroCheque,
        'QtdeNoBanco' : QtdeNoBanco,
        'Banco' : Banco,
        'Agencia' : Agencia,
        'Cidade' : Cidade,
        'UF' : UF,
        'CodNatureza' : CodNatureza,
        'DescNatureza' : DescNatureza,
        'AreaReservada': AreaReservada
    }

################################################################################################
#Bloco 041000 - Informações do Recheque - Quantidade e Última Ocorrência 
################################################################################################
def processaBloco041000(linha):
    QtdeOcorrencias = str(linha[7:16]).strip()
    QtdeUltimaOcorrencia = str(linha[16:25]).strip()

    return {
        'QtdeOcorrencias' : QtdeOcorrencias,
        'QtdeUltimaOcorrencia' : QtdeUltimaOcorrencia
    }

################################################################################################
#Bloco 041001 - Informações do Recheque – Detalhes
################################################################################################
def processaBloco041001(linha):
    Data = str(linha[7:15]).strip()
    Banco = str(linha[15:31]).strip()
    Agencia = str(linha[31:35]).strip()
    ContaCorrente = str(linha[35:41]).strip()
    DigitoConta = str(linha[41:42]).strip()
    ChequeInicial = str(linha[42:48]).strip()
    ChequeFinal = str(linha[48:54]).strip()
    Motivo = str(linha[54:64]).strip()
    ContaCorrente12B = str(linha[64:76]).strip()

    return {
        'Data' : Data,
        'Banco' : Banco,
        'Agencia' : Agencia,
        'ContaCorrente' : ContaCorrente,
        'DigitoConta' : DigitoConta,
        'ChequeInicial' : ChequeInicial,
        'ChequeFinal' : ChequeFinal,
        'Motivo' : Motivo,
        'ContaCorrente12B' : ContaCorrente12B
    }

################################################################################################
#Bloco 041101 - Informações de participantes com anotações
################################################################################################
def processaBloco041101(linha):
    NomeParticipante = str(linha[7:72]).strip()
    DctoParticipante = str(linha[72:83]).strip()
    
    CodTipoPessoaParticipante = str(linha[83:84]).strip()
    DescTipoPessoaParticipante =  buscaTipoPessoa(str(linha[83:84]).strip())

    return {
        'NomeParticipante' : NomeParticipante,
        'DctoParticipante' : DctoParticipante,
        'CodTipoPessoaParticipante' : CodTipoPessoaParticipante,
        'DescTipoPessoaParticipante' : DescTipoPessoaParticipante
    }
