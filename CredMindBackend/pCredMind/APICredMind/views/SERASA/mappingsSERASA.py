# mapeamentos.py

SituacoesEmpresaANTIGA = {
    '00': 'INAPTA',
    '02': 'ATIVA',
    '03': 'INATIVA',
    '04': 'NAO LOCALIZADA',
    '05': 'EM LIQUIDACAO',
    '06': 'SUSPENSO',
    '07': 'NAO CADASTRADA',
    '09': 'CANCELADO',
}

MensagensReciprocidade = {
    '' : '',
    'A': 'ATENÇÃO!!! VOCE NÃO ESTÁ VISUALIZANDO O BLOCO “EVOLUCAO DE COMPROMISSOS” SUA EMPRESA ENCONTRA-SE EM ATRASO COM O ENVIO DOS DADOS DESDE (DTULTRECIPR) AO REGULARIZAR O ENVIO, O REFERIDO BLOCO VOLTARÁ A SER EXIBIDO AUTOMATICAMENTE',
    'B': 'ATENÇÃO!!! VOCE NÃO ESTÁ VISUALIZANDO O BLOCO “HISTORICO DE PAGAMENTOS (VALORES EM R$)” SUA EMPRESA ENCONTRA-SE EM ATRASO COM O ENVIO DOS DADOS DESDE (DTULTRECIPR) AO REGULARIZAR O ENVIO, O REFERIDO BLOCO VOLTARÁ A SER EXIBIDO AUTOMATICAMENTE',
    'C': 'ATENÇÃO!!! VOCÊ NÃO ESTÁ VISUALIZANDO O RELATO ANALÍTICO  SUA EMPRESA ENCONTRA-SE EM ATRASO COM O ENVIO DOS DADOS DESDE (DTULTRECIPR) AO REGULARIZAR O ENVIO, O RELATO ANALÍTICO SERÁ VISUALIZADO AUTOMATICAMENTE ',
    'D': 'ATENÇÃO!!! VOCÊ NÃO ESTÁ VISUALIZANDO OS BLOCOS “HISTORICO DE PAGAMENTOS (VALORES EM R$)” E “EVOLUÇÃO DE COMPROMISSOS” EM VIRTUDE DE ATRASO COM OS DADOS DESDE (DTULTRECIPR) AO REGULARIZAR O ENVIO, OS BLOCOS VOLTARAO A SER EXIBIDOS AUTOMATICAMENTE',
    'E': 'ATENÇÃO!!! VOCE TEM?? DIAS DE ACESSO LIBERADO AS INFORMACOES DE COMPORTAMENTO EM NEGOCIOS PARA CONTINUAR VISUALIZANDO-AS, CONTATE O SEU GERENTE DE RELACIONAMENTO OU PELO TELEFONE 33 SERASA, E VEJA COMO E FACIL MANDAR SEUS DADOS PARA SERASA.',
    'F': 'ATENÇÃO!!! VOCÊ NÃO ESTÁ VISUALIZANDO O RELATO ANALÍTICO  SUA EMPRESA ENCONTRA-SE EM ATRASO COM O ENVIO DO ARQUIVO DE CONCILIAÇÃO DESDE (01/01/0001). AO REGULARIZAR A CONCILIAÇÃO, O RELATO ANALÍTICO SERÁ VISUALIZADO AUTOMATICAMENTE.',
    'G': 'ATENÇÃO!!! VOCÊ NÃO ESTÁ VISUALIZANDO O RELATO ANALÍTICO. O LIMITE DE CONSULTAS ANALÍTICAS FOI ATINGIDO. FAVOR ENVIAR DADOS DE RECIPROCIDADE PARA REGULARIZAR A VISÃO.',
    'H': 'ATENÇÃO!!! VOCÊ NÃO ESTÁ VISUALIZANDO O BLOCO “EVOLUÇÃO DE COMPROMISSOS”. O LIMITE DE CONSULTAS ANALÍTICAS PARA O BLOCO FOI ATINGIDO. FAVOR ENVIAR DADOS DE RECIPROCIDADE PARA REGULARIZAR A VISÃO.',
    'I': 'ATENÇÃO!!! VOCÊ NÃO ESTÁ VISUALIZANDO O BLOCO “HISTÓRICO DE PAGAMENTOS”. O LIMITE DE CONSULTAS ANALÍTICAS PARA O BLOCO FOI ATINGIDO. FAVOR ENVIAR DADOS DE RECIPROCIDADE PARA REGULARIZAR A VISÃO.',
}

TiposRelato = {
    '1' : 'ANALITICO',
    '2' : 'SINTETICO',
}

TiposRelCob = {
    '1' : 'QUADRO SOCIAL CORTESIA',
    '2' : 'QUADRO SOCIAL COM COBRANÇA',
}

SituacoesEmpresaNova = {
    '0': 'INAPTA',
    '2': 'ATIVA',
    '4': 'NULA',
    '6': 'SUSPENSA',
    '7': 'BAIXADA',
}

ControleSocietarioBaseJunta = {
    ' ': 'NAO',
    '4': 'SIM',
}

SituacaoCapitalTotal = {
    'F': 'EMPRESA COM % > ou = 95% e < ou = 100 %',
    'N': 'EMPRESA COM % MENOR QUE 95%',
    'M': 'EMPRESA COM % MAIOR QUE 100%',
}

TipoDctoSocio = {
    '0000': 'DOCUMENTO OFICIAL',
    '0050': 'DOCUMENTO ATRIBUÍDO PELA SERASA',
    '0099': 'DOCUMENTO NÃO CONFIRMAÇÃO OFICIAL',
}

SituacaoSocio = {
    '00': 'INAPTA',
    '02': 'ATIVA',
    '03': 'INATIVA',
    '04': 'NAO LOCALIZADA',
    '05': 'EM LIQUIDACAO',
    '06': 'NAO CADASTRADA',
    '07': 'SUSPENSO',
    '09': 'CANCELADO',
}

StatusSocioConstituido = {
    'I': 'INCONSISTENTE',
    'C': 'CONSISTENTE',
}

QuadroAdminBaseJunta = {
    '': 'NAO',
    '4' : 'SIM',
}

TipoDctoAdmin = {
    '0000': 'DOCUMENTO OFICIAL',
    '0050': 'DOCUMENTO ATRIBUÍDO PELA SERASA',
    '0099': 'DOCUMENTO NÃO CONFIRMAÇÃO OFICIAL',
}

SituacaoAdmin = {
    '00': 'INAPTA',
    '02': 'ATIVA',
    '03': 'INATIVA',
    '04': 'NAO LOCALIZADA',
    '05': 'EM LIQUIDACAO',
    '06': 'NAO CADASTRADA',
    '07': 'SUSPENSO',
    '09': 'CANCELADO',
}

StatusAdminConstituido = {
    'I': 'INCONSISTENTE',
    'C': 'CONSISTENTE',
}

BaseJunta = {
    '': 'NAO',
    '4' : 'SIM',
}

TipoDctoParticipada = {
    '0000': 'DOCUMENTO OFICIAL',
    '0050': 'DOCUMENTO ATRIBUÍDO PELA SERASA',
    '0099': 'DOCUMENTO NÃO CONFIRMAÇÃO OFICIAL',
}

SituacaoParticipada = {
    '00': 'INAPTA',
    '02': 'ATIVA',
    '03': 'INATIVA',
    '04': 'NAO LOCALIZADA',
    '05': 'EM LIQUIDACAO',
    '06': 'NAO CADASTRADA',
    '07': 'SUSPENSO',
    '09': 'CANCELADO',
}

TipoDctoParticipante = {
    '0000': 'DOCUMENTO OFICIAL',
    '0050': 'DOCUMENTO ATRIBUÍDO PELA SERASA',
    '0099': 'DOCUMENTO NÃO CONFIRMAÇÃO OFICIAL',
}

SituacaoParticipante = {
    '00': 'INAPTA',
    '02': 'ATIVA',
    '03': 'INATIVA',
    '04': 'NAO LOCALIZADA',
    '05': 'EM LIQUIDACAO',
    '06': 'NAO CADASTRADA',
    '07': 'SUSPENSO',
    '09': 'CANCELADO',
}

TipoSocio = {
    'A': 'ADMINITRADOR',
    'S': 'SOCIO',
    'D': 'SOCIO / ADMINISTRADOR',
}

TipoPrazo = {
    'V': 'A VISTA',
    'P' : 'A PRAZO',
}

TipoSinalDiasAtraso = {
    '0': 'DIAS POSITIVO',
    '1' : 'DIAS NEGATIVO',
}

RetornoModVerifTitulo = {
    '00': 'OPERAÇÃO JÁ CADASTRADA',
    '01' : 'TÍTULO NÃO ENCONTRADO',
}

TipoEmpresa = {
    'F': 'BANCO',
    'C' : 'EMPRESA',
    'A' : 'BANCO + EMPRESA'
}

TipoPessoa = {
    'F': 'FISICA',
    'C' : 'JURIDICA'
}

TipoConsulta = {
    ' ': 'MERCADO',
    'T': 'SETOR',
    'G' : 'SEGMENTO'
}

TipoNaturezaCONCENTRE = {
    '01': 'PENDENCIA FINANCEIRA (SOMENTE PARA AUTORIZADOR)',
    '03': 'PROTESTO',
    '04': 'ACAO JUDICIAL',
    '05': 'PARTICIPACAO EM FALENCIA',
    '06': 'FALENCIA/CONCORDATA',
    '07': 'DIVIDA VENCIDA',
    '09': 'CHEQUE SEM FUNDO ACHEI',
    '10': 'REFIN (SOMENTE PARA AUTORIZADOR)',
}

TipoNaturezaModalidadeCONVEMPEFIN = {
    'AD' : 'ADIANTAMENTOS A DEPOSITANTES - C/C DEVEDORA',
    'AG' : 'EMPRÉSTIMOS AGRÍCOLAS E INDUSTRIAIS',
    'AL' : 'ALUGUEL',
    'AR' : 'ARRENDAMENTOS, INCLUSIVE LEASING',
    'C1' : 'CONSÓRCIO DE IMÓVEL',
    'C2' : 'CONSÓRCIO VEÍCULOS PESADOS: TRATORES, ÔNIBUS, CAMINHÕES, BARCOS E AVIÕES',
    'C3' : 'CONSÓRCIO VEÍCULOS  ',
    'C4' : 'CONSÓRCIO DE MOTOCICLETAS E MOTONETAS',
    'C5' : 'CONSÓRCIO OUTROS BENS MÓVEIS',
    'C6' : 'CONSÓRCIO DE PASSAGENS AÉREAS',
    'CA' : 'OPERAÇÕES DE CÂMBIO',
    'CB' : 'CDC OUTROS BENS MÓVEIS',
    'CC' : 'COTA CONDOMINIAL',
    'CD' : 'CRÉDITO DIRETO',
    'CL' : 'CDC VEÍCULOS LEVES',
    'CM' : 'CDC MOTOCICLETAS E MOTONETAS',
    'CO' : 'CONSÓRCIO CONTEMPLADO',
    'CP' : 'CRÉDITO PESSOAL',
    'CR' : 'IMPEDIDOS DE CRÉDITO RURAL PELO BACEN',
    'CT' : 'OPERAÇÕES COM CARTÃO DE CRÉDITO',
    'CV' : 'CDC VEÍCULOS PESADOS: TRATORES, ÔNIBUS, CAMINHÕES, BARCOS E AVIÕES',
    'DC' : 'DÍVIDAS ORIGINÁRIAS DE CHEQUES',
    'DE' : 'DÍVIDAS ORIGINARIAS DE CHEQUES ELETRÔNICOS',
    'DP' : 'DUPLICATA',
    'EC' : 'EMPRÉSTIMOS EM CONTA, C/C GARANT., CAP. GIRO, PROGR. ESPECIAL',
    'EE' : 'ENERGIA ELÉTRICA-FATURAS DE FORNECIMENTO DE LUZ',
    'EG' : 'EMPRÉSTIMO CONSIGNADO',
    'FG' : 'GÁS-FATURAS DE FORNECIMENTO DE GÁS',
    'FI' : 'CRÉDITOS E FINANCIAMENTOS',
    'HO' : 'DESPESAS COM HOSPITAIS',
    'IE' : 'INSTITUIÇÃO DE ENSINO:  BOLSA RESTITUÍVEL',
    'IM' : 'OPERAÇÕES IMOBILIÁRIAS',
    'LL' : 'LEASING VEÍCULOS LEVES',
    'LM' : 'LEASING MOTOCICLETAS E MOTONETAS',
    'LV' : 'LEASING VEÍCULOS PESADOS:TRATORES, ÔNIBUS, CAMINHÕES, BARCOS E AVIÕES',
    'ME' : 'MENSALIDADES ESCOLARES',
    'NF' : 'NOTAS FISCAIS',
    'OA' : 'OPERAÇÕES AGRÍCOLAS NEGOCIAÇÕES PRODUTOS RURAIS-INSUMOS, SEMENTES ETC.  ',
    'OJ' : 'OPERAÇÕES AJUIZADAS',
    'OO' : 'OUTRAS OPERAÇÕES',
    'RE' : 'OPERAÇÕES DE REPASSE, FINAME, 63, RECON ETC.',
    'RR' : 'ARRECADADORES-PRESTADORES DE SERVIÇOS',
    'SB' : 'SANEAMENTO BÁSICO, FATURAS DE FORNECIMENTO DE ÁGUA',
    'SF' : 'SEGURO FIANÇA LOCATÍCIA ',
    'SG' : 'SEGURO GARANTIA ',
    'SQ' : 'SEGURO QUEBRA DE GARANTIA',
    'SR' : 'SEGURO DE RISCO DECORRIDO',
    'SS' : 'MENSALIDADE DE PLANO/SEGURO DE SAÚDE',
    'TC' : 'TERMO DE CONFISSÃO DE DÍVIDA DESCUMPRIDO',
    'TD' : 'TÍTULOS DESCONTADOS, DUPLICATAS, PROMISSÓRIAS ETC.',
    'TE' : 'SERVIÇOS DE TELEFONIA MÓVEL PESSOAL / CELULAR OUTRAS CONTAS APÓS RESCISÃO DO CONTRATO.',
    'TF' : 'SERVIÇOS DE TELEFONIA FIXA OUTRAS CONTAS APÓS RESCISÃO DO CONTRATO ',
    'TI' : 'SERVIÇOS DE DADOS E INTERNET (SPEEDY, ALUGUEL DE CANAIS DE DADOS E FIBRA ÓTICA) ',
    'TM' : 'SERVIÇOS DE TELEFONIA MÓVEL PESSOAL / CELULAR RES221/00',
    'TP' : 'SERVIÇOS DE TELEFONIA / VENDAS DE PRODUTOS VENDAS DE APARELHOS, INSTALAÇÃO, ALUGUEL DE APARELHOS ',
    'TR' : 'SERVIÇOS DE TELEFONIA RENEGOCIAÇÃO DA DÍVIDA ',
    'TT' : 'SERVIÇOS DE TELEFONIA FIXA RES 085/98',
    'VM' : 'PRESTAÇÃO DE SERVIÇOS-VENDAS DE MERCADORIAS'
}

TipoCartaAnuencia = {
    'C': 'CARTA ANUÊNCIA ENTREGUE PELO CREDOR',
    'E': 'CARTA ANUÊNCIA ELETRÔNICA ENTREGUE PELO CREDOR',
    'D': 'CARTA ANUÊNCIA ENTREGUE PELO DEVEDOR'
}

TipoProtesto = {
    'Z1': 'FALTA DE PAGAMENTO'
}

TipoAcao = {
    'EX': 'EXECUÇÃO',
    'BA': 'BUSCA E APREENSAO',
    'JF': 'JUSTIÇA FEDERAL',
    'JE': 'EXECUCAO - PEQUENAS CAUSAS',
    'JB': 'BUSCA E APREENSAO PEQUENAS CAUSAS',
    'FE': 'AÇO FISCAL ESTADUAL',
    'FM': 'AÇAO FISCAL MUNICIPAL',
    'TR': 'EXECUCAO DE TÍTULO JUDICIAL TRABALHISTA'
}

TipoFalenciaConcordata = {
    'FR': 'FALENCIA REQUERIDA'
}

TipoPIE = {
    'FD': 'FALENCIA DECRETADA',
    'AF': 'AUTO FALENCIA',
    'CR': 'CONCORDATA REQUERIDA',
    'CD': 'CONCORDATA DEFERIDA',
    'CS': 'CONCORDATA SUSPENSIVA',
    'RR': 'RECUPERACAO JUDICIAL REQUERIDA',
    'RC': 'RECUPERACAO JUDICIAL CONCEDIDA',
    'RE': 'RECUPERACAO EXTRAJUDICIAL REQUERIDA',
    'RH': 'RECUPERACAO EXTRAJUDICIAL HOMOLOGADA'
}

TipoACHEI = {
    '12': 'CHEQUE SEM FUNDO (SEGUNDA APRESENTACAO)',
    '13': 'CONTA ENCERRADA',
    '14': 'PRÁTICA ESPURIA'
}

TipoCCF = {
    'I': 'CONTA INDIVIDUAL',
    'C': 'CONTA CONJUNTA'
}

TipoSRF = {
    '66': 'LEI 5.614 IN66/97'
}

TipoCONVEMDevedores = {
    'CC': 'COBRANCA CAUCIONADA',
    'CD': 'COBRANCA DIRETA',
    'CE': 'COBRANCA ESTADUAL',
    'CF': 'COBRANCA DESCONTADA',
    'CH': 'CHEQUE',
    'CS': 'COBRANCA SIMPLES',
    'DP': 'DUPLICATA',
    'NP': 'NOTA PROMISSORIA',
    'CBI': 'CEDULA DE CREDITO BANCERIO POR INDICACAO',
    'CCB': 'CEDULA DE CREDITO BANCERIO',
    'CDA': 'CERTIDAO DE DIVIDA ATIVA',
    'CPS': 'CONTA DE PRESTACAO DE SERVICO',
    'CT': 'ESPECIE DE CONTRATO',
    'DD': 'DOCUMENTO DE DIVIDA',
    'EC': 'ENCARGOS CONDOMINIAIS',
    'FS': 'FATURA DE SERVICO',
    'ME': 'MENSALIDADES ESCOLARES',
    'RA': 'RECIBO DE ALUGUEL APENAS PARA PJ',
    'OU': 'OUTROS'
}

TipoQualifParticEmpFalida = {
    'GER': 'GERENTE',
    'TIT': 'TITULAR',
    'SOC': 'SOCIO',
    'DIR': 'DIRETOR'
}

TipoNaturezaRestricoesFinanREFIN = {
    'AD' : 'ADIANTAMENTO A DEPOSITANTES - C/C DEVEDORES EM GERAL',
    'AG' : 'EMPRÉSTIMOS AGRÍCOLAS E INDUSTRIAIS - FINANCIAMENTOS DE CUSTEIO DE INVESTIMENTOS AGRÍCOLAS E INDUSTRIAIS',
    'AR' : 'ARRENDAMENTOS, INCLUSIVE LEASING',
    'CA' : 'OPERAÇÕES DE CÂMBIO - OPERAÇÕES E FINANCIAMENTOS DE CÂMBIO EM GERAL',
    'CB' : 'CDC OUTROS BENS MÓVEIS',
    'CH' : 'ADIANTAMENTO A DEPOSITANTES - CHEQUES SEM FUNDOS ACOLHIDOS',
    'CL' : 'CDC VEÍCULOS LEVES',
    'CM' : 'CDC MOTOCICLETAS E MOTONETAS',
    'CR' : 'IMPEDIDOS PELO BANCO CENTRAL DE OBTENÇÃO DE CRÉDITO RURAL',
    'CT' : 'CARTÃO DE CRÉDITO',
    'CV' : 'CDC VEÍCULOS PESADOS: TRATORES, ÔNIBUS, CAMINHÕES, BARCOS E AVIÕES',
    'C2' : 'CONSÓRCIO VEÍCULOS PESADOS: TRATORES, ÔNIBUS, CAMINHÕES, BARCOS E AVIÕES',
    'C3' : 'CONSÓRCIO VEÍCULOS LEVES',
    'C4' : 'CONSÓRCIO MOTOCICLETAS E MOTONETAS',
    'C5' : 'CONSÓRCIO OUTROS BENS MÓVEIS',
    'EC' : 'EMPRÉSTIMOS EM CONTAS - C/C GARANTIDAS, FINANCIAMENTOS DE CAPITAL DE GIRO, PROGRAMAS ESPECIAIS ETC.',
    'FI' : 'CRÉDITOS E FINANCIAMENTOS - EMPRÉSTIMOS A PESSOAS FÍSICAS, FINANCIAMENTOS AO CONSUMIDOR FINAL ETC.',
    'IM' : 'OPERAÇÕES IMOBILIÁRIAS EM GERAL, INCLUSIVE DE SOCIEDADES DE POUPANÇA',
    'IP' : 'DÉBITO IPVA',
    'LL' : 'LEASING VEÍCULOS LEVES',
    'LM' : 'LEASING MOTOCICLETAS E MOTONETAS',
    'LV' : 'LEASING VEÍCULOS PESADOS: TRATORES, ÔNIBUS, CAMINHÕES, BARCOS E AVIÕES',
    'OJ' : 'OPERAÇÕES AJUIZADAS',
    'OO' : 'OUTRAS OPERAÇÕES - DIVERSAS OPERAÇÕES QUE NÃO SE ENQUADRAM NAS DEMAIS',
    'RE' : 'OPERAÇÕES DE REPASSE - OPERAÇÕES 63, FINAME, REINVEST, RECON, PROALCOOL ETC.',
    'SJ' : 'DÉBITO SUB JUDICE',
    'SR' : 'SEGURO DE RISCO DECORRIDO',
    'TD' : 'TÍTULOS DESCONTADOS - DESCONTOS DE DUPLICATAS, PROMISSÓRIAS E OUTROS TÍTULOS',
}

TipoMensagemPontualidade = {
    '9990' : 'CNPJ NÃO CADASTRADO NA BASE DE DADOS SERASA EXPERIAN',
    '9990' : 'SCORE NÃO CALCULADO INSUFICIENCIA INFORMACOES BASE DE DADOS SERASA EXPERIAN',
    '9990' : 'EMPRESA NAO LOCALIZADA NO ENDERECO INFORMADO',
    '9991' : 'SITUACAO DO CNPJ: EXTINTO',
    '9991' : 'SITUACAO DO CNPJ: BAIXADO',
    '9991' : 'SITUACAO DO CNPJ: NULO',
    '9991' : 'EMPRESA INATIVA-INCORPORADA',
    '9991' : 'EMPRESA INATIVA POR FUSAO',
    '9993' : 'NAO FOI POSSIVEL CALCULAR O INDICADOR DE PONTUALIDADE PJ, POIS O CNPJ CONSULTADO NAO APRESENTA INFORMACOES DE HISTORICO DE CREDITO NA BASE DE DADOS DA SERASA EXPERIAN.',
    '9994' : 'NAO FOI POSSIVEL CALCULAR O INDICADOR DE PONTUALIDADE PJ, POIS NAO HA CADASTRO POSITIVO ABERTO PARA O CNPJ CONSULTADO.',
    '9995' : 'NAO FOI POSSIVEL CALCULAR O INDICADOR DE PONTUALIDADE PJ, POIS AS INFORMACOES POSITIVAS DO CNPJ CONSULTADO NAO ESTAO DISPONIVEIS PARA O CALCULO.',
    '9996' : 'NAO FOI POSSIVEL CALCULAR O INDICADOR DE PONTUALIDADE PJ, POIS AS INFORMACOES COES POSITIVAS DO CNPJ CONSULTADO AINDA NAO PODEM SER DISPONIBILIZADAS',
}

TipoSimplesNacional = {
    'P' : 'OPTANTE',
    'N' : 'NAO OPTANTE',
    'A' : 'EM ANALISE'
}

TipoCodAlerta = {
    '0' : 'PROVISORIO',
    '1' : 'CONFIRMADO'
}

TipoCodSetor = {
    '0' : 'GERAL ',
    '1' : 'ATACADO',
    '2' : 'BANCOS / FINANCEIRAS',
    '3' : 'SERVIÇOS',
    '4' : 'COMÉRCIO',
    '5' : 'INDUSTRIA',
    '6' : 'FACTORING',
    '8' : 'OUTROS'
}

TipoCodRetornoMonitore = {
    '00' : 'INCLUSÃO EFETUADA COM SUCESSO',
    '99' : 'ERRO NA INCLUSÃO'
}

TipoOperacao = {
    'C' : 'COMPRADOR',
    'F' : 'FIADO',
    'A' : 'AVALISTA'
}

TipoRegistroLayout = {
    'C' : 'CADASTRAIS',
    'I' : 'INFORMACOES PRACA',
    'P' : 'CONSULTAS',
    'A' : 'APONTAMENTOS'
}

TipoLinhaLayout = {
    'C' : 'CABECALHO',
    'D' : 'DADOS VARIAVEIS',
    'F' : 'LITERAL + DADOS'
}

TipoAtributoLayout = {
    'F' : 'FIXA NORMAL',
    'B' : 'FIXA BRILHANTE',
    'V' : 'VARIAVEL NORMAL',
    'W' : 'VARIAVEL BRILHANTE '
}

###############################################################################################
###############################################################################################
###############################################################################################

def buscaMensagemReciprocidade(codigo):
    return MensagensReciprocidade.get(codigo, 'CODIGO NAO ENCONTRADO')

def buscaSituacaoEmpresaANTIGA(codigo):
    return SituacoesEmpresaANTIGA.get(codigo, 'CODIGO NAO ENCONTRADO')

def buscaTipoRelato(codigo):
    return TiposRelato.get(codigo, 'CODIGO NAO ENCONTRADO')

def buscaTipoRelCob(codigo):
    return TiposRelCob.get(codigo, 'CODIGO NAO ENCONTRADO')

def buscaSituacaoEmpresaNova(codigo):
    return SituacoesEmpresaNova.get(codigo, 'CODIGO NAO ENCONTRADO')

def buscaControleSocietarioBaseJunta(codigo):
    return ControleSocietarioBaseJunta.get(codigo, 'CODIGO NAO ENCONTRADO')

def buscaSituacaoCapitalTotal(codigo):
    return SituacaoCapitalTotal.get(codigo, 'CODIGO NAO ENCONTRADO')

def buscaTipoDctoSocio(codigo):
    return TipoDctoSocio.get(codigo, 'SEQUÊNCIA QUANDO DA UTILIZAÇÂO DE DOCUMENTO DE TERCEIROS')

def buscaSituacaoSocio(codigo):
    return SituacaoSocio.get(codigo, 'CODIGO NAO ENCONTRADO')

def buscaStatusSocioConstituido(codigo):
    return StatusSocioConstituido.get(codigo, 'CODIGO NAO ENCONTRADO')

def buscaQuadroAdminBaseJunta(codigo):
    return QuadroAdminBaseJunta.get(codigo, 'CODIGO NAO ENCONTRADO')

def buscaTipoDctoAdmin(codigo):
    return TipoDctoAdmin.get(codigo, 'SEQUÊNCIA QUANDO DA UTILIZAÇÂO DE DOCUMENTO DE TERCEIROS')

def buscaSituacaoAdmin(codigo):
    return SituacaoAdmin.get(codigo, 'CODIGO NAO ENCONTRADO')

def buscaStatusAdminConstituido(codigo):
    return StatusAdminConstituido.get(codigo, 'CODIGO NAO ENCONTRADO')

def buscaBaseJunta(codigo):
    return BaseJunta.get(codigo, 'CODIGO NAO ENCONTRADO')

def buscaTipoDctoParticipada(codigo):
    return TipoDctoParticipada.get(codigo, 'SEQUÊNCIA QUANDO DA UTILIZAÇÂO DE DOCUMENTO DE TERCEIROS')

def buscaSituacaoParticipada(codigo):
    return SituacaoParticipada.get(codigo, 'CODIGO NAO ENCONTRADO')

def buscaTipoDctoParticipante(codigo):
    return TipoDctoParticipante.get(codigo, 'SEQUÊNCIA QUANDO DA UTILIZAÇÂO DE DOCUMENTO DE TERCEIROS')

def buscaSituacaoParticipante(codigo):
    return SituacaoParticipante.get(codigo, 'CODIGO NAO ENCONTRADO')

def buscaTipoSocio(codigo):
    return TipoSocio.get(codigo, 'CODIGO NAO ENCONTRADO')

def buscaTipoPrazo(codigo):
    return TipoPrazo.get(codigo, 'CODIGO NAO ENCONTRADO')

def buscaTipoSinalDiasAtraso(codigo):
    return TipoSinalDiasAtraso.get(codigo, 'CODIGO NAO ENCONTRADO')

def buscaRetornoModVerifTitulo(codigo):
    return RetornoModVerifTitulo.get(codigo, 'CODIGO NAO ENCONTRADO')

def buscaTipoEmpresa(codigo):
    return TipoEmpresa.get(codigo, 'CODIGO NAO ENCONTRADO')

def buscaTipoPessoa(codigo):
    return TipoPessoa.get(codigo, 'CODIGO NAO ENCONTRADO')

def buscaTipoConsulta(codigo):
    return TipoConsulta.get(codigo, 'CODIGO NAO ENCONTRADO')

def buscaTipoNaturezaModalidadeCONVEMPEFIN(codigo):
    return TipoNaturezaModalidadeCONVEMPEFIN.get(codigo, 'CODIGO NAO ENCONTRADO')

def buscaTipoNaturezaCONCENTRE(codigo):
    return TipoNaturezaCONCENTRE.get(codigo, 'CODIGO NAO ENCONTRADO')

def buscaTipoCartaAnuencia(codigo):
    return TipoCartaAnuencia.get(codigo, 'CODIGO NAO ENCONTRADO')

def buscaTipoProtesto(codigo):
    return TipoProtesto.get(codigo, 'CODIGO NAO ENCONTRADO')

def buscaTipoAcao(codigo):
    return TipoAcao.get(codigo, 'CODIGO NAO ENCONTRADO')

def buscaTipoFalenciaConcordata(codigo):
    return TipoFalenciaConcordata.get(codigo, 'CODIGO NAO ENCONTRADO')

def buscaTipoPIE(codigo):
    return TipoPIE.get(codigo, 'CODIGO NAO ENCONTRADO')

def buscaTipoACHEI(codigo):
    return TipoACHEI.get(codigo, 'CODIGO NAO ENCONTRADO')

def buscaTipoCCF(codigo):
    return TipoCCF.get(codigo, 'CODIGO NAO ENCONTRADO')

def buscaTipoSRF(codigo):
    return TipoSRF.get(codigo, 'CODIGO NAO ENCONTRADO')

def buscaTipoCONVEMDevedores(codigo):
    return TipoCONVEMDevedores.get(codigo, 'CODIGO NAO ENCONTRADO')

def buscaTipoQualifParticEmpFalida(codigo):
    return TipoQualifParticEmpFalida.get(codigo, 'CODIGO NAO ENCONTRADO')

def buscaTipoNaturezaRestricoesFinanREFIN(codigo):
    return TipoNaturezaRestricoesFinanREFIN.get(codigo, 'CODIGO NAO ENCONTRADO')

def buscaTipoMensagemPontualidade(codigo):
    return TipoMensagemPontualidade.get(codigo, 'CODIGO NAO ENCONTRADO')

def buscaTipoSimplesNacional(codigo):
    return TipoSimplesNacional.get(codigo, 'CODIGO NAO ENCONTRADO')

def buscaTipoCodAlerta(codigo):
    return TipoCodAlerta.get(codigo, 'CODIGO NAO ENCONTRADO')

def buscaTipoCodSetor(codigo):
    return TipoCodSetor.get(codigo, 'CODIGO NAO ENCONTRADO')

def buscaTipoCodRetornoMonitore(codigo):
    return TipoCodRetornoMonitore.get(codigo, 'CODIGO NAO ENCONTRADO')

def buscaTipoTipoOperacao(codigo):
    return TipoOperacao.get(codigo, 'CODIGO NAO ENCONTRADO')

def buscaTipoRegistroLayout(codigo):
    return TipoRegistroLayout.get(codigo, 'CODIGO NAO ENCONTRADO')

def buscaTipoLinhaLayout(codigo):
    return TipoLinhaLayout.get(codigo, 'CODIGO NAO ENCONTRADO')

def buscaTipoAtributoLayout(codigo):
    return TipoAtributoLayout.get(codigo, 'CODIGO NAO ENCONTRADO')

####################################################################################################
#Dicionário para mapear códigos de registro para nomes descritivos
####################################################################################################
NomesBlocos = {
    #Dados Cadastrais
    "010000": {"Grupo": "DadosCadastrais", "Item": "DadosControleEmpresa"},
    "010100": {"Grupo": "DadosCadastrais", "Item": "FraseStatusEmpresa"},
    "010101": {"Grupo": "DadosCadastrais", "Item": "Contabilizacao"},
    "010102": {"Grupo": "DadosCadastrais", "Item": "Identificacao"},
    "010103": {"Grupo": "DadosCadastrais", "Item": "Endereco"},
    "010104": {"Grupo": "DadosCadastrais", "Item": "Localizacao"},
    "010105": {"Grupo": "DadosCadastrais", "Item": "Atividade"},
    "010106": {"Grupo": "DadosCadastrais", "Item": "Filiais"},
    "010107": {"Grupo": "DadosCadastrais", "Item": "PrincipaisProdutos"},
    "010108": {"Grupo": "DadosCadastrais", "Item": "ControleSocietUltAtual"},
    "010109": {"Grupo": "DadosCadastrais", "Item": "ControleSocietDetSocios"},
    "010110": {"Grupo": "DadosCadastrais", "Item": "QuadroAdminUltAtual"},
    "010111": {"Grupo": "DadosCadastrais", "Item": "QuadroAdminDetalhes"},
    "010112": {"Grupo": "DadosCadastrais", "Item": "PartUltAtualizacao"},
    "010113": {"Grupo": "DadosCadastrais", "Item": "ParticipadaDetalhes"},
    "010114": {"Grupo": "DadosCadastrais", "Item": "ParticipanteDetalhes"},
    "010115": {"Grupo": "DadosCadastrais", "Item": "NomesSemelhantes"},
    "010116": {"Grupo": "DadosCadastrais", "Item": "Antecessora"},
    "010117": {"Grupo": "DadosCadastrais", "Item": "SociosPFNovoQuadroSocial"},
    "010118": {"Grupo": "DadosCadastrais", "Item": "SociosPFComplNovoQuadroSocial"},
    "010119": {"Grupo": "DadosCadastrais", "Item": "SociosPJComplNovoQuadroSocial"},
    "010120": {"Grupo": "DadosCadastrais", "Item": "SociosPJComplNovoQuadroSocial"},
    "010121": {"Grupo": "DadosCadastrais", "Item": "VeiculosBensSociosAdm"},
    "010122": {"Grupo": "DadosCadastrais", "Item": "QuadroSocialJunta"},
    "010198": {"Grupo": "DadosCadastrais", "Item": "ObsCadIncorpFusaoCisao"},
    
    #Dados Comerciais
    "020100": {"Grupo": "DadosComerciais", "Item": "PrincFornUltAtual"},
    "020101": {"Grupo": "DadosComerciais", "Item": "PrincFornecedores"},
    "020102": {"Grupo": "DadosComerciais", "Item": "RelFornecedores"},
    "020103": {"Grupo": "DadosComerciais", "Item": "RelFornecedoresPeriodo"},
    "020104": {"Grupo": "DadosComerciais", "Item": "RelFornecedoresMaisAntigo"},
    "021105": {"Grupo": "DadosComerciais", "Item": "HistPagtosValores"},
    "021106": {"Grupo": "DadosComerciais", "Item": "EvolCompromissosForn"},
    "021107": {"Grupo": "DadosComerciais", "Item": "ReferenciaisNegocios"},
    "021108": {"Grupo": "DadosComerciais", "Item": "HistPagtosQtdeTitulos"},
    "021109": {"Grupo": "DadosComerciais", "Item": "ReferenciaisNegociosAnalitico"},
    "021110": {"Grupo": "DadosComerciais", "Item": "CompromissosAnaliticos"},
    "021118": {"Grupo": "DadosComerciais", "Item": "HistPagtosValoresIndividuais"},
    "020119": {"Grupo": "DadosComerciais", "Item": "RelacFornIndividuais"},
    "023406": {"Grupo": "DadosComerciais", "Item": "TotalEvolCompromisso"},
    "023416": {"Grupo": "DadosComerciais", "Item": "TotalEvolCompromisso"},
    "023426": {"Grupo": "DadosComerciais", "Item": "TotalEvolCompromisso"},
    "025405": {"Grupo": "DadosComerciais", "Item": "AnaliseComparHistPagtos"},
    "025415": {"Grupo": "DadosComerciais", "Item": "AnaliseComparHistPagtos"},

    #Dados Comerciais - Segmento Consolidado
    "020111": {"Grupo": "DadosComercSegConsolidado", "Item": "PrincFornUltAtual"},
    "020112": {"Grupo": "DadosComercSegConsolidado", "Item": "PrincForn"},
    "020113": {"Grupo": "DadosComercSegConsolidado", "Item": "RelacForn"},
    "020134": {"Grupo": "DadosComercSegConsolidado", "Item": "RelacFornSubGrupo"},
    "020114": {"Grupo": "DadosComercSegConsolidado", "Item": "RelacFornSegPeriodo"},
    "020135": {"Grupo": "DadosComercSegConsolidado", "Item": "RelacFornPeriodoSubGrupo"},
    "021115": {"Grupo": "DadosComercSegConsolidado", "Item": "HistPagto"},
    "021136": {"Grupo": "DadosComercSegConsolidado", "Item": "HistPagtoSubGrupo"},
    "021116": {"Grupo": "DadosComercSegConsolidado", "Item": "EvolCompForn"},
    "021137": {"Grupo": "DadosComercSegConsolidado", "Item": "EvolCompFornSubGrupo"},
    "021120": {"Grupo": "DadosComercSegConsolidado", "Item": "EvolCompVencidos"},
    "021121": {"Grupo": "DadosComercSegConsolidado", "Item": "EvolCompAVencer"},
    "021122": {"Grupo": "DadosComercSegConsolidado", "Item": "RefNegociosAVista"},
    "021117": {"Grupo": "DadosComercSegConsolidado", "Item": "RefNegocios"},
    "021138": {"Grupo": "DadosComercSegConsolidado", "Item": "RefNegociosSubGrupo"},
    "021125": {"Grupo": "DadosComercSegConsolidado", "Item": "HisPagtosVisaoCedente"},
    "021126": {"Grupo": "DadosComercSegConsolidado", "Item": "EvolCompFornVisaoCedente"},
    "021127": {"Grupo": "DadosComercSegConsolidado", "Item": "RefNegociosVisaoCedente"},
    "021139": {"Grupo": "DadosComercSegConsolidado", "Item": "HistPagtoSubGrupoVisaoCedente"},
    "021140": {"Grupo": "DadosComercSegConsolidado", "Item": "EvolCompFornSubGrupoVisaoCedente"},
    "021141": {"Grupo": "DadosComercSegConsolidado", "Item": "RefNegociosSubGrupoVisaoCedente"},
    "020133": {"Grupo": "DadosComercSegConsolidado", "Item": "ModVerifTitulos"},
    "023405": {"Grupo": "DadosComercSegConsolidado", "Item": "TotalHistPagtos"},
    "023409": {"Grupo": "DadosComercSegConsolidado", "Item": "TotalHistPagtos"},
    "023410": {"Grupo": "DadosComercSegConsolidado", "Item": "TotalHistPagtos"},
    "023415": {"Grupo": "DadosComercSegConsolidado", "Item": "TotalHistPagtos"},
    "023418": {"Grupo": "DadosComercSegConsolidado", "Item": "TotalHistPagtos"},
    "023425": {"Grupo": "DadosComercSegConsolidado", "Item": "TotalHistPagtos"},
    "023436": {"Grupo": "DadosComercSegConsolidado", "Item": "TotalHistPagtos"},
    "023439": {"Grupo": "DadosComercSegConsolidado", "Item": "TotalHistPagtos"},

    #Informações de Consutas de Altertas
    "030101": {"Grupo": "DadosConsultasAltertas", "Item": "ConsultasSerasas"},
    "030102": {"Grupo": "DadosConsultasAltertas", "Item": "UltimasConsultas"},
    "030103": {"Grupo": "DadosConsultasAltertas", "Item": "FrasesAlerta"},
    "030201": {"Grupo": "DadosConsultasAltertas", "Item": "InfParticAlerta"},
    "030301": {"Grupo": "DadosConsultasAltertas", "Item": "ConsSerasaSintetico"},
    "030102": {"Grupo": "DadosConsultasAltertas", "Item": "ConsSerasaSintetico"},
    "030303": {"Grupo": "DadosConsultasAltertas", "Item": "UltConsSerasa"},
    "030304": {"Grupo": "DadosConsultasAltertas", "Item": "UltConsSerasa"},
    "030399": {"Grupo": "DadosConsultasAltertas", "Item": "InfGeraisDataAtual"},

    #Informações de Apontamentos
    "040101": {"Grupo": "DadosConsultasAltertas", "Item": "PEFIN"},
    "040102": {"Grupo": "DadosConsultasAltertas", "Item": "REFIN"},
    "040201": {"Grupo": "DadosConsultasAltertas", "Item": "ConcentreGrafias"},
    "040202": {"Grupo": "DadosConsultasAltertas", "Item": "ConcentreResumo"},
    "040301": {"Grupo": "DadosConsultasAltertas", "Item": "ConcenteProtestos"},
    "040401": {"Grupo": "DadosConsultasAltertas", "Item": "ConcentreAcaoJudiciai"},
    "040501": {"Grupo": "DadosConsultasAltertas", "Item": "ConcentrePartFalencia"},
    "040601": {"Grupo": "DadosConsultasAltertas", "Item": "ConcentreFalenciaConcordata"},
    "040701": {"Grupo": "DadosConsultasAltertas", "Item": "ConcentreDividasVencidas"},
    "040801": {"Grupo": "DadosConsultasAltertas", "Item": "RechequeChequeSemFundoAchei"},
    "040901": {"Grupo": "DadosConsultasAltertas", "Item": "RechequeChequeSemFundoAcheiCCF"},
    "041000": {"Grupo": "DadosConsultasAltertas", "Item": "RechequeQtdeUltOcorr"},
    "041001": {"Grupo": "DadosConsultasAltertas", "Item": "RechequeDetalhes"},
    "041101": {"Grupo": "DadosConsultasAltertas", "Item": "ParcitipAnotacoes"},

    #Mensagens de Bloco
    "010299": {"Grupo": "Mensagens", "Item": "Mensagem"},
    "010999": {"Grupo": "Mensagens", "Item": "Mensagem"},
    "011199": {"Grupo": "Mensagens", "Item": "Mensagem"},
    "011399": {"Grupo": "Mensagens", "Item": "Mensagem"},
    "011499": {"Grupo": "Mensagens", "Item": "Mensagem"},
    "040199": {"Grupo": "Mensagens", "Item": "Mensagem"},
    "040299": {"Grupo": "Mensagens", "Item": "Mensagem"},
    "041099": {"Grupo": "Mensagens", "Item": "Mensagem"},

    #RiskScoring => PRINAD = Probabilidade de Inadimplencia
    "070101": {"Grupo": "RiskScoring", "Item": "Prinad1Dec"},
    "070101": {"Grupo": "RiskScoring", "Item": "Prinad2Dec"},
    "070109": {"Grupo": "RiskScoring", "Item": "Prinad"},
    "070102": {"Grupo": "RiskScoring", "Item": "AutorizadorB"},
    "070103": {"Grupo": "RiskScoring", "Item": "AutorizadorPQ"},
    "070104": {"Grupo": "RiskScoring", "Item": "AutorizadorH"},
    "070105": {"Grupo": "RiskScoring", "Item": "AutorizadorE"},
    "070106": {"Grupo": "RiskScoring", "Item": "Prinad"},
    "070110": {"Grupo": "RiskScoring", "Item": "RiskScoringCustom"},
    "070111": {"Grupo": "RiskScoring", "Item": "PrinadCustom"},
    "070199": {"Grupo": "RiskScoring", "Item": "Autorizador"},
    "071099": {"Grupo": "RiskScoring", "Item": "RiskScoringCustom"},
    "070114": {"Grupo": "RiskScoring", "Item": "ClaseTextoExplic"},
    "070109": {"Grupo": "RiskScoring", "Item": "PositivoEmpresasCalculo"},
    "070106": {"Grupo": "RiskScoring", "Item": "PositivoEmpresasPrinad"},
    "070195": {"Grupo": "RiskScoring", "Item": "PositivoEmpresasMensagens"},
    "070199": {"Grupo": "RiskScoring", "Item": "PositivoEmpresasMsgNaoCalc"},
    "070401": {"Grupo": "RiskScoring", "Item": "ScoreSocios"},

    #Risco de Crédito
    "090101": {"Grupo": "RiscoCredito", "Item": "Calculo"},
    "090199": {"Grupo": "RiscoCredito", "Item": "Mensagem"},
    "090201": {"Grupo": "RiscoCredito", "Item": "CRE6"},
    "090299": {"Grupo": "RiscoCredito", "Item": "CRE6MsgGeral"},
    "090298": {"Grupo": "RiscoCredito", "Item": "CRE6MsgEstado"},
    "090297": {"Grupo": "RiscoCredito", "Item": "CRE6MsgEstadoRegiao"},
    "930109": {"Grupo": "RiscoCredito", "Item": "EmpresaSetorCalculo"},
    "930106": {"Grupo": "RiscoCredito", "Item": "EmpresaSetorPrinad"},
    "930114": {"Grupo": "RiscoCredito", "Item": "ClaseTextoExplic"},
    "930199": {"Grupo": "RiscoCredito", "Item": "ScoreEmpresaSetor"},
    "930201": {"Grupo": "RiscoCredito", "Item": "ScoreEmpresaSetor"},
    "930299": {"Grupo": "RiscoCredito", "Item": "ScoreEmpresaSetorMsgGeral"},
    "930298": {"Grupo": "RiscoCredito", "Item": "ScoreEmpresaSetorMsgEstado"},
    "930297": {"Grupo": "RiscoCredito", "Item": "ScoreEmpresaSetorMsgEstadoRegiao"},

    #Gasto Estimado
    "100101": {"Grupo": "GastoEstimado", "Item": "Valor"},
    "100102": {"Grupo": "GastoEstimado", "Item": "Mensagem"},
    "100199": {"Grupo": "GastoEstimado", "Item": "MensagemNaoCalculo"},

    #Alerta Identidade PJ
    "110101": {"Grupo": "AlertaIdentidadePJ", "Item": "Pontuacao"},
    "110102": {"Grupo": "AlertaIdentidadePJ", "Item": "MsgFiltro"},
    "110103": {"Grupo": "AlertaIdentidadePJ", "Item": "TextoExplic"},
    "110199": {"Grupo": "AlertaIdentidadePJ", "Item": "MensagemNaoCalculo"},

    #Mosaic PJ
    "120101": {"Grupo": "MosaicPJ", "Item": "Dados"},
    "120199": {"Grupo": "MosaicPJ", "Item": "Mensagem"},

    #Orgãos Publicos
    "120201": {"Grupo": "OrgaosPublicos", "Item": "Dados"},
    "120202": {"Grupo": "OrgaosPublicos", "Item": "Totais"},
    "120299": {"Grupo": "OrgaosPublicos", "Item": "Mensagem"},

    #Pontualidade Pagto PJ
    "130101": {"Grupo": "PontualidadePagtoPJ", "Item": "Dados"},
    "130199": {"Grupo": "PontualidadePagtoPJ", "Item": "Mensagem"},

    #Risco Novas Empresas
    "140101": {"Grupo": "RiscoNovasEmpresas", "Item": "Dados"},
    "140103": {"Grupo": "RiscoNovasEmpresas", "Item": "Filtros"},
    "140199": {"Grupo": "RiscoNovasEmpresas", "Item": "Mensagem"},

    #Feature Capacidade Mensal de Pagamento PJ
    "140101": {"Grupo": "CapacidadeMensalPagtoPJ", "Item": "Calculo"},
    "140103": {"Grupo": "CapacidadeMensalPagtoPJ", "Item": "CalculoFiltro"},
    "140199": {"Grupo": "CapacidadeMensalPagtoPJ", "Item": "Mensagem"},

    #Endereços e Telefones alternativos
    "280101": {"Grupo": "EndFonesAltern", "Item": "EnderecosP1"},
    "280102": {"Grupo": "EndFonesAltern", "Item": "EnderecosP2"},
    "280199": {"Grupo": "EndFonesAltern", "Item": "EnderecosMensagens"},
    "290101": {"Grupo": "EndFonesAltern", "Item": "Telefones"},
    "290199": {"Grupo": "EndFonesAltern", "Item": "TelefonesMensagens"},

    #Situacao Fiscal
    "270101": {"Grupo": "SituacaoFiscal", "Item": "ReceitaIdentificacao"},
    "270102": {"Grupo": "SituacaoFiscal", "Item": "ReceitaCNAEsSec"},
    "270103": {"Grupo": "SituacaoFiscal", "Item": "ReceitaMensagens"},
    "270104": {"Grupo": "SituacaoFiscal", "Item": "SintegraSEFAZSituacao"},
    "270105": {"Grupo": "SituacaoFiscal", "Item": "SintegraSEFAZIdentificacao"},
    "270106": {"Grupo": "SituacaoFiscal", "Item": "SintegraSEFAZAtividadeEconon"},
    "270107": {"Grupo": "SituacaoFiscal", "Item": "SintegraSEFAZObservacoes"},
    "270108": {"Grupo": "SituacaoFiscal", "Item": "SintegraSEFAZMensagens"},
    "270109": {"Grupo": "SituacaoFiscal", "Item": "SUFRAMAIdentSituacao"},
    "270110": {"Grupo": "SituacaoFiscal", "Item": "SUFRAMAMensagens"},
    "270199": {"Grupo": "SituacaoFiscal", "Item": "MensagemGeral"},

    #Faturamento Estimado com Positivo
    "300201": {"Grupo": "FaturamentoEstimadoPositivo", "Item": "Identificacao"},
    "300202": {"Grupo": "FaturamentoEstimadoPositivo", "Item": "Valor"},
    "300203": {"Grupo": "FaturamentoEstimadoPositivo", "Item": "MotivoNaoCalculo"},
    "300299": {"Grupo": "FaturamentoEstimadoPositivo", "Item": "Mensagens"},

    #Perfil Financeiro
    "300901": {"Grupo": "PerfilFinanceiro", "Item": "IdentifEmpresa"},
    "300902": {"Grupo": "PerfilFinanceiro", "Item": "ControleBalanco"},
    "300903": {"Grupo": "PerfilFinanceiro", "Item": "ContasAtivo"},
    "300904": {"Grupo": "PerfilFinanceiro", "Item": "ContasPassivo"},
    "300905": {"Grupo": "PerfilFinanceiro", "Item": "ConstasDemonstrativoResultado"},
    "300906": {"Grupo": "PerfilFinanceiro", "Item": "IndicesFinanceiros"},
    "300907": {"Grupo": "PerfilFinanceiro", "Item": "Conclusao"},

    #Histórico de Pagamento Financeiro – Avançado
    "320101": {"Grupo": "HistPagtosAvancado", "Item": "CompPorLinhaCred"},
    "320102": {"Grupo": "HistPagtosAvancado", "Item": "QtdeCompCredores"},
    "320103": {"Grupo": "HistPagtosAvancado", "Item": "PercParcelasComp"},
    "320104": {"Grupo": "HistPagtosAvancado", "Item": "CompPagosUlt5Anos"},
    "320199": {"Grupo": "HistPagtosAvancado", "Item": "Mensagens"},
    "320201": {"Grupo": "HistPagtosAvancado", "Item": "CompAtivosPorLInhaCred"},
    "320202": {"Grupo": "HistPagtosAvancado", "Item": "QtdeCompCredores"},
    "320203": {"Grupo": "HistPagtosAvancado", "Item": "PercParcelasCompAtivos"},
    "320204": {"Grupo": "HistPagtosAvancado", "Item": "ContratosAtivos"},
    "320205": {"Grupo": "HistPagtosAvancado", "Item": "PontualidadePagto"},
    "320206": {"Grupo": "HistPagtosAvancado", "Item": "VctosAbertos"},
    "320297": {"Grupo": "HistPagtosAvancado", "Item": "MsgPontualidadePagto"},
    "320298": {"Grupo": "HistPagtosAvancado", "Item": "MsgVctoAberto"},
    "320299": {"Grupo": "HistPagtosAvancado", "Item": "MsgContratosAtivos"},

    #Alerta Cadastral da Empresa
    "600099": {"Grupo": "AlertaCadastral", "Item": "EmpMsgGeral"},
    "610099": {"Grupo": "AlertaCadastral", "Item": "SociosAdminMsgGeral"},
    "600101": {"Grupo": "AlertaCadastral", "Item": "EmpConsAltRazaoSocial"},
    "600102": {"Grupo": "AlertaCadastral", "Item": "EmpAltRazaoSocial"},
    "600199": {"Grupo": "AlertaCadastral", "Item": "EmpMensagens"},
    "600201": {"Grupo": "AlertaCadastral", "Item": "EmpConsAltRamoAtividade"},
    "600202": {"Grupo": "AlertaCadastral", "Item": "EmpAltRamoAtividade"},
    "600299": {"Grupo": "AlertaCadastral", "Item": "EmpMensagens"},
    "600301": {"Grupo": "AlertaCadastral", "Item": "EmpConsAltEndereco"},
    "600302": {"Grupo": "AlertaCadastral", "Item": "EmpAltEndereco"},
    "600399": {"Grupo": "AlertaCadastral", "Item": "EmpMensagens"},
    "600401": {"Grupo": "AlertaCadastral", "Item": "EmpConsAltTipoSocietario"},
    "600402": {"Grupo": "AlertaCadastral", "Item": "EmpAltTipoSocietario"},
    "600499": {"Grupo": "AlertaCadastral", "Item": "EmpMensagens"},
    "600501": {"Grupo": "AlertaCadastral", "Item": "EmpConsAltEnquadFiscal"},
    "600502": {"Grupo": "AlertaCadastral", "Item": "EmpAltEnquadFiscal"},
    "600599": {"Grupo": "AlertaCadastral", "Item": "EmpMensagens"},
    "600601": {"Grupo": "AlertaCadastral", "Item": "EmpConsPresCadCGU"},
    "600699": {"Grupo": "AlertaCadastral", "Item": "EmpMensagens"},
    "600701": {"Grupo": "AlertaCadastral", "Item": "EmpConsInconsistComerciais"},
    "600702": {"Grupo": "AlertaCadastral", "Item": "EmpInconsistComerciais"},
    "600799": {"Grupo": "AlertaCadastral", "Item": "Mensagens"},

    #Alerta Cadastral dos Sócios e Administradores
    "610101": {"Grupo": "AlertaCadastralSocios", "Item": "ConsAltSocios"},
    "610102": {"Grupo": "AlertaCadastralSocios", "Item": "AltSocios"},
    "610199": {"Grupo": "AlertaCadastralSocios", "Item": "Mensagens"},
    "610201": {"Grupo": "AlertaCadastralSocios", "Item": "ConsAltAdmin"},
    "610202": {"Grupo": "AlertaCadastralSocios", "Item": "AltAdmin"},
    "610299": {"Grupo": "AlertaCadastralSocios", "Item": "Mensagens"},
    "610301": {"Grupo": "AlertaCadastralSocios", "Item": "ConsInconsistSocietariasPJ"},
    "610302": {"Grupo": "AlertaCadastralSocios", "Item": "InconsistSocietariasPJ"},
    "610399": {"Grupo": "AlertaCadastralSocios", "Item": "Mensagens"},
    "610401": {"Grupo": "AlertaCadastralSocios", "Item": "ConsInconsistAdminPJ"},
    "610402": {"Grupo": "AlertaCadastralSocios", "Item": "InconsistAdminPJ"},
    "610499": {"Grupo": "AlertaCadastralSocios", "Item": "Mensagens"},
    "610501": {"Grupo": "AlertaCadastralSocios", "Item": "ConsPresencaObitosSociosPF"},
    "610502": {"Grupo": "AlertaCadastralSocios", "Item": "PresencaObitosSociosPF"},
    "610599": {"Grupo": "AlertaCadastralSocios", "Item": "Mensagens"},
    "610601": {"Grupo": "AlertaCadastralSocios", "Item": "ConsPresencaObitosAdminPF"},
    "610602": {"Grupo": "AlertaCadastralSocios", "Item": "PresencaObitosAdminPF"},
    "610699": {"Grupo": "AlertaCadastralSocios", "Item": "Mensagens"},

    #Indice de Relacionamento com o mercado (IRM)
    "301001": {"Grupo": "IndiceRelacionamentoMercado", "Item": "IRM"},
    "301099": {"Grupo": "IndiceRelacionamentoMercado", "Item": "MsgNaoCalculo"},
    "301301": {"Grupo": "IndiceRelacionamentoMercado", "Item": "IRMGeral"},
    "301399": {"Grupo": "IndiceRelacionamentoMercado", "Item": "Mensagens"},

    #Indicador de Recuperação de Crédito
    "530101": {"Grupo": "IndicadorRecupecaoCredito", "Item": "IRC"},
    "530199": {"Grupo": "IndicadorRecupecaoCredito", "Item": "Mensagens"},

    #Alertscoring
    "550101": {"Grupo": "Alertscoring", "Item": "Calculo"},
    "550199": {"Grupo": "Alertscoring", "Item": "Mensagens"},

    #Limite de crédito PJ
    "560102": {"Grupo": "LimiteCreditoPJ", "Item": "Calculo"},
    "560104": {"Grupo": "LimiteCreditoPJ", "Item": "Mensagens"},

    #Inscrição Estadual
    "571001": {"Grupo": "InscricaoEstadual", "Item": "Informacoes"},

    #Informações de Monitore Gerencie Carteira
    "080102": {"Grupo": "MonitoreGerencieCarteira", "Item": "Dados"},

    #Informações do SPC
    "901001": {"Grupo": "InformacoesSPC", "Item": "Anotacoes1"},
    "901002": {"Grupo": "InformacoesSPC", "Item": "Anotacoes2"},
    "901003": {"Grupo": "InformacoesSPC", "Item": "TotaisQtdes"},
    "901099": {"Grupo": "InformacoesSPC", "Item": "MsgAnotacoes"},
    "907001": {"Grupo": "InformacoesSPC", "Item": "ConsultasSPC"},
    "907002": {"Grupo": "InformacoesSPC", "Item": "TotaisConsMes"},
    "907099": {"Grupo": "InformacoesSPC", "Item": "Mensagens"},

    #Anotações e Consultas SPC
    "911101": {"Grupo": "AnotacoesConsultasSPC", "Item": "Anotacoes1"},
    "911102": {"Grupo": "AnotacoesConsultasSPC", "Item": "Anotacoes2"},
    "911103": {"Grupo": "AnotacoesConsultasSPC", "Item": "TotaisQtdes"},
    "911199": {"Grupo": "AnotacoesConsultasSPC", "Item": "MsgAnotacoes"},
    "918001": {"Grupo": "AnotacoesConsultasSPC", "Item": "ConsultasSPC"},
    "918002": {"Grupo": "AnotacoesConsultasSPC", "Item": "TotaisConsMes"},
    "918099": {"Grupo": "AnotacoesConsultasSPC", "Item": "Mensagens"},

    #Comportamento de Pagamento do Setor
    "310101": {"Grupo": "ComportamentoPagtoSetor", "Item": "PagtosAtrasoDiasPecMed"},
    "310102": {"Grupo": "ComportamentoPagtoSetor", "Item": "VctoFuturosAtrasoDiasPecMed"},
    "310199": {"Grupo": "ComportamentoPagtoSetor", "Item": "MsgNaoCalculo"},

    #Vendas com Cartão
    "700001": {"Grupo": "VendasCartao", "Item": "DadosEmpresa"},
    "700002": {"Grupo": "VendasCartao", "Item": "DadosEmpresaCont"},
    "700003": {"Grupo": "VendasCartao", "Item": "FaixaUtilizacao"},
    "700099": {"Grupo": "VendasCartao", "Item": "Mensagens"},

    #SPC Sócios e Administradores
    "920001": {"Grupo": "SPCSociosAdmin", "Item": "QtdeAnotacoes"},
    "920002": {"Grupo": "SPCSociosAdmin", "Item": "Anotacao"},
    "920099": {"Grupo": "SPCSociosAdmin", "Item": "MsgIndispInf"},

    #Anotações e Consultas SPC Sócios e Administradores
    "925001": {"Grupo": "SPCAnotacoesSociosAdmin", "Item": "QtdeAnotacoes"},
    "925002": {"Grupo": "SPCAnotacoesSociosAdmin", "Item": "Anotacao"},
    "925099": {"Grupo": "SPCAnotacoesSociosAdmin", "Item": "MsgIndispInf"},
    "926001": {"Grupo": "SPCAnotacoesSociosAdmin", "Item": "ConsultasSPC"},
    "926002": {"Grupo": "SPCAnotacoesSociosAdmin", "Item": "ConsultasSPC"},
    "926003": {"Grupo": "SPCAnotacoesSociosAdmin", "Item": "TotaisConsultasSPCMes"},
    "926099": {"Grupo": "SPCAnotacoesSociosAdmin", "Item": "MsgConsultaSPC"},

    #Indicador de recuperação de dívidas
    "580101": {"Grupo": "IndicadorRecuperacaoDividas", "Item": "IndicadorPEFINREFINDivVencidas"},
    "580199": {"Grupo": "IndicadorRecuperacaoDividas", "Item": "Mensagens"},
}

def buscaNomesBlocos(codigo):
    bloco = NomesBlocos.get(codigo)
    if bloco:
        return bloco["Grupo"], bloco["Item"]
    else:
        return f'Dados{codigo}', f'Dados{codigo}'
