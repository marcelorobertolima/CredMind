#DadosAnotacoesConsultasSPCSociosAdministradores_92.py
from datetime import datetime
from APICredMind.views.SERASA.mappingsSERASA import *

################################################################################################
#Bloco 925001 - Quantidade de anotações e anotação mais recente
################################################################################################
def processaBloco925001(linha):
    SeqSocio = str(linha[7:11]).strip()

    CodTipoPessoaSocio = str(linha[11:12]).strip()
    DescTipoPessoaSocio = buscaTipoPessoa(str(linha[11:12]).strip())

    NumDctoSocio = str(linha[12:21]).strip()
    FilialDctoSocio = str(linha[21:25]).strip()
    DigDctoSocio = str(linha[25:27]).strip()
    SeqSocio2 = str(linha[27:31]).strip()
    SocioOuAdmin = str(linha[31:32]).strip()
    NomeRazaoSocio = str(linha[32:102]).strip()
    QtdeTotalAnotacoes = str(linha[102:112]).strip()
    ValorTotalAnotacoes = str(linha[112:129]).strip()
    DataAnotacaoMaisRecente = str(linha[129:137]).strip()

    CodSocioConsistido = str(linha[137:138]).strip()
    DescSocioConsistido = buscaStatusSocioConstituido(str(linha[137:138]).strip())
    
    return {
        'SeqSocio': SeqSocio,
        'CodTipoPessoaSocio': CodTipoPessoaSocio,
        'DescTipoPessoaSocio': DescTipoPessoaSocio,
        'NumDctoSocio': NumDctoSocio,
        'FilialDctoSocio': FilialDctoSocio,
        'DigDctoSocio': DigDctoSocio,
        'SeqSocio2': SeqSocio2,
        'SocioOuAdmin': SocioOuAdmin,
        'NomeRazaoSocio': NomeRazaoSocio,
        'QtdeTotalAnotacoes': QtdeTotalAnotacoes,
        'ValorToalAnotacoes': ValorTotalAnotacoes,
        'DataAnotacaoMaisRecente': DataAnotacaoMaisRecente,
        'CodSocioConsistido': CodSocioConsistido,
        'DescSocioConsistido': DescSocioConsistido
    }

################################################################################################
#Bloco 925002 - Dados da anotação (Podem retornar até 5 anotações por sócio) 
################################################################################################
def processaBloco925002(linha):
    SeqSocio = str(linha[7:11]).strip()
    DataInclusaoAnotacao = str(linha[11:19]).strip()
    DataVencimentoAnotacao = str(linha[19:27]).strip()
    NumContrato = str(linha[27:57]).strip()
    
    CodTipoOperacao = str(linha[57:58]).strip()
    DescTipoOperacao = buscaTipoTipoOperacao(str(linha[57:58]).strip())
    
    ValorAnotacao = str(linha[58:75]).strip()
    NomeCidade = str(linha[75:105]).strip()
    UF = str(linha[105:107]).strip()
    NomeAssociadoCredor = str(linha[107:177]).strip()
    OrigemAnotacao = str(linha[177:207]).strip()
    
    return {
        'SeqSocio': SeqSocio,
        'DataInclusaoAnotacao': DataInclusaoAnotacao,
        'DataVencimentoAnotacao': DataVencimentoAnotacao,
        'NumContrato': NumContrato,
        'CodTipoOperacao': CodTipoOperacao,
        'DescTipoOperacao': DescTipoOperacao,
        'ValorAnotacao': ValorAnotacao,
        'NomeCidade': NomeCidade,
        'UF': UF,
        'NomeAssociadoCredor': NomeAssociadoCredor,
        'OrigemAnotacao': OrigemAnotacao
    }

################################################################################################
#Bloco 925099 - Mensagem de indisponibilidade da informação
################################################################################################
def processaBloco925099(linha):
    SeqSocio = str(linha[7:11]).strip()
    MsgInformIndisp = str(linha[11:91]).strip()
    
    return {
        'SeqSocio': SeqSocio,
        'MsgInformIndisp': MsgInformIndisp
    }

################################################################################################
#Bloco 926001 - Quantidade de anotações e anotação mais recente
################################################################################################
def processaBloco926001(linha):
    SeqSocio = str(linha[7:11]).strip()

    CodTipoPessoaSocio = str(linha[11:12]).strip()
    DescTipoPessoaSocio = buscaTipoPessoa(str(linha[11:12]).strip())

    NumDctoSocio = str(linha[12:21]).strip()
    FilialDctoSocio = str(linha[21:25]).strip()
    DigDctoSocio = str(linha[25:27]).strip()
    SeqSocio2 = str(linha[27:31]).strip()
    SocioOuAdmin = str(linha[31:32]).strip()
    NomeRazaoSocio = str(linha[32:102]).strip()
    QtdeConsultas = str(linha[102:108]).strip()

    CodSocioConsistido = str(linha[108:109]).strip()
    DescSocioConsistido = buscaStatusSocioConstituido(str(linha[108:109]).strip())
    
    return {
        'SeqSocio': SeqSocio,
        'CodTipoPessoaSocio': CodTipoPessoaSocio,
        'DescTipoPessoaSocio': DescTipoPessoaSocio,
        'NumDctoSocio': NumDctoSocio,
        'FilialDctoSocio': FilialDctoSocio,
        'DigDctoSocio': DigDctoSocio,
        'SeqSocio2': SeqSocio2,
        'SocioOuAdmin': SocioOuAdmin,
        'NomeRazaoSocio': NomeRazaoSocio,
        'QtdeConsultas': QtdeConsultas,
        'CodSocioConsistido': CodSocioConsistido,
        'DescSocioConsistido': DescSocioConsistido
    }

################################################################################################
#Bloco 926002 - Informações do SPC – Consultas ao SPC
################################################################################################
def processaBloco926002(linha):
    SeqSocio = str(linha[7:11]).strip()
    DataConsulta = str(linha[11:19]).strip()
    NomeAssociado = str(linha[19:79]).strip()
    QtdeConsultas = str(linha[79:83]).strip()
    
    return {
        'SeqSocio': SeqSocio,
        'DataConsulta': DataConsulta,
        'NomeAssociado': NomeAssociado,
        'QtdeConsultas': QtdeConsultas
    }

################################################################################################
#Bloco 926003 - Informações do SPC – Totais de Consultas por mês
################################################################################################
def processaBloco926003(linha):
    SeqSocio = str(linha[7:11]).strip()
    AnoConsulta = str(linha[11:13]).strip()
    MesConsulta = str(linha[13:15]).strip()
    DescMesConsulta = str(linha[15:18]).strip()
    QtdeConsultas = str(linha[18:21]).strip()
    
    return {
        'SeqSocio': SeqSocio,
        'AnoConsulta': AnoConsulta,
        'MesConsulta': MesConsulta,
        'DescMesConsulta': DescMesConsulta,
        'QtdeConsultas': QtdeConsultas
    }

################################################################################################
#Bloco 926099 - Informações do SPC – Mensagens do Consultas ao SPC
################################################################################################
def processaBloco926099(linha):
    SeqSocio = str(linha[7:11]).strip()
    Mensagem = str(linha[11:91]).strip()
    
    return {
        'SeqSocio': SeqSocio,
        'Mensagem': Mensagem
    }
