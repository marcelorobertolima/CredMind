#DadosVendaCartao_70.py
from datetime import datetime
from APICredMind.views.SERASA.mappingsSERASA import *

################################################################################################
#Bloco 700001 - Vendas com Cartão – Dados da Empresa
################################################################################################
def processaBloco700001(linha):
    DataAtualizacao = str(linha[7:17]).strip()
    CNPJ = str(linha[17:31]).strip()
    RazaoSocial = str(linha[31:101]).strip()
    NomeFantasia = str(linha[101:161]).strip()
    DataPrimTransCartao = str(linha[161:171]).strip()
    PeriodoTrans = str(linha[171:201]).strip()
    Endereco = str(linha[201:271]).strip()
    
    return {
        'DataAtualizacao': DataAtualizacao,
        'CNPJ': CNPJ,
        'RazaoSocial': RazaoSocial,
        'NomeFantasia': NomeFantasia,
        'DataPrimTransCartao': DataPrimTransCartao,
        'PeriodoTrans': PeriodoTrans,
        'Endereco': Endereco
    }

################################################################################################
#Bloco 700002 - Vendas com Cartão – Dados da Empresa Continuação
################################################################################################
def processaBloco700002(linha):
    Cidade = str(linha[7:37]).strip()
    UF = str(linha[37:39]).strip()
    CEP = str(linha[39:48]).strip()
    Segmento = str(linha[48:108]).strip()
    Rede = str(linha[108:168]).strip()
    CanalPrincipal = str(linha[168:198]).strip()
    Telefone = str(linha[198:211]).strip()
    
    return {
        'Cidade': Cidade,
        'UF': UF,
        'CEP': CEP,
        'Segmento': Segmento,
        'Rede': Rede,
        'CanalPrincipal': CanalPrincipal,
        'Telefone': Telefone
    }

################################################################################################
#Bloco 700003 - Vendas com Cartão – Faixa de Utilização
################################################################################################
def processaBloco700003(linha):
    DiaSemana = str(linha[7:10]).strip()
    FaixaDas0000as0600 = str(linha[10:11]).strip()
    FaixaDas0601as1200 = str(linha[11:12]).strip()
    FaixaDas1201as1800 = str(linha[12:13]).strip()
    FaixaDas1801as2200 = str(linha[13:14]).strip()
    FaixaDas2201as2359 = str(linha[14:15]).strip()
    
    return {
        'DiaSemana': DiaSemana,
        'FaixaDas0000as0600': FaixaDas0000as0600,
        'FaixaDas0601as1200': FaixaDas0601as1200,
        'FaixaDas1201as1800': FaixaDas1201as1800,
        'FaixaDas1801as2200': FaixaDas1801as2200,
        'FaixaDas2201as2359': FaixaDas2201as2359
    }

################################################################################################
#Bloco 700099 - Vendas com Cartão – Mensagens
################################################################################################
def processaBloco700099(linha):
    CodMsgRetorno = str(linha[7:10]).strip()
    Mensagem = str(linha[10:90]).strip()
    
    return {
        'CodMsgRetorno': CodMsgRetorno,
        'Mensagem': Mensagem
    }
