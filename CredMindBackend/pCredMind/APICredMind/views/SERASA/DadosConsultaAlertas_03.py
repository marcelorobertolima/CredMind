#DadosConsultaAlertas_04.py
from datetime import datetime
from APICredMind.views.SERASA.mappingsSERASA import *

################################################################################################
#Bloco 030101 - Consultas à Serasa
################################################################################################
def processaBloco030101(linha):
    AnoConsulta = str(linha[7:9]).strip()
    MesConsulta = str(linha[9:11]).strip()
    DescMesConsulta = str(linha[11:14]).strip()
    QtdeConsultasPorEmpresa = str(linha[14:17]).strip()
    QtdeConsultasPorEmpresaBanco = str(linha[17:20]).strip()
    
    CodTipoEmpresa = str(linha[20:21]).strip()
    DescTipoEmpresa = buscaTipoEmpresa(str(linha[20:21]).strip())
    
    AreaReservada = str(linha[21:36])

    return {
        'AnoConsulta' : AnoConsulta,
        'MesConsulta' : MesConsulta,
        'DescMesConsulta' : DescMesConsulta,
        'QtdeConsultasPorEmpresa' : QtdeConsultasPorEmpresa,
        'QtdeConsultasPorEmpresaBanco' : QtdeConsultasPorEmpresaBanco,
        'CodTipoEmpresa' : CodTipoEmpresa,
        'DescTipoEmpresa' : DescTipoEmpresa,
        'AreaReservada' : AreaReservada
    }

################################################################################################
#Bloco 030102 - Últimas Consultas 
################################################################################################
def processaBloco030102(linha):
    DataConsulta = str(linha[7:15]).strip()
    NomeConsultante = str(linha[15:50]).strip()
    QtdeConsultasDiaCliente = str(linha[50:54]).strip()
    CNPJConsultante = str(linha[54:63]).strip()
    AreaReservada = str(linha[63:64]).strip()
    AreaReservada2 = str(linha[64:65]).strip()

    return {
        'DataConsulta' : DataConsulta,
        'NomeConsultante' : NomeConsultante,
        'QtdeConsultasDiaCliente' : QtdeConsultasDiaCliente,
        'CNPJConsultante' : CNPJConsultante,
        'AreaReservada' : AreaReservada,
        'AreaReservada2' : AreaReservada2
    }

################################################################################################
#Bloco 030103 - Frase de Alerta
################################################################################################
def processaBloco030103(linha):
    FraseAlerta = str(linha[7:131]).strip()
    DataAltera = str(linha[131:139]).strip()
    AreaReservada = str(linha[139:159]).strip()

    return {
        'FraseAlerta' : FraseAlerta,
        'DataAltera' : DataAltera,
        'AreaReservada' : AreaReservada
    }

################################################################################################
#Bloco 030201 - Informações de participantes com alerta
################################################################################################
def processaBloco030201(linha):
    NomeParticipante = str(linha[7:72]).strip()
    DctoParticipante = str(linha[72:83]).strip()
    
    CodTipoPessoaParticipante = str(linha[83:84]).strip()
    DescTipoPessoaParticipante = buscaTipoPessoa(str(linha[83:84]).strip())

    return {
        'NomeParticipante' : NomeParticipante,
        'DctoParticipante' : DctoParticipante,
        'TipoPessoaParticipante' : CodTipoPessoaParticipante,
        'DescTipoPessoaParticipante': DescTipoPessoaParticipante
    }

################################################################################################
#Bloco 030301 - Consultas à Serasa – Sintético - SETOR
################################################################################################
def processaBloco030301(linha):
    CodSetor = str(linha[7:11]).strip()
    DescSetor = str(linha[11:36]).strip()
    DataConsulta = str(linha[36:44]).strip()
    QtdeConsultas = str(linha[44:52]).strip()
    
    CodTipoConsulta = str(linha[52:53]).strip()
    DescTipoConsulta = buscaTipoConsulta(str(linha[52:53]).strip())

    return {
        'CodSetor' : CodSetor,
        'DescSetor' : DescSetor,
        'DataConsulta' : DataConsulta,
        'QtdeConsultas': QtdeConsultas,
        'CodTipoConsulta': CodTipoConsulta,
        'DescTipoConsulta': DescTipoConsulta
    }

################################################################################################
#Bloco 030302 - Consultas à Serasa – Sintético - SEGMENTO
################################################################################################
def processaBloco030302(linha):
    CodSegmento = str(linha[7:11]).strip()
    DescSegmento = str(linha[11:36]).strip()
    DataConsulta = str(linha[36:44]).strip()
    QtdeConsultas = str(linha[44:52]).strip()
    
    CodTipoConsulta = str(linha[52:53]).strip()
    DescTipoConsulta = buscaTipoConsulta(str(linha[52:53]).strip())

    return {
        'CodSegmento' : CodSegmento,
        'DescSegmento' : DescSegmento,
        'DataConsulta' : DataConsulta,
        'QtdeConsultas': QtdeConsultas,
        'CodTipoConsulta': CodTipoConsulta,
        'DescTipoConsulta': DescTipoConsulta
    }

################################################################################################
#Bloco 030303  - Últimas Consultas à Serasa - MERCADO
################################################################################################
def processaBloco030303(linha):
    CodMercado = str(linha[7:11]).strip()
    DescMercado = str(linha[11:36]).strip()
    DataConsulta = str(linha[36:44]).strip()
    CNPJConsultante = str(linha[44:52]).strip()
    FilialCNPJConsultante = str(linha[52:56]).strip()
    DigCNPJConsultante = str(linha[56:58]).strip()
    RazaoSocialConsultante = str(linha[58:128]).strip()
    QtdeConsultas = str(linha[128:136]).strip()
    
    CodTipoConsulta = str(linha[136:137]).strip()
    DescTipoConsulta = buscaTipoConsulta(str(linha[136:137]).strip())

    return {
        'CodMercado' : CodMercado,
        'DescMercado' : DescMercado,
        'DataConsulta' : DataConsulta,
        'CNPJConsultante': CNPJConsultante,
        'FilialCNPJConsultante': FilialCNPJConsultante,
        'DigCNPJConsultante': DigCNPJConsultante,
        'RazaoSocialConsultante': RazaoSocialConsultante,
        'QtdeConsultas': QtdeConsultas,
        'CodTipoConsulta': CodTipoConsulta,
        'DescTipoConsulta': DescTipoConsulta
    }

################################################################################################
#Bloco 030304  - Últimas Consultas à Serasa - SEGMENTO
################################################################################################
def processaBloco030304(linha):
    CodSegmento = str(linha[7:11]).strip()
    DescSegmento = str(linha[11:36]).strip()
    DataConsulta = str(linha[36:44]).strip()
    CNPJConsultante = str(linha[44:52]).strip()
    FilialCNPJConsultante = str(linha[52:56]).strip()
    DigCNPJConsultante = str(linha[56:58]).strip()
    RazaoSocialConsultante = str(linha[58:128]).strip()
    QtdeConsultas = str(linha[128:136]).strip()
    
    CodTipoConsulta = str(linha[136:137]).strip()
    DescTipoConsulta = buscaTipoConsulta(str(linha[136:137]).strip())

    return {
        'CodSegmento' : CodSegmento,
        'DescSegmento' : DescSegmento,
        'DataConsulta' : DataConsulta,
        'CNPJConsultante': CNPJConsultante,
        'FilialCNPJConsultante': FilialCNPJConsultante,
        'DigCNPJConsultante': DigCNPJConsultante,
        'RazaoSocialConsultante': RazaoSocialConsultante,
        'QtdeConsultas': QtdeConsultas,
        'CodTipoConsulta': CodTipoConsulta,
        'DescTipoConsulta': DescTipoConsulta
    }

################################################################################################
#Bloco 030399 - Informações Gerais - Data de atualização 
################################################################################################
def processaBloco030399(linha):
    DataAtualizacao = str(linha[7:17]).strip()
    AreaReservada = str(linha[17:146]).strip()

    return {
        'DataAtualizacao' : DataAtualizacao,
        'AreaReservada' : AreaReservada
    }
