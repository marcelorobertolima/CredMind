import json
from django.db import transaction, connection
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from APICredMind.models import CnaeSecao, CnaeDivisao, CnaeGrupo, CnaeClasse, CnaeSubclasse
from APICredMind.views.PoliticaConsultas.Consulta_DadosBasicos import Consulta_DadosBasicosEmpresa
from APICredMind.serializers import EnriquecimentoCNAECedentesOperaSerializer

import pyodbc
from django.conf import settings

class obterCNAE(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        try:
            file_path = r"C:\Users\marcelo.l\OneDrive\CredMind\CredMind\CredMindBackend\pCredMind\cnae_data.json"
            with open(file_path, "r", encoding="utf-8") as json_file:
                data = json.load(json_file)

            secao_ids = set(CnaeSecao.objects.values_list("id", flat=True))
            divisao_ids = set(CnaeDivisao.objects.values_list("id", flat=True))
            grupo_ids = set(CnaeGrupo.objects.values_list("id", flat=True))
            classe_ids = set(CnaeClasse.objects.values_list("id", flat=True))
            subclasse_ids = set(CnaeSubclasse.objects.values_list("id", flat=True))

            secoes_to_insert = []
            divisoes_to_insert = []
            grupos_to_insert = []
            classes_to_insert = []
            sub_classes_to_insert = []

            for item in data:
                secao_id = item['classe']['grupo']['divisao']['secao']['id']
                secao_descricao = item['classe']['grupo']['divisao']['secao']['descricao']
                if secao_id not in secao_ids:
                    secoes_to_insert.append((secao_id, secao_descricao))

                divisao_id = item['classe']['grupo']['divisao']['id']
                divisao_descricao = item['classe']['grupo']['divisao']['descricao']
                if divisao_id not in divisao_ids:
                    divisoes_to_insert.append((divisao_id, divisao_descricao, secao_id))

                grupo_id = item['classe']['grupo']['id']
                grupo_descricao = item['classe']['grupo']['descricao']
                if grupo_id not in grupo_ids:
                    grupos_to_insert.append((grupo_id, grupo_descricao, divisao_id))

                classe_id = item['classe']['id']
                classe_descricao = item['classe']['descricao']
                if classe_id not in classe_ids:
                    classes_to_insert.append((classe_id, classe_descricao, grupo_id))

                subclasse_id = item['id']
                subclasse_descricao = item['descricao']
                if subclasse_id not in subclasse_ids:
                    sub_classes_to_insert.append((subclasse_id, subclasse_descricao, classe_id))

            # INSERIR COM MERGE PARA SQL SERVER
            with transaction.atomic(), connection.cursor() as cursor:
                if secoes_to_insert:
                    for secao in secoes_to_insert:
                        cursor.execute("""
                            MERGE INTO dbo.cnae_secoes AS target
                            USING (SELECT %s AS id, %s AS descricao) AS source
                            ON target.id = source.id
                            WHEN NOT MATCHED THEN
                                INSERT (id, descricao) VALUES (source.id, source.descricao);
                        """, secao)

                if divisoes_to_insert:
                    for divisao in divisoes_to_insert:
                        cursor.execute("""
                            MERGE INTO dbo.cnae_divisoes AS target
                            USING (SELECT %s AS id, %s AS descricao, %s AS secao_id) AS source
                            ON target.id = source.id
                            WHEN NOT MATCHED THEN
                                INSERT (id, descricao, secao_id) VALUES (source.id, source.descricao, source.secao_id);
                        """, divisao)

                if grupos_to_insert:
                    for grupo in grupos_to_insert:
                        cursor.execute("""
                            MERGE INTO dbo.cnae_grupos AS target
                            USING (SELECT %s AS id, %s AS descricao, %s AS divisao_id) AS source
                            ON target.id = source.id
                            WHEN NOT MATCHED THEN
                                INSERT (id, descricao, divisao_id) VALUES (source.id, source.descricao, source.divisao_id);
                        """, grupo)

                if classes_to_insert:
                    for classe in classes_to_insert:
                        cursor.execute("""
                            MERGE INTO dbo.cnae_classes AS target
                            USING (SELECT %s AS id, %s AS descricao, %s AS grupo_id) AS source
                            ON target.id = source.id
                            WHEN NOT MATCHED THEN
                                INSERT (id, descricao, grupo_id) VALUES (source.id, source.descricao, source.grupo_id);
                        """, classe)

                if sub_classes_to_insert:
                    for subclasse in sub_classes_to_insert:
                        cursor.execute("""
                            MERGE INTO dbo.cnae_subclasses AS target
                            USING (SELECT %s AS id, %s AS descricao, %s AS classe_id) AS source
                            ON target.id = source.id
                            WHEN NOT MATCHED THEN
                                INSERT (id, descricao, classe_id) VALUES (source.id, source.descricao, source.classe_id);
                        """, subclasse)

            return Response({"detail": "Dados processados com sucesso."}, status=status.HTTP_200_OK)

        except FileNotFoundError:
            return Response({"error": "Arquivo JSON não encontrado."}, status=status.HTTP_400_BAD_REQUEST)
        except json.JSONDecodeError:
            return Response({"error": "Erro ao decodificar o JSON."}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

###########################################################################################################################
###########################################################################################################################
###########################################################################################################################
class eriqueceCNAE(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        try:
            auth_header = request.headers.get('Authorization')

            if not auth_header:
                return Response({"error": "Authorization header is missing."}, status=status.HTTP_401_UNAUTHORIZED)

            #Carrega os Cedentes via stoCedentes
            cedentes = obterCedentes()

            #Faz loop por CNPJ
            for cedente in cedentes:
                codigoCedente = cedente["Codigo_Cedente"]
                cnpj_Cedente = cedente["CNPJ_Cedente"]
                nome_Cedente = cedente["Nome_Cedente"]

                #Consome a Consulta_DadosBasicosEmpresa
                if not auth_header:
                    return Response({"error": "Authorization header is missing."}, status=status.HTTP_401_UNAUTHORIZED)
                
                DadosRetorno = Consulta_DadosBasicosEmpresa(cnpj_Cedente, auth_header, "basic_data", None)

                result = DadosRetorno.get('DadosEmpresa', {}).get('Result', [])

                if result:
                    basic_data = result[0].get("BasicData", {})
                    activities = basic_data.get("Activities", [])

                #Pega o CNAE do retorno
                for activity in activities:
                    isMain = activity.get("IsMain")
                    activities_code = activity.get("Code")
                    activity_name = activity.get("Activity")

                    #Busca Estrutura através da stoBuscaCNAE
                    dadosCNAE = obterDadosCNAE(activities_code)

                    #Criar o json para salvar na base de dados
                    dadosCedentes = {
                        "CNPJCedente": cnpj_Cedente,
                        "CodCedente": codigoCedente,
                        "NomeCedente": nome_Cedente,
                        "Primario": isMain
                    }

                    DadosCedentesGravacao = {**dadosCedentes, **dadosCNAE}

                    #Grava os dados na nova Tabela EnriquecimentoCedentesOpera
                    #CodigoPessoa, CNPJ e a estrutura do CNAE
                    enriquecimentoSerializer = EnriquecimentoCNAECedentesOperaSerializer(data=DadosCedentesGravacao)

                    if enriquecimentoSerializer.is_valid():
                        enriquecimentoSerializer.save()

            return Response({"detail": "Dados enriquecidos com sucesso."}, status=status.HTTP_200_OK)

            #Atualiza Qprof com o CNAE enriquecido
            #A implementar
            
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

########################################################################################################
########################################################################################################
########################################################################################################
def obterCedentes():
    try:
        with connection.cursor() as cursor:
            # Chama a stored procedure 'stoCedentes' sem parâmetros
            cursor.execute("EXEC stoCedentes")  # Ou EXEC nome_da_procedure caso tenha parâmetros
            resultados = cursor.fetchall()  # Obtém os resultados

        lista_cedentes = []

        for row in resultados:
            codigo_cedente, cnpj_cedente, nome_cedente = row
            lista_cedentes.append({
                "Codigo_Cedente": codigo_cedente,
                "CNPJ_Cedente": cnpj_cedente,
                "Nome_Cedente": nome_cedente
            })

        return lista_cedentes

    except Exception as e:
        return f"Erro ao executar a stored procedure: {e}"

########################################################################################################
########################################################################################################
########################################################################################################
def obterDadosCNAE(CNAE):
    try:
        # Usando as configurações do banco de dados no settings.py
        conn = pyodbc.connect(
            f'DRIVER={{SQL Server}};'
            f'SERVER={settings.DATABASES["default"]["HOST"]};'
            f'DATABASE={settings.DATABASES["default"]["NAME"]};'
            f'UID={settings.DATABASES["default"]["USER"]};'
            f'PWD={settings.DATABASES["default"]["PASSWORD"]}'
        )
        
        SQL = "EXEC stoBuscaCNAE @CNAE = ?"
        
        cursor = conn.cursor()
        cursor.execute(SQL, (CNAE,))
        row = cursor.fetchone()

        if row:
            return {
                "ID_SubClasse": row[0],
                "Desc_SubClasse": row[1],
                "ID_Classe": row[2],
                "Desc_Classe": row[3],
                "ID_Grupo": row[4],
                "Desc_Grupo": row[5],
                "ID_Divisao": row[6],
                "Desc_Divisao": row[7],
                "ID_Secao": row[8],
                "Desc_Secao": row[9]
            }
        else:
            return None

    except Exception as e:
        return f"Erro ao executar a stored procedure: {e}"