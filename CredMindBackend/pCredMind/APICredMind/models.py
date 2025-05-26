import json
from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager

##############################################################################
# Usuário customizado
##############################################################################
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    
    # Defina o campo de identificação como o email
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        try:
            return self.email
        except Exception as e:
            # Aqui, você pode registrar ou retornar algo como uma mensagem de erro
            return f"Erro ao acessar o email: {e}"

##############################################################################
# Tabela Consultas
##############################################################################
class Consultas(models.Model):
    id = models.BigAutoField(primary_key=True)
    id_consulta = models.CharField(max_length=64, blank=True, null=True)
    id_analise = models.CharField(max_length=64, blank=True, null=True)
    DataConsulta = models.DateTimeField(null=True, blank=True)
    Bureau = models.CharField(max_length=255, null=True, blank=True)
    Request = models.TextField(null=True, blank=True)  # Alterado para TextField para compatibilidade com SQL Server
    Response = models.TextField(null=True, blank=True)  # Alterado para TextField para compatibilidade com SQL Server

    class Meta:
        db_table = 'Consultas'

    def __str__(self):
        return self.id_consulta

##############################################################################
# Tabela Analises
##############################################################################
class Analises(models.Model):
    id = models.BigAutoField(primary_key=True)
    id_analise = models.CharField(max_length=64)
    DataConsulta = models.DateTimeField()
    Request = models.TextField()  # Alterado para TextField para compatibilidade com SQL Server
    Response = models.TextField()  # Alterado para TextField para compatibilidade com SQL Server

    class Meta:
        db_table = 'Analises'

    def __str__(self):
        return self.id_analise

##############################################################################
# Tabela ProspecSERASA
##############################################################################
class ProspecSERASA(models.Model):
    id = models.BigAutoField(primary_key=True)
    id_consulta = models.CharField(max_length=64)
    CNPJ = models.CharField(max_length=255, null=True, blank=True)
    RazaoSocial = models.CharField(max_length=255, null=True, blank=True)
    NomeFant = models.CharField(max_length=255, null=True, blank=True)
    Endereco = models.CharField(max_length=255, null=True, blank=True)
    Bairro = models.CharField(max_length=255, null=True, blank=True)
    Cidade = models.CharField(max_length=255, null=True, blank=True)
    UF = models.CharField(max_length=255, null=True, blank=True)
    CEP = models.CharField(max_length=255, null=True, blank=True)
    eMail = models.CharField(max_length=255, null=True, blank=True)
    DDD = models.CharField(max_length=255, null=True, blank=True)
    Telefone = models.CharField(max_length=255, null=True, blank=True)
    DataFundacao = models.CharField(max_length=255, null=True, blank=True)
    Ramo = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'ProspecSERASA'

    def __str__(self):
        return self.id_consulta

##############################################################################
# Tabela BlackListCNAE
##############################################################################
class BlackListCNAE(models.Model):
    id = models.BigAutoField(primary_key=True)
    idCNAE = models.CharField(max_length=10)
    Descricao = models.CharField(max_length=255)

    class Meta:
        db_table = 'BlackListCNAE'

    def __str__(self):
        return self.idCNAE

##############################################################################
# Tabela CnaeSecao
##############################################################################
class CnaeSecao(models.Model):
    id = models.BigAutoField(primary_key=True)
    descricao = models.TextField()

    class Meta:
        db_table = 'CnaeSecoes'
        indexes = [
            models.Index(fields=['id'])
        ]

    def __str__(self):
        return self.descricao

##############################################################################
# Tabela CnaeDivisao
##############################################################################
class CnaeDivisao(models.Model):
    id = models.BigAutoField(primary_key=True)
    descricao = models.TextField()
    secao = models.ForeignKey(CnaeSecao, related_name='divisoes', on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'CnaeDivisoes'
        indexes = [
            models.Index(fields=['secao'])
        ]

    def __str__(self):
        return self.descricao

##############################################################################
# Tabela CnaeGrupo
##############################################################################
class CnaeGrupo(models.Model):
    id = models.BigAutoField(primary_key=True)
    descricao = models.TextField()
    divisao = models.ForeignKey(CnaeDivisao, related_name='grupos', on_delete=models.SET_NULL, null=True)
    secao = models.ForeignKey(CnaeSecao, related_name='grupos', on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'CnaeGrupos'
        indexes = [
            models.Index(fields=['divisao', 'secao'])
        ]

    def __str__(self):
        return self.descricao

##############################################################################
# Tabela CnaeClasse
##############################################################################
class CnaeClasse(models.Model):
    id = models.BigAutoField(primary_key=True)
    descricao = models.TextField()
    grupo = models.ForeignKey(CnaeGrupo, related_name='classes', on_delete=models.SET_NULL, null=True)
    divisao = models.ForeignKey(CnaeDivisao, related_name='classes', on_delete=models.SET_NULL, null=True)
    secao = models.ForeignKey(CnaeSecao, related_name='classes', on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'CnaeClasses'
        indexes = [
            models.Index(fields=['grupo', 'divisao', 'secao'])
        ]

    def __str__(self):
        return self.descricao

##############################################################################
# Tabela CnaeSubclasse
##############################################################################
class CnaeSubclasse(models.Model):
    id = models.BigAutoField(primary_key=True)
    descricao = models.TextField()
    classe = models.ForeignKey(CnaeClasse, related_name='subclasses', on_delete=models.SET_NULL, null=True)
    grupo = models.ForeignKey(CnaeGrupo, related_name='subclasses', on_delete=models.SET_NULL, null=True)
    divisao = models.ForeignKey(CnaeDivisao, related_name='subclasses', on_delete=models.SET_NULL, null=True)
    secao = models.ForeignKey(CnaeSecao, related_name='subclasses', on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'CnaeSubclasses'
        indexes = [
            models.Index(fields=['classe', 'grupo', 'divisao', 'secao'])
        ]

    def __str__(self):
        return self.descricao

##############################################################################
# Tabela EnriquecimentoCNAECedentesOpera
##############################################################################
class EnriquecimentoCNAECedentesOpera(models.Model):
    CodCedente = models.CharField(max_length=255, null=True, blank=True)
    NomeCedente = models.CharField(max_length=255, null=True, blank=True)
    CNPJCedente = models.CharField(max_length=255, null=True, blank=True)
    ID_SubClasse = models.CharField(max_length=255, null=True, blank=True)
    Desc_SubClasse = models.CharField(max_length=255, null=True, blank=True)
    ID_Classe = models.CharField(max_length=255, null=True, blank=True)
    Desc_Classe = models.CharField(max_length=255, null=True, blank=True)
    ID_Grupo = models.CharField(max_length=255, null=True, blank=True)
    Desc_Grupo = models.CharField(max_length=255, null=True, blank=True)
    ID_Divisao = models.CharField(max_length=255, null=True, blank=True)
    Desc_Divisao = models.CharField(max_length=255, null=True, blank=True)
    ID_Secao = models.CharField(max_length=255, null=True, blank=True)
    Desc_Secao = models.CharField(max_length=255, null=True, blank=True)
    Primario = models.BooleanField(default=False, null=False, blank=False)

    class Meta:
        db_table = 'EnriquecimentoCNAECedentesOpera'

    def __str__(self):
        return self.NomeCedente
    
##############################################################################
# Tabela Relatorios
##############################################################################
class Relatorios(models.Model):
    id = models.BigAutoField(primary_key=True)
    id_consulta = models.CharField(max_length=64, blank=True, null=True)
    id_analise = models.CharField(max_length=64, blank=True, null=True)
    Data = models.DateTimeField(null=True, blank=True)
    CNPJ = models.CharField(max_length=255, null=True, blank=True)
    Relatorio = models.TextField(null=True, blank=True)
    RelatorioPDF = models.BinaryField(null=True, blank=True)

    class Meta:
        db_table = 'Relatorios'

    def __str__(self):
        return self.id_consulta
