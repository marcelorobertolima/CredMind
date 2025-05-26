#DadosSociosAdministradoresSPC_92.py
from datetime import datetime
from APICredMind.views.SERASA.mappingsSERASA import *

################################################################################################
#Bloco 920001 - Quantidade de anotações e anotações mais recente 
################################################################################################
def processaBloco920001(linha):
    CodTipoPessoaSocio = str(linha[7:8]).strip()
    DescTipoPessoaSocio = buscaTipoPessoa(str(linha[7:8]).strip())

    NumDctoSocio = str(linha[8:17]).strip()
    FilialDctoSocio = str(linha[17:21]).strip()
    DigDctoSocio = str(linha[21:23]).strip()
    SeqSocio = str(linha[23:27]).strip()
    SocioOuAdmin = str(linha[27:28]).strip()
    NomeRazaoSocio = str(linha[28:98]).strip()
    QtdeTotalAnotacoes = str(linha[98:108]).strip()
    ValorTotalAnotacoes = str(linha[108:125]).strip()
    DataAnotacaoMaisRecente = str(linha[125:133]).strip()

    CodSocioConsistido = str(linha[133:134]).strip()
    DescSocioConsistido = buscaStatusSocioConstituido(str(linha[133:134]).strip())
    
    return {
        'CodTipoPessoaSocio': CodTipoPessoaSocio,
        'DescTipoPessoaSocio': DescTipoPessoaSocio,
        'NumDctoSocio': NumDctoSocio,
        'FilialDctoSocio': FilialDctoSocio,
        'DigDctoSocio': DigDctoSocio,
        'SeqSocio': SeqSocio,
        'SocioOuAdmin': SocioOuAdmin,
        'NomeRazaoSocio': NomeRazaoSocio,
        'QtdeTotalAnotacoes': QtdeTotalAnotacoes,
        'ValorToalAnotacoes': ValorTotalAnotacoes,
        'DataAnotacaoMaisRecente': DataAnotacaoMaisRecente,
        'CodSocioConsistido': CodSocioConsistido,
        'DescSocioConsistido': DescSocioConsistido
    }

################################################################################################
#Bloco 920002 - Dados da Anotação (Podem retornar até 5 anotações por sócio)
################################################################################################
def processaBloco920002(linha):
    DataInclusaoAnotacao = str(linha[7:15]).strip()
    DataVencimentoAnotacao = str(linha[15:23]).strip()
    NumContrato = str(linha[23:53]).strip()
    
    CodTipoOperacao = str(linha[53:54]).strip()
    DescTipoOperacao = buscaTipoTipoOperacao(str(linha[53:54]).strip())
    
    ValorAnotacao = str(linha[54:71]).strip()
    NomeCidade = str(linha[71:101]).strip()
    UF = str(linha[101:103]).strip()
    NomeAssociadoCredor = str(linha[103:173]).strip()
    OrigemAnotacao = str(linha[173:203]).strip()
    
    return {
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
#Bloco 920099 - Mensagem de indisponibilidade da informação
################################################################################################
def processaBloco920099(linha):
    MsgInformIndisp = str(linha[7:87]).strip()
    
    return {
        'MsgInformIndisp': MsgInformIndisp
    }