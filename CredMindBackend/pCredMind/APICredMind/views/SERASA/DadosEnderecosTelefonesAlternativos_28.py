#DadosEnderecosTelefonesAlternativos_28.py
from datetime import datetime
from APICredMind.views.SERASA.mappingsSERASA import *

################################################################################################
#Bloco 280101 - Endereços e Telefones alternativos – Endereços – Parte 1
################################################################################################
def processaBloco280101(linha):
    DataInf = str(linha[7:15]).strip()
    TipoLogradouro = str(linha[15:25]).strip()
    TituloLogradouro = str(linha[25:35]).strip()
    NomeLogradouro = str(linha[35:95]).strip()
    NumLogradouro = str(linha[95:105]).strip()
    ComplLogradourdo = str(linha[105:145]).strip()
    AreaReservada = str(linha[145:146]).strip()
    
    return {
        'DataInf': DataInf,
        'TipoLogradouro': TipoLogradouro,
        'TituloLogradouro': TituloLogradouro,
        'NomeLogradouro': NomeLogradouro,
        'NumLogradouro': NumLogradouro,
        'ComplLogradourdo': ComplLogradourdo,
        'AreaReservada': AreaReservada
    }

################################################################################################
#Bloco 280102 - Endereços e Telefones alternativos – Endereços – Parte 2
################################################################################################
def processaBloco280102(linha):
    Bairro = str(linha[7:77]).strip()
    Cidade = str(linha[77:147]).strip()
    UF = str(linha[147:149]).strip() 
    CEP = str(linha[149:157]).strip()
    
    return {
        'Bairro': Bairro,
        'Cidade': Cidade,
        'UF': UF,
        'CEP': CEP
    }

################################################################################################
#Bloco 280199 - Endereços e Telefones alternativos – Endereços – Mensagens
################################################################################################
def processaBloco280199(linha):
    DataConsulta = str(linha[7:15]).strip()
    HoraConsulta = str(linha[15:23]).strip()
    Mensagem = str(linha[23:123]).strip() 
    
    return {
        'DataConsulta': DataConsulta,
        'HoraConsulta': HoraConsulta,
        'Mensagem': Mensagem
    }

################################################################################################
#Bloco 290101 - Endereços e Telefones alternativos – Telefones
################################################################################################
def processaBloco290101(linha):
    DataConsulta = str(linha[7:15]).strip()
    NumDDD = str(linha[15:19]).strip()
    NumTelefone = str(linha[19:29]).strip()
    AreaReservada = str(linha[29:30]).strip()
    
    return {
        'DataConsulta': DataConsulta,
        'NumDDD': NumDDD,
        'NumTelefone': NumTelefone,
        'AreaReservada': AreaReservada
    }

################################################################################################
#Bloco 290199 - Endereços e Telefones alternativos – Telefones – Mensagens
################################################################################################
def processaBloco290199(linha):
    DataConsulta = str(linha[7:15]).strip()
    HoraConsulta = str(linha[15:23]).strip()
    Mensagem = str(linha[23:123]).strip() 
    AreaReservada = str(linha[123:146]).strip()
    
    return {
        'DataConsulta': DataConsulta,
        'HoraConsulta': HoraConsulta,
        'Mensagem': Mensagem,
        'AreaReservada': AreaReservada
    }
