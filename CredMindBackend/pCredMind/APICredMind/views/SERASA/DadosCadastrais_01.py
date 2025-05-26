#SERASADadosCadastrais_01.py
from datetime import datetime
from APICredMind.views.SERASA.mappingsSERASA import *

################################################################################################
#Bloco 010000 - Dados de Controle da Empresa Consultada
################################################################################################
def processaBloco010000(linha):
    CodSituacaoEmpresaAntiga = str(linha[7:9]).strip()
    DescSituacaoEmpresaAntiga = buscaSituacaoEmpresaANTIGA(linha[7:9]).strip()
    DescSituacaoEmpresaAntigaSERASA = str(linha[9:88]).strip()
    CodCNPJConsultado = str(linha[88:97]).strip()
    IdentTemFicha = str(linha[97:98]).strip()
    TransacaoContabilizada = str(linha[98:102]).strip()
    CodMsgReciprocidade = str(linha[102:103]).strip()
    DescMsgReciprocidade = buscaMensagemReciprocidade(linha[102:103]).strip()
    DataUltimaRemessaReciprocidade = str(linha[103:113]).strip()
    TransacaoContDesmembrada02 = str(linha[113:117]).strip()
    TransacaoContDesmembrada03 = str(linha[117:121]).strip()
    TransacaoContDesmembrada04 = str(linha[121:125]).strip()
    TransacaoContDesmembrada05 = str(linha[125:129]).strip()
    TransacaoContDesmembrada06 = str(linha[129:133]).strip()
    TransacaoContDesmembrada07 = str(linha[133:137]).strip()
    TransacaoContDesmembrada08 = str(linha[137:141]).strip()
    TransacaoContDesmembrada09 = str(linha[141:145]).strip()
    TransacaoContDesmembrada10 = str(linha[145:149]).strip()
    TipoRelato = str(linha[149:150]).strip()
    DescTipoRelato = buscaTipoRelato(linha[149:150]).strip()
    TemReciprocidade = str(linha[150:151]).strip()
    TipoRelCob = str(linha[151:152]).strip()
    DescTipoRelCob = buscaTipoRelCob(linha[151:152]).strip()
    DiasRestantesVisaoAnaliticaAuto = str(linha[152:154]).strip()
    CodSituacaoEmpresaNova = str(linha[154:155]).strip()
    DescSituacaoEmpresaNova = buscaSituacaoEmpresaNova(linha[154:155]).strip()
    DescSituacaoEmpresaSERASA = str(linha[155:235]).strip().strip()
    DataAvisoPrevio = str(linha[235:245]).strip()
    TemProtesteIndisp = str(linha[245:246]).strip()

    return {
        'CodSituacaoEmpresaAntiga' : CodSituacaoEmpresaAntiga,
        'DescSituacaoEmpresaAntiga' : DescSituacaoEmpresaAntiga,
        'DescSituacaoEmpresaAntigaSERASA' : DescSituacaoEmpresaAntigaSERASA,
        'CodCNPJConsultado' : CodCNPJConsultado,
        'IdentTemFicha' : IdentTemFicha,
        'TransacaoContabilizada' :TransacaoContabilizada,
        'CodMsgReciprocidade' : CodMsgReciprocidade,
        'DescMsgReciprocidade': DescMsgReciprocidade,
        'DataUltimaRemessaReciprocidade' : DataUltimaRemessaReciprocidade,
        'TransacaoContDesmembrada02' : TransacaoContDesmembrada02,
        'TransacaoContDesmembrada03' : TransacaoContDesmembrada03,
        'TransacaoContDesmembrada04' : TransacaoContDesmembrada04,
        'TransacaoContDesmembrada05' : TransacaoContDesmembrada05,
        'TransacaoContDesmembrada06' : TransacaoContDesmembrada06,
        'TransacaoContDesmembrada07' : TransacaoContDesmembrada07,
        'TransacaoContDesmembrada08' : TransacaoContDesmembrada08,
        'TransacaoContDesmembrada09' : TransacaoContDesmembrada09,
        'TransacaoContDesmembrada10' : TransacaoContDesmembrada10,
        'TipoRelato' : TipoRelato,
        'DescTipoRelato' : DescTipoRelato,
        'TemReciprocidade' : TemReciprocidade,
        'TipoRelatorioCob' : TipoRelCob,
        'DescTipoRelCob' : DescTipoRelCob,
        'DiasRestantesVisaoAnaliticaAuto' : DiasRestantesVisaoAnaliticaAuto,
        'CodSituacaoEmpresaNova' : CodSituacaoEmpresaNova,
        'DescSituacaoEmpresaNova' : DescSituacaoEmpresaNova,
        'DescSituacaoEmpresaSERASA' : DescSituacaoEmpresaSERASA,
        'DataAvisoPrevio' : DataAvisoPrevio,
        'TemProtesteIndisp' : TemProtesteIndisp
    }

################################################################################################
#Bloco 010100 - Frase status da empresa
################################################################################################
def processaBloco010100(linha):
    MensagemEmpresa = str(linha[7:79]).strip()
    
    return {
        'MensagemEmpresa': MensagemEmpresa
    }

################################################################################################
#Bloco 010101 - Contabilizacao
################################################################################################
def processaBloco010101(linha):
    ConfidencialPara = str(linha[7:67]).strip()
    DataContabilizacaoConsulta = str(linha[67:75]).strip()
    HoraContabilizacaoConsulta = str(linha[75:83]).strip()
    AreaReservada = str(linha[83:85]).strip()
    CNPJEditado = str(linha[85:109]).strip()
    DataUltimaConsultaBloco = str(linha[109:117]).strip()
    OrigemDados = str(linha[117:118]).strip()
    NumeroUltiRegOrgaosOficiais = str(linha[118:129]).strip()
    DataultimoRegOraosOficiais = str(linha[129:137]).strip()
    
    return {
        'ConfidencialPara' : ConfidencialPara,
        'DataContabilizacaoConsulta' : DataContabilizacaoConsulta,
        'HoraContabilizacaoConsulta' : HoraContabilizacaoConsulta,
        'AreaReservada' : AreaReservada,
        'CNPJEditado' : CNPJEditado,
        'DataUltimaConsultaBloco' : DataUltimaConsultaBloco,
        'OrigemDados' : OrigemDados,
        'NumeroUltiRegOrgaosOficiais' : NumeroUltiRegOrgaosOficiais,
        'DataultimoRegOraosOficiais' : DataultimoRegOraosOficiais
    }

################################################################################################
#Bloco 010102 - Identificação
################################################################################################
def processaBloco010102(linha):
    RazaoSocial = str(linha[7:77]).strip()
    CNPJEmpresa = str(linha[77:86]).strip()
    NomeFatasia = str(linha[86:146]).strip()
    NIRE = str(linha[146:157]).strip()
    TipoSociedade = str(linha[157:217]).strip()
    OpcaoTributaria = str(linha[217:247]).strip()
    CodNaturezaJuridica = str(linha[247:251]).strip()
    
    return {
        'RazaoSocial' : RazaoSocial,
        'CNPJEmpresa' : CNPJEmpresa,
        'NomeFatasia' : NomeFatasia,
        'NIRE' : NIRE,
        'TipoSociedade' : TipoSociedade,
        'OpcaoTributaria' : OpcaoTributaria,
        'CodNaturezaJuridica' : CodNaturezaJuridica
    }

################################################################################################
#Bloco 010103 - Endereço
################################################################################################
def processaBloco010103(linha):
    EnderecoCompleto = str(linha[7:77]).strip()
    Bairro = str(linha[77:107]).strip()
    Endereco = str(linha[107:187]).strip()
    
    return {
        'EnderecoCompleto' : EnderecoCompleto,
        'Bairro' : Bairro,
        'Endereco' : Endereco
    }

################################################################################################
#Bloco 010104 - Localizacao
################################################################################################
def processaBloco010104(linha):
    Cidade = str(linha[7:37]).strip()
    UF = str(linha[37:39]).strip()
    CEP = str(linha[39:48]).strip()
    DDD = str(linha[48:52]).strip()
    NumTelefone = str(linha[52:61]).strip()
    NumFAX = str(linha[61:70]).strip()
    AreaReservada = str(linha[70:74]).strip()
    Site = str(linha[74:144]).strip()
    Email = str(linha[144:214]).strip()
    
    return {
        'Cidade' : Cidade,
        'UF' : UF,
        'CEP' : CEP,
        'DDD' : DDD,
        'NumTelefone' : NumTelefone,
        'NumFAX' : NumFAX,
        'AreaReservada' : AreaReservada,
        'Site' : Site,
        'Email' : Email
    }

################################################################################################
#Bloco 010105 - Atividade
################################################################################################
def processaBloco010105(linha):
    DataFundacaoSERASA = str(linha[7:15]).strip()
    
    if DataFundacaoSERASA == '00000000':
        DataFundacao = ''
    else:
        DataFundacaoAux = datetime.strptime(DataFundacaoSERASA, "%Y%m%d")
        DataFundacao = DataFundacaoAux.strftime("%d/%m/%Y")
    
    DataInscricaoCNPJSERASA = str(linha[15:23]).strip()
    DataInscricaoCNPJSERASAAux = datetime.strptime(DataInscricaoCNPJSERASA, "%Y%m%d")
    DataInscricaoCNPJ = DataInscricaoCNPJSERASAAux.strftime("%d/%m/%Y")
    
    RamoAtividade = str(linha[23:77]).strip()
    CodigoSERASACompleto = str(linha[77:84]).strip()
    QtdeFuncionarios = str(linha[84:89]).strip()
    PercentualCompra = str(linha[89:92]).strip()
    PercentualVendas = str(linha[92:95]).strip()
    NumeroFiliais = str(linha[95:98]).strip()
    NumeroFiliais2 = str(linha[98:104]).strip()
    CNAE = str(linha[104:111]).strip()
    DataUltManutTVCG = str(linha[111:119]).strip()
    
    return {
        'DataFundacao': DataFundacao,
        'DataInscricaoCNPJ': DataInscricaoCNPJ,
        'RamoAtividade': RamoAtividade,
        'CosigoSERASACompleto' : CodigoSERASACompleto,
        'QtdeFuncionarios': QtdeFuncionarios,
        'PercentualCompra': PercentualCompra,
        'PercentualVendas': PercentualVendas,
        'NumeroFiliais': NumeroFiliais,
        'NumeroFiliais2': NumeroFiliais2,
        'CNAE': CNAE,
        'DataUltManutTVCG': DataUltManutTVCG
    }

################################################################################################
#Bloco 010106 - Filiais
################################################################################################
def processaBloco010106(linha):
    NomeFilial = str(linha[7:37]).strip()
    CodEmbratel = str(linha[37:41]).strip()
    
    return {
        'NomeFilial' : NomeFilial,
        'CodEmbratel' : CodEmbratel
    }

################################################################################################
#Bloco 010107 - Principais Produtos
################################################################################################
def processaBloco010107(linha):
    PrincipaisProdutos = str(linha[7:67]).strip()
    
    return {
        'PrincipaisProdutos' : PrincipaisProdutos
    }

################################################################################################
#Bloco 010108 - Controle Societário (Data da Última Atualização e Capital Social)
################################################################################################
def processaBloco010108(linha):
    DataUltimaAtualizacao = str(linha[7:15]).strip()
    ValorCapitalSocial = str(linha[15:28]).strip()
    ValorCapitalRealizado = str(linha[28:41]).strip()
    ValorCapitalAutorizado = str(linha[41:54]).strip()
    DescricaoNacionalidade = str(linha[54:66]).strip()
    DescricaoOrigem = str(linha[66:78]).strip()
    DescricaoNatureza = str(linha[78:90]).strip()
    
    CodControleSocietarioBaseJunta = str(linha[90:91]).strip()
    DescControleSocietarioBaseJunta = buscaControleSocietarioBaseJunta(str(linha[90:91]).strip())

    CodSituacaoCapitalTotal = str(linha[91:92]).strip()
    DescCodSituacaoCapitalTotal = buscaSituacaoCapitalTotal(str(linha[91:92]).strip())

    return {
        'DataUltimaAtualizacao' : DataUltimaAtualizacao,
        'ValorCapitalSocial' : ValorCapitalSocial,
        'ValorCapitalRealizado' : ValorCapitalRealizado,
        'ValorCapitalAutorizado' : ValorCapitalAutorizado,
        'DescricaoNacionalidade' : DescricaoNacionalidade,
        'DescricaoOrigem' : DescricaoOrigem,
        'DescricaoNatureza' : DescricaoNatureza,
        'CodControleSocietarioBaseJunta' : CodControleSocietarioBaseJunta,
        'DescControleSocietarioBaseJunta' : DescControleSocietarioBaseJunta,
        'CodSituacaoCapitalTotal' : CodSituacaoCapitalTotal,
        'DescCodSituacaoCapitalTotal' : DescCodSituacaoCapitalTotal
    }

################################################################################################
#Bloco 010109 - Controle Societário (Detalhes dos Sócios)
################################################################################################
def processaBloco010109(linha):
    TipoSocio = str(linha[7:8]).strip()
    CPFCNPJSocio = str(linha[8:17]).strip()
    
    TipoDcto = str(linha[17:21]).strip()
    DescTipoDcto = buscaTipoDctoSocio(str(linha[17:21]).strip())

    DigitoControleCPF = str(linha[21:23]).strip()
    NomeSocio = str(linha[23:88]).strip()
    NacionalidadeSocio = str(linha[88:100]).strip()
    PercentualCapital = str(linha[100:104]).strip()
    DataEntradaSocio = str(linha[104:112]).strip()
    SocioComRestricao = str(linha[112:113]).strip()
    PercentualCapitalVotante = str(linha[113:117]).strip()
    
    CodSituacaoSocio = str(linha[117:119]).strip()
    DescSituacaoSocio = buscaSituacaoSocio(str(linha[117:119]).strip())

    CodSocioSERASA = str(linha[119:126]).strip()

    CodStatusSocioConstituido = str(linha[126:127]).strip()
    DescStatusSocioConstituido = buscaStatusSocioConstituido(str(linha[126:127]).strip())

    return {
        'TipoSocio' : TipoSocio,
        'CPFCNPJSocio' : CPFCNPJSocio,
        'TipoDcto' : TipoDcto,
        'DescTipoDcto' : DescTipoDcto,
        'DigitoControleCPF' : DigitoControleCPF,
        'NomeSocio' : NomeSocio,
        'NacionalidadeSocio' : NacionalidadeSocio,
        'PercentualCapital' : PercentualCapital,
        'DataEntradaSocio' : DataEntradaSocio,
        'SocioComRestricao' : SocioComRestricao,
        'PercentualCapitalVotante' : PercentualCapitalVotante,
        'CodSituacaoSocio' : CodSituacaoSocio,
        'DescSituacaoSocio': DescSituacaoSocio,
        'CodSocioSERASA': CodSocioSERASA,
        'CodStatusSocioConstituido': CodStatusSocioConstituido,
        'DescStatusSocioConstituido': DescStatusSocioConstituido
    }

################################################################################################
#Bloco 010110 - Quadro Administrativo
################################################################################################
def processaBloco010110(linha):
    DataUltimaAtualizacao = str(linha[7:15]).strip()
    CodQuadroAdminBaseJunta = str(linha[15:16]).strip()
    DescQuadroAdminBaseJunta = buscaQuadroAdminBaseJunta(str(linha[15:16]).strip())
    
    return {
        'DataUltimaAtualizacao' : DataUltimaAtualizacao,
        'CodQuadroAdminBaseJunta' : CodQuadroAdminBaseJunta,
        'DescQuadroAdminBaseJunta': DescQuadroAdminBaseJunta
    }

################################################################################################
#Bloco 010111 - Quadro Administrativo
################################################################################################
def processaBloco010111(linha):
    TipoAdmin = str(linha[7:8]).strip()
    CPFCNPJAdmin = str(linha[8:17]).strip()
    
    TipoDctoAdmin = str(linha[17:21]).strip()
    DescTipoDctoAdmin = buscaTipoDctoAdmin(str(linha[17:21]).strip())

    DigitoControleCPFAdmin = str(linha[21:23]).strip()
    NomeAdmin = str(linha[23:81]).strip()
    CargoAdmin = str(linha[81:93]).strip()
    NacionalidadeAdmin = str(linha[93:105]).strip()
    EstadoCivilAdmin = str(linha[105:114]).strip()
    DataInicioMandato = str(linha[114:122]).strip()
    DataFimMandato = str(linha[122:130]).strip()
    AdminComRestricao = str(linha[130:131]).strip()
    CodCargoAdmin = str(linha[131:134]).strip()

    CodSituacaoAdmin = str(linha[134:136]).strip()
    DescSituacaoAdmin = buscaSituacaoAdmin(str(linha[134:136]).strip())

    DataEntradaAdmin = str(linha[136:144]).strip()

    CodStatusAdminConstituido = str(linha[144:145]).strip()
    DescStatusAdminConstituido = buscaStatusAdminConstituido(str(linha[144:145]).strip())

    return {
        'TipoAdmin' : TipoAdmin,
        'CPFCNPJAdmin' : CPFCNPJAdmin,
        'TipoDctoAdmin' : TipoDctoAdmin,
        'DescTipoDctoAdmin' : DescTipoDctoAdmin,
        'DigitoControleCPFAdmin' : DigitoControleCPFAdmin,
        'NomeAdmin' : NomeAdmin,
        'CargoAdmin': CargoAdmin,
        'NacionalidadeAdmin' : NacionalidadeAdmin,
        'EstadoCivilAdmin': EstadoCivilAdmin,
        'DataInicioMandato' : DataInicioMandato,
        'DataFimMandato' : DataFimMandato,
        'AdminComRestricao': AdminComRestricao,
        'CodCargoAdmin' : CodCargoAdmin,
        'CodSituacaoAdmin' : CodSituacaoAdmin,
        'DescSituacaoAdmin': DescSituacaoAdmin,
        'DataEntradaAdmin': DataEntradaAdmin,
        'CodStatusAdminConstituido': CodStatusAdminConstituido,
        'DescStatusAdminConstituido': DescStatusAdminConstituido
    }

################################################################################################
#Bloco 010112 - Quadro Administrativo
################################################################################################
def processaBloco010112(linha):
    DataUltimaAtualizacao = str(linha[7:15]).strip()
    CodOrigemDados = str(linha[15:16]).strip()
    DescBaseJunta = buscaBaseJunta(str(linha[15:16]).strip())
    
    return {
        'DataUltimaAtualizacao' : DataUltimaAtualizacao,
        'CodOrigemDados' : CodOrigemDados,
        'DescBaseJunta': DescBaseJunta
    }

################################################################################################
#Bloco 010113 - Participações - Participada
################################################################################################
def processaBloco010113(linha):
    CPFCNPJParticipada = str(linha[7:16]).strip()
    DigitoCPFParticipada = str(linha[16:18]).strip()
    EmpresaParcipada = str(linha[18:85]).strip()
    TemRestricao = str(linha[85:86]).strip()

    TipoDctoParticipada = str(linha[86:90]).strip()
    DescTipoDctoParticipada = buscaTipoDctoParticipada(str(linha[86:90]).strip())

    TipoParticipada = str(linha[90:91]).strip()

    CodSituacaoParticipada = str(linha[91:93]).strip()
    DescSituacaoParticipada = buscaSituacaoParticipada(str(linha[91:93]).strip())

    return {
        'CPFCNPJParticipada' : CPFCNPJParticipada,
        'DigitoCPFParticipada' : DigitoCPFParticipada,
        'EmpresaParcipada' : EmpresaParcipada,
        'TemRestricao' : TemRestricao,
        'TipoDctoParticipada' : TipoDctoParticipada,
        'DescTipoDctoParticipada' : DescTipoDctoParticipada,
        'TipoParticipada': TipoParticipada,
        'CodSituacaoParticipada' : CodSituacaoParticipada,
        'DescSituacaoParticipada': DescSituacaoParticipada
    }

################################################################################################
#Bloco 010114 - Participações - Participante 
################################################################################################
def processaBloco010114(linha):
    NomeParticipante = str(linha[7:74]).strip()
    VinculoParticipante = str(linha[74:83]).strip()
    CodEmbratelParticipante = str(linha[83:87]).strip()
    DescCidadeEmbratelParticipante = str(linha[87:117]).strip()
    UFEmbratelParticipante = str(linha[117:119]).strip()
    PercParticipacaoParticipante = str(linha[119:124]).strip()
    TemRestricao = str(linha[124:125]).strip()
    CPFCNPJParticipante = str(linha[125:134]).strip()

    TipoDctoParticipante = str(linha[134:138]).strip()
    DescTipoDctoParticipante = buscaTipoDctoParticipante(str(linha[134:138]).strip())

    DigitoCPFParticipante = str(linha[138:140]).strip()
    TipoParticipante = str(linha[140:141]).strip()

    CodSituacaoParticipante = str(linha[141:143]).strip()
    DescSituacaoParticipante = buscaSituacaoParticipante(str(linha[141:143]).strip())

    return {
        'NomeParticipante' : NomeParticipante,
        'VinculoParticipante' : VinculoParticipante,
        'CodEmbratelParticipante' : CodEmbratelParticipante,
        'DescCidadeEmbratelParticipante' : DescCidadeEmbratelParticipante,
        'UFEmbratelParticipante' : UFEmbratelParticipante,
        'PercParticipacaoParticipante' : PercParticipacaoParticipante,
        'TemRestricao': TemRestricao,
        'CPFCNPJParticipante' : CPFCNPJParticipante,
        'TipoDctoParticipante': TipoDctoParticipante,
        'DescTipoDctoParticipante': DescTipoDctoParticipante,
        'DigitoCPFParticipante': DigitoCPFParticipante,
        'TipoParticipante': TipoParticipante,
        'CodSituacaoParticipante': CodSituacaoParticipante,
        'DescSituacaoParticipante': DescSituacaoParticipante
    }

################################################################################################
#Bloco 010115 - Nomes Semelhantes
################################################################################################
def processaBloco010115(linha):
    Nome = str(linha[7:67]).strip()
    ReservadoSERASA = str(linha[67:117]).strip()
    SituacaoEmpresa = str(linha[117:118]).strip()
    TipoDcto = str(linha[118:119]).strip()
    NIRE = str(linha[119:130]).strip()
    Origem = str(linha[130:133]).strip()
    ReservadoSERASA2 = str(linha[133:153]).strip()
    UF = str(linha[153:155]).strip()
    Praca = str(linha[155:159]).strip()
    Cidade = str(linha[159:184]).strip()
    ReservadoSERASA3 = str(linha[184:289]).strip()
    SeqGeracao = str(linha[289:292]).strip()
    Ident = str(linha[292:293]).strip()
    Restri = str(linha[293:284]).strip()

    return {
        'Nome' : Nome,
        'ReservadoSERASA' : ReservadoSERASA,
        'SituacaoEmpresa' : SituacaoEmpresa,
        'TipoDcto' : TipoDcto,
        'NIRE' : NIRE,
        'Origem' : Origem,
        'ReservadoSERASA2': ReservadoSERASA2,
        'UF' : UF,
        'Praca': Praca,
        'Cidade': Cidade,
        'ReservadoSERASA3': ReservadoSERASA3,
        'SeqGeracao': SeqGeracao,
        'Ident': Ident,
        'Restri': Restri
    }

################################################################################################
#Bloco 010116 - Antecessora
################################################################################################
def processaBloco010116(linha):
    RazaoSocialAntecessora = str(linha[7:77]).strip()
    ReservadoSERASA = str(linha[77:78]).strip()
    DataMotivo = str(linha[78:86]).strip()
    ReservadoSERASA2 = str(linha[86:95]).strip()

    return {
        'RazaoSocialAntecessora' : RazaoSocialAntecessora,
        'ReservadoSERASA' : ReservadoSERASA,
        'DataMotivo' : DataMotivo,
        'ReservadoSERASA2' : ReservadoSERASA2
    }

################################################################################################
#Bloco 010117 - Informações Adicionais dos Sócios – Novo quadro social
################################################################################################
def processaBloco010117(linha):
    DctoSocio = str(linha[7:16]).strip()
    FilialDcto = str(linha[16:20]).strip()
    DigitoDcto = str(linha[20:22]).strip()
    DataAtualizacao = str(linha[22:30]).strip()
    NomeSocio = str(linha[30:90]).strip()
    DataRGSocio = str(linha[90:101]).strip()    
    DataNascimentoSocio = str(linha[101:109]).strip()    
    
    CodVinculoSocio = str(linha[109:110]).strip()
    DesVinculoSocio = buscaTipoSocio(str(linha[109:110]).strip())
    
    CidadeNascSocio = str(linha[110:140]).strip()
    UFNascSocio = str(linha[140:142]).strip()
    DDDFoneSocio = str(linha[142:146]).strip()
    FoneSocio = str(linha[146:155]).strip()
    RamalFoneSocio = str(linha[155:159]).strip()
    RuaEndSocio = str(linha[159:229]).strip()
    BairroEndSocio = str(linha[229:249]).strip()
    CidadeEndSocio = str(linha[249:279]).strip()
    UFEndSocio = str(linha[279:281]).strip()
    CEPEndSocio = str(linha[281:290]).strip()
    ReservadoSERASA = str(linha[290:294]).strip()
    SituacaoSocio = str(linha[294:295]).strip()
    DesSituacaoSocio = buscaStatusSocioConstituido(str(linha[294:295]).strip())

    return {
        'DctoSocio' : DctoSocio,
        'FilialDcto' : FilialDcto,
        'DigitoDcto' : DigitoDcto,
        'DataAtualizacao' : DataAtualizacao,
        'NomeSocio' : NomeSocio,
        'DataRGSocio' : DataRGSocio,
        'DataNascimentoSocio' : DataNascimentoSocio,
        'CodVinculoSocio' : CodVinculoSocio,
        'DesVinculoSocio' : DesVinculoSocio,
        'CidadeNascSocio' : CidadeNascSocio,
        'UFNascSocio' : UFNascSocio,
        'DDDFoneSocio' : DDDFoneSocio,
        'FoneSocio' : FoneSocio,
        'RamalFoneSocio' : RamalFoneSocio,
        'RuaEndSocio' : RuaEndSocio,
        'BairroEndSocio' : BairroEndSocio,
        'CidadeEndSocio' : CidadeEndSocio,
        'UFEndSocio' : UFEndSocio,
        'CEPEndSocio' : CEPEndSocio,
        'ReservadoSERASA' : ReservadoSERASA,
        'SituacaoSocio' : SituacaoSocio,
        'DesSituacaoSocio': DesSituacaoSocio
    }

################################################################################################
#Bloco 010118 - Informações Adicionais dos Sócios - Complemento – Novo quadro social
################################################################################################
def processaBloco010118(linha):
    DescCodProfissao = str(linha[7:19]).strip()
    RendaMensal = str(linha[19:30]).strip()
    OutrasRendas = str(linha[30:41]).strip()
    CodPeriodoOutrasRendas = str(linha[41:53]).strip()
    OrigemOutrasRendas = str(linha[53:65]).strip()
    CPFConjuge = str(linha[65:74]).strip()
    DigCPFConjuge = str(linha[74:76]).strip()
    NomeConjuge = str(linha[76:136]).strip()
    RGConjuge = str(linha[136:147]).strip()
    RendaMensalConjuge = str(linha[147:158]).strip()

    return {
        'DescCodProfissao' : DescCodProfissao,
        'RendaMensal' : RendaMensal,
        'OutrasRendas' : OutrasRendas,
        'CodPeriodoOutrasRendas' : CodPeriodoOutrasRendas,
        'OrigemOutrasRendas' : OrigemOutrasRendas,
        'DataMotivo' : CPFConjuge,
        'DataMotivo' : DigCPFConjuge,
        'DataMotivo' : NomeConjuge,
        'DataMotivo' : RGConjuge,
        'DataMotivo' : RendaMensalConjuge
    }

################################################################################################
#Bloco 010119 - Informações Adicionais dos Sócios – (PJ) – Novo quadro social
################################################################################################
def processaBloco010119(linha):
    CNPJSocio = str(linha[7:16]).strip()
    FilialCNPJSocio = str(linha[16:20]).strip()
    DigCNPJSocio = str(linha[20:22]).strip()
    DataFundacao = str(linha[22:30]).strip()
    DataAtualizacao = str(linha[30:38]).strip()
    RazaoSocialSocio = str(linha[38:108]).strip()
    NomeFantasiaSocio = str(linha[108:138]).strip()
    
    CodVinculo = str(linha[138:139]).strip()
    DesVinculo = buscaTipoSocio(str(linha[138:139]).strip())
    
    CodSituacaoSocio = str(linha[139:140]).strip()
    DescSituacaoSocio = buscaStatusSocioConstituido(str(linha[139:140]).strip())

    return {
        'CNPJSocio' : CNPJSocio,
        'FilialCNPJSocio' : FilialCNPJSocio,
        'DigCNPJSocio' : DigCNPJSocio,
        'DataFundacao' : DataFundacao,
        'DataAtualizacao' : DataAtualizacao,
        'RazaoSocialSocio' : RazaoSocialSocio,
        'NomeFantasiaSocio' : NomeFantasiaSocio,
        'CodVinculo' : CodVinculo,
        'DesVinculo' : DesVinculo,
        'CodSituacaoSocio' : CodSituacaoSocio,
        'DescSituacaoSocio': DescSituacaoSocio
    }

################################################################################################
#Bloco 010120 - Informações Adicionais dos Sócios – (PJ) - Dados Complementares – Novo quadro social
################################################################################################
def processaBloco010120(linha):
    RuaEndSocio = str(linha[7:70]).strip()
    BairroEndSocio = str(linha[70:97]).strip()
    CidadeEndSocio = str(linha[97:127]).strip()
    UFEndSocio = str(linha[127:129]).strip()
    CEPEndSocio = str(linha[129:138]).strip()
    DDDFoneSocio = str(linha[138:142]).strip()
    FoneSocio = str(linha[142:151]).strip()
    RamalFoneSocio = str(linha[151:155]).strip()
    RamoAtividadeSocio = str(linha[155:215]).strip()

    return {
        'RuaEndSocio' : RuaEndSocio,
        'BairroEndSocio' : BairroEndSocio,
        'CidadeEndSocio' : CidadeEndSocio,
        'UFEndSocio' : UFEndSocio,
        'CEPEndSocio' : CEPEndSocio,
        'DDDFoneSocio' : DDDFoneSocio,
        'FoneSocio' : FoneSocio,
        'RamalFoneSocio' : RamalFoneSocio,
        'RamoAtividadeSocio' : RamoAtividadeSocio
    }

################################################################################################
#Bloco 010121 - Veículos e Outros Bens dos Sócios / Administradores (PESSOA FÍSICA)
################################################################################################
def processaBloco010121(linha):
    TipoPessoa = str(linha[7:8]).strip()
    CPFSocio = str(linha[8:17]).strip()
    SeqSocio = str(linha[17:21]).strip()
    DigSocio = str(linha[21:23]).strip()
    DataUltimaAtualizacao = str(linha[23:31]).strip()
    DescricaoBem = str(linha[31:61]).strip()
    ValorBem = str(linha[61:74]).strip()
    Onus = str(linha[74:75]).strip()

    return {
        'TipoPessoa' : TipoPessoa,
        'CPFSocio' : CPFSocio,
        'SeqSocio' : SeqSocio,
        'DigSocio' : DigSocio,
        'DataUltimaAtualizacao' : DataUltimaAtualizacao,
        'DescricaoBem' : DescricaoBem,
        'ValorBem' : ValorBem,
        'Onus' : Onus
    }

################################################################################################
#Bloco 010122 - Quadro Social Utilizando Informações da Junta Comercial
################################################################################################
def processaBloco010122(linha):
    RazaoSocial = str(linha[7:67]).strip()
    NIRE = str(linha[67:78]).strip()
    ReservadaSERASA = str(linha[78:87]).strip()
    
    return {
        'RazaoSocial' : RazaoSocial,
        'NIRE' : NIRE,
        'ReservadaSERASA': ReservadaSERASA
    }

################################################################################################
#Bloco 010198 - Observações Cadastrais de Incorporação, Fusão, Cisão
################################################################################################
def processaBloco010198(linha):
    MsgBlocoObservCadastrais = str(linha[7:86]).strip()
    DataAtualizacaoBloco = str(linha[86:94]).strip()
    
    return {
        'MsgBlocoObservCadastrais' : MsgBlocoObservCadastrais,
        'DataAtualizacaoBloco' : DataAtualizacaoBloco
    }

