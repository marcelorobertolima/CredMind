#DadosIndiceRelacionamentoMercado_30.py
from datetime import datetime
from APICredMind.views.SERASA.mappingsSERASA import *

################################################################################################
#Bloco 301001 - Índice de Relacionamento com Mercado (IRM)
################################################################################################
def processaBloco301001(linha):
    DataAtualizacao = str(linha[7:16]).strip()
    IndiceRelMercado = str(linha[16:18]).strip()
    Mensagem = str(linha[18:118]).strip()
    
    return {
        'DataAtualizacao': DataAtualizacao,
        'IndiceRelMercado': IndiceRelMercado,
        'Mensagem': Mensagem
    }

################################################################################################
#Bloco 301099 - Índice de Relacionamento com Mercado (IRM) – Mensagem não Cálculo
################################################################################################
def processaBloco301099(linha):
    DataAtualizacao = str(linha[7:16]).strip()
    Mensagem = str(linha[16:95]).strip()
    
    return {
        'DataAtualizacao': DataAtualizacao,
        'Mensagem': Mensagem
    }

################################################################################################
#Bloco 301301 - Índice Relacionamento Mercado e Setor – Geral
################################################################################################
def processaBloco301301(linha):
    CodSetor = str(linha[7:11]).strip()
    DescSetor = buscaTipoCodSetor(str(linha[7:11]).strip())
    
    CodGrauRelac = str(linha[11:15]).strip()
    Mensagem = str(linha[15:95]).strip()
    
    return {
        'CodSetor': CodSetor,
        'DescSetor': DescSetor,
        'CodGrauRelac': CodGrauRelac,
        'Mensagem': Mensagem
    }


################################################################################################
#Bloco 301399 - Índice Relacionamento Mercado e Setor – Mensagens
################################################################################################
def processaBloco301399(linha):
    DataAtualizacao = str(linha[7:9]).strip()
    Mensagem = str(linha[9:89]).strip()
    
    return {
        'DataAtualizacao': DataAtualizacao,
        'Mensagem': Mensagem
    }
