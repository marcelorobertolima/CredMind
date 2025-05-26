#DadosAlertaIdentidadePJ_10.py
from datetime import datetime
from APICredMind.views.SERASA.mappingsSERASA import *

################################################################################################
#Bloco 110101 - Pontuação/Msg produto
#O formato abaixo é o retorno da consulta quando a pontuação for >= 3 e <= 1000 e
#meio da consulta = String – modelo NRI1
#O formato abaixo é o retorno da consulta quando a pontuação for >= 3 e <= 1000 e
#meio da consulta = String – modelo NRI2 ou NRI3
################################################################################################
def processaBloco110101(linha, modelo = ''):
    if modelo == 'NRI1':
        DataConsulta = str(linha[7:15]).strip()
        HoraConsulta = str(linha[15:23]).strip()
        MensagemProduto = str(linha[23:123]).strip()
        AreaReservada = str(linha[123:132]).strip()

        return {
            'DataConsulta' : DataConsulta,
            'HoraConsulta' : HoraConsulta,
            'MensagemProduto' : MensagemProduto,
            'AreaReservada' : AreaReservada
        }
    elif modelo == 'NRI2' or modelo == 'NRI3':
        DataConsulta = str(linha[7:15]).strip()
        HoraConsulta = str(linha[15:23]).strip()
        Pontuacao = str(linha[23:28]).strip()
        MensagemProduto = str(linha[28:128]).strip()
        VisaoSolicitada = str(linha[128:132]).strip()

        return {
            'DataConsulta' : DataConsulta,
            'HoraConsulta' : HoraConsulta,
            'Pontuacao' : Pontuacao,
            'MensagemProduto' : MensagemProduto,
            'VisaoSolicitada' : VisaoSolicitada
        }
    else:
        DataConsulta = '.'
        HoraConsulta = '.'
        Pontuacao = '.'
        MensagemProduto = '.'
        VisaoSolicitada = '.'

        return {
            'DataConsulta' : DataConsulta,
            'HoraConsulta' : HoraConsulta,
            'Pontuacao' : Pontuacao,
            'MensagemProduto' : MensagemProduto,
            'VisaoSolicitada' : VisaoSolicitada
        }

################################################################################################
#Bloco 110102 - Mensagem filtro
################################################################################################
def processaBloco110102(linha):
    DataConsulta = str(linha[7:15]).strip()
    HoraConsulta = str(linha[15:23]).strip()
    Mensagem = str(linha[23:123]).strip()

    return {
        'DataConsulta' : DataConsulta,
        'HoraConsulta' : HoraConsulta,
        'Mensagem' : Mensagem
    }

################################################################################################
#Bloco 110103 - Texto explicativo 
################################################################################################
def processaBloco110103(linha):
    DataConsulta = str(linha[7:15]).strip()
    HoraConsulta = str(linha[15:23]).strip()
    Mensagem = str(linha[23:123]).strip()

    return {
        'DataConsulta' : DataConsulta,
        'HoraConsulta' : HoraConsulta,
        'Mensagem' : Mensagem
    }

################################################################################################
#Bloco 110199 - Mensagem de não cálculo 
#O formato abaixo é o retorno da consulta quando a pontuação for >= 3 e <= 1000 e
#meio da consulta = String – modelo NRI1
#O formato abaixo é o retorno da consulta quando a pontuação for >= 3 e <= 1000 e
#meio da consulta = String – modelo NRI2 ou NRI3
################################################################################################
def processaBloco110199(linha, modelo = ''):
    if modelo == 'NRI1':
        DataConsulta = str(linha[7:15]).strip()
        HoraConsulta = str(linha[15:23]).strip()
        MensagemProduto = str(linha[23:123]).strip()
        VisaoSolicitada = str(linha[123:127]).strip()

        return {
            'DataConsulta' : DataConsulta,
            'HoraConsulta' : HoraConsulta,
            'MensagemProduto' : MensagemProduto,
            'VisaoSolicitada' : VisaoSolicitada
        }
    elif modelo == 'NRI2':
        DataConsulta = str(linha[7:15]).strip()
        HoraConsulta = str(linha[15:23]).strip()
        Pontuacao = str(linha[23:28]).strip()
        AreaReservada = str(linha[28:128]).strip()
        VisaoSolicitada = str(linha[128:132]).strip()

        return {
            'DataConsulta' : DataConsulta,
            'HoraConsulta' : HoraConsulta,
            'Pontuacao' : Pontuacao,
            'AreaReservada' : AreaReservada,
            'VisaoSolicitada' : VisaoSolicitada
        }
    elif modelo == 'NRI3':
        DataConsulta = str(linha[7:15]).strip()
        HoraConsulta = str(linha[15:23]).strip()
        Pontuacao = str(linha[23:28]).strip()

        return {
            'DataConsulta' : DataConsulta,
            'HoraConsulta' : HoraConsulta,
            'Pontuacao' : Pontuacao
        }
    else:
        DataConsulta = '.'
        HoraConsulta = '.'
        Pontuacao = '.'
        MensagemProduto = '.'
        VisaoSolicitada = '.'

        return {
            'DataConsulta' : DataConsulta,
            'HoraConsulta' : HoraConsulta,
            'Pontuacao' : Pontuacao,
            'MensagemProduto' : MensagemProduto,
            'VisaoSolicitada' : VisaoSolicitada
        }
