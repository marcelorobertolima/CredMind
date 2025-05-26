#DadosConsultaAlertas_04.py
from datetime import datetime
from APICredMind.views.SERASA.mappingsSERASA import *

################################################################################################
#Bloco 990000 - Layout Formatado – Consulta Relato
################################################################################################
def processaBloco990000(linha):
    CNPJEmpresa = str(linha[7:16]).strip()
    RazaoSocial = str(linha[16:86]).strip()
    AreaReservada = str(linha[86:131]).strip()

    return {
        'CNPJEmpresa' : CNPJEmpresa,
        'RazaoSocial' : RazaoSocial,
        'AreaReservada' : AreaReservada
    }

################################################################################################
#Bloco 990101 - Layout Formatado – Consulta Relato 
################################################################################################
def processaBloco990101(linha):
    LinhaEditadaProduto = str(linha[7:86]).strip()
    AreaReservada = str(linha[86:97]).strip()
    
    CodTipoRegistro = str(linha[97:98]).strip()
    DescTipoRegistro = buscaTipoRegistroLayout(str(linha[97:98]).strip())
    
    CodTipoLinha = str(linha[98:99]).strip()
    DescTipoLinha = buscaTipoLinhaLayout(str(linha[98:99]).strip())

    CodAtributo = str(linha[99:100]).strip()
    DescAtributo = buscaTipoAtributoLayout(str(linha[99:100]).strip())

    Conjunto = str(linha[100:102]).strip()
    Menu = str(linha[102:103]).strip()
    Pagina = str(linha[103:105]).strip()
    AreaReservada2 = str(linha[105:107]).strip()
    NomeBloco = str(linha[107:131]).strip()

    return {
        'LinhaEditadaProduto' : LinhaEditadaProduto,
        'AreaReservada' : AreaReservada,
        'CodTipoRegistro' : CodTipoRegistro,
        'DescTipoRegistro' : DescTipoRegistro,
        'CodTipoLinha' : CodTipoLinha,
        'DescTipoLinha' : DescTipoLinha,
        'CodAtributo' : CodAtributo,
        'DescAtributo' : DescAtributo,
        'Conjunto' : Conjunto,
        'Menu' : Menu,
        'Pagina' : Pagina,
        'AreaReservada2' : AreaReservada2,
        'NomeBloco' : NomeBloco
    }
