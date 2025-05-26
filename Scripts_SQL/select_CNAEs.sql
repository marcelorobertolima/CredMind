/*
select * from cnae_secoes with (nolock) where ID = 'J'
select * from cnae_divisoes with (nolock) where ID = '62'
select * from cnae_grupos with (nolock) where ID = '620'
select * from cnae_classes with (nolock) where ID = '62091'
select * from cnae_subclasses with (nolock) where id = '6209100'
*/

--EXEC stoBuscaCNAE @CNAE = '6209100';

ALTER PROCEDURE stoBuscaCNAE(@CNAE AS VARCHAR(50))
AS
SELECT      cnae_subclasses.id          AS ID_SubClasse,
            cnae_subclasses.descricao   AS Desc_SubClasse,
            cnae_classes.id             AS ID_Classe,
            cnae_classes.descricao      AS Desc_Classe,
            cnae_grupos.id              AS ID_Grupo,
            cnae_grupos.descricao       AS Desc_Grupo,
            cnae_divisoes.id            AS ID_Divisao,
            cnae_divisoes.descricao     AS Desc_Divisao,
            cnae_secoes.id              AS ID_Secao,
            cnae_secoes.descricao       AS Desc_Secao
FROM        cnae_subclasses             WITH (NOLOCK)
INNER JOIN  cnae_classes                WITH (NOLOCK)
ON          cnae_subclasses.classe_id   = cnae_classes.id
INNER JOIN  cnae_grupos                 WITH (NOLOCK)
ON          cnae_classes.grupo_id       = cnae_grupos.id
INNER JOIN  cnae_divisoes               WITH (NOLOCK)
ON          cnae_grupos.divisao_id      = cnae_divisoes.id
INNER JOIN  cnae_secoes                 WITH (NOLOCK)
ON          cnae_divisoes.secao_id      = cnae_secoes.id
WHERE       cnae_subclasses.id          = @CNAE
