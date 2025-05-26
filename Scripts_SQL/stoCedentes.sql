ALTER PROCEDURE stoCedentes
AS
select          --top 2
                stg_pessoa.CODIGO_PESSOA as Codigo_Cedente,
                case when stg_pessoa.TIPO_PESSOA = 'J' --PJ
                then
                    FORMAT(
                        CAST(
                            RIGHT('000000000' + CAST(stg_pessoajuridica.NUMERO_EST_CNPJ AS VARCHAR(8)), 8) + 
                            RIGHT('0000' + CAST(stg_pessoajuridica.NUMERO_FILIAL_CNPJ AS VARCHAR(4)), 4) + 
                            RIGHT('00' + CAST(stg_pessoajuridica.DIGITO_CNPJ AS VARCHAR(2)), 2)
                        AS BIGINT), 
                    '00000000000000'
                    )
                else --PF
                    FORMAT(
                            CAST(
                                RIGHT('000000000' + CAST(stg_pessoafisica.NUMERO_CPF AS VARCHAR(11)), 11) +
                                RIGHT('00' + CAST(stg_pessoafisica.DIGITO_CPF AS VARCHAR(11)), 11)
                            AS BIGINT), 
                            '00000000000'
                        )
                end AS CNPJ_Cedente,
                stg_pessoa.NOME_PESSOA as Nome_Cedente
from            csdados..stg_pessoa as stg_pessoa with (nolock)
left join       csdados..stg_pessoajuridica as stg_pessoajuridica with (nolock)
on              stg_pessoa.CODIGO_PESSOA = stg_pessoajuridica.CODIGO_PESSOA
left join       csdados..stg_pessoafisica as stg_pessoafisica with (nolock)
on              stg_pessoa.CODIGO_PESSOA = stg_pessoafisica.CODIGO_PESSOA
where           stg_pessoa.INDICADOR_PESSOA_CEDENTE = 'S'
and             stg_pessoa.CODIGO_PESSOA != 104086 --Gustavo
and             not exists (select  top 1 1
                            from    EnriquecimentoCNAECedentesOpera
                            where   stg_pessoa.CODIGO_PESSOA = EnriquecimentoCNAECedentesOpera.CodCedente
                            )