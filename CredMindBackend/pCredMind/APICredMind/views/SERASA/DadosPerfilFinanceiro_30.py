#DadosPerfilFinanceiro_30.py
from datetime import datetime
from APICredMind.views.SERASA.mappingsSERASA import *

################################################################################################
#Bloco 300901 - Identificação da Empresa 
################################################################################################
def processaBloco300901(linha):
    DataAualizacao = str(linha[7:16]).strip()
    CNPJ = str(linha[16:25]).strip()
    FilialCNPJ = str(linha[25:29]).strip()
    DigCNPJ = str(linha[29:31]).strip()
    RazaoSocial = str(linha[31:101]).strip()
    NomeUsuario = str(linha[101:121]).strip()
    DataConsulta = str(linha[121:129]).strip()
    HoraConsulta = str(linha[129:135]).strip()
    
    return {
        'DataAualizacao': DataAualizacao,
        'CNPJ': CNPJ,
        'FilialCNPJ': FilialCNPJ,
        'DigCNPJ': DigCNPJ,
        'RazaoSocial': RazaoSocial,
        'NomeUsuario': NomeUsuario,
        'DataConsulta': DataConsulta,
        'HoraConsulta': HoraConsulta
    }

################################################################################################
#Bloco 300902 - Controle do Balanço
################################################################################################
def processaBloco300902(linha):
    DataBalanco = str(linha[7:16]).strip()
    TipoBalanco = str(linha[16:17]).strip()
    DescTipoBalanco = str(linha[17:37]).strip()
    TipoDemonstrativo = str(linha[37:38]).strip()
    DescTipoDemonstrativo = str(linha[38:58]).strip()
    PeriodoDemonstrativo = str(linha[58:60]).strip()
    CodUnidadeValor = str(linha[60:61]).strip()
    DescUnidadeValor = str(linha[61:81]).strip()
    Moeda = str(linha[81:82]).strip()
    DescMoeda = str(linha[82:102]).strip()
    
    return {
        'DataBalanco': DataBalanco,
        'TipoBalanco': TipoBalanco,
        'DescTipoBalanco': DescTipoBalanco,
        'TipoDemonstrativo': TipoDemonstrativo,
        'DescTipoDemonstrativo': DescTipoDemonstrativo,
        'PeriodoDemonstrativo': PeriodoDemonstrativo,
        'CodUnidadeValor': CodUnidadeValor,
        'DescUnidadeValor': DescUnidadeValor,
        'Moeda': Moeda,
        'DescMoeda': DescMoeda
    }

################################################################################################
#Bloco 300903 - Contas do Ativo
################################################################################################
def processaBloco300903(linha):
    CodNivelConta = str(linha[7:10]).strip()
    NumConta = str(linha[10:15]).strip()
    NomeConta = str(linha[15:40]).strip()
    ValorConta = str(linha[40:49]).strip()
    IndicBrilho = str(linha[49:50]).strip()
    
    return {
        'CodNivelConta': CodNivelConta,
        'NumConta': NumConta,
        'NomeConta': NomeConta,
        'ValorConta': ValorConta,
        'IndicBrilho': IndicBrilho
    }

################################################################################################
#Bloco 300904 - Contas do Passivo
################################################################################################
def processaBloco300904(linha):
    CodNivelConta = str(linha[7:10]).strip()
    NumConta = str(linha[10:15]).strip()
    NomeConta = str(linha[15:40]).strip()
    ValorConta = str(linha[40:49]).strip()
    IndicBrilho = str(linha[49:50]).strip()
    
    return {
        'CodNivelConta': CodNivelConta,
        'NumConta': NumConta,
        'NomeConta': NomeConta,
        'ValorConta': ValorConta,
        'IndicBrilho': IndicBrilho
    }

################################################################################################
#Bloco 300905 - Contas do Demonstrativo do Resultado
################################################################################################
def processaBloco300905(linha):
    CodNivelConta = str(linha[7:10]).strip()
    NumConta = str(linha[10:15]).strip()
    NomeConta = str(linha[15:40]).strip()
    ValorConta = str(linha[40:49]).strip()
    IndicBrilho = str(linha[49:50]).strip()
    
    return {
        'CodNivelConta': CodNivelConta,
        'NumConta': NumConta,
        'NomeConta': NomeConta,
        'ValorConta': ValorConta,
        'IndicBrilho': IndicBrilho
    }

################################################################################################
#Bloco 300906 - Índices Financeiros 
################################################################################################
def processaBloco300906(linha):
    CodCategIndices = str(linha[7:9]).strip()
    DescCategIndices = str(linha[9:44]).strip()
    CodIndice = str(linha[44:47]).strip()
    DescIndice = str(linha[47:82]).strip()
    IndiceBalanco = str(linha[82:95]).strip()
    IndicePadraoBalanco = str(linha[95:108]).strip()
    FormatoIndice = str(linha[108:109]).strip()
    QtdeCasasInt = str(linha[109:111]).strip()
    QtdeCasasDec = str(linha[111:113]).strip()
    
    return {
        'CodCategIndices': CodCategIndices,
        'DescCategIndices': DescCategIndices,
        'CodIndice': CodIndice,
        'DescIndice': DescIndice,
        'IndiceBalanco': IndiceBalanco,
        'IndicePadraoBalanco': IndicePadraoBalanco,
        'FormatoIndice': FormatoIndice,
        'QtdeCasasInt': QtdeCasasInt,
        'QtdeCasasDec': QtdeCasasDec
    }

################################################################################################
#Bloco 300907 - Conclusão
################################################################################################
def processaBloco300907(linha):
    CodCCredito = str(linha[7:11]).strip()
    DescCCredito = str(linha[11:41]).strip()
    SeqFraseCCredito = str(linha[41:45]).strip()
    FraseCCredito = str(linha[45:245]).strip()
    
    return {
        'CodCCredito': CodCCredito,
        'DescCCredito': DescCCredito,
        'SeqFraseCCredito': SeqFraseCCredito,
        'FraseCCredito': FraseCCredito
    }
