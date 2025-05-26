from django.contrib import admin
from django.urls import path

from APICredMind.views.Politicas.PoliticaAnalise import PoliticaAnalise
from APICredMind.views.Politicas.PoliticaOnboarding import PoliticaOnboarding
from APICredMind.views.Lemit.consultaLemit import consultaEmpresaLemit
from APICredMind.views.SERASA.consultaSERASARelato import consultaSERASARelato

from APICredMind.views.SERASA.processaSERASA import processaSERASA

from APICredMind.views.Users.views import UserDetailView
from APICredMind.views.BigDataCorp.consultaBigDataCorp import *

from APICredMind.views.ControleAcesso.vwControleAcesso import CustomTokenObtainPairView
from APICredMind.views.PoliticaConsultas.Consulta_Socios import ConsultaDadosQSA
from APICredMind.views.PoliticaConsultas.Consulta_Processos_Empresa import ConsultaProcessosEmpresa

from APICredMind.views.IBGE.CNAE import obterCNAE
from APICredMind.views.IBGE.CNAE import eriqueceCNAE
from APICredMind.views.NeoCredit.esteiraInativos import esteiraInativosNeoCredit

urlpatterns = [
    path('PoliticaAnalise', PoliticaAnalise.as_view(), name='PoliticaAnalise'),
    path('PoliticaOnboarding', PoliticaOnboarding.as_view(), name='PoliticaOnboarding'),
    path('consultaEmpresaLemit', consultaEmpresaLemit.as_view(), name='consultaEmpresaLemit'),
    path('consultaSERASARelato', consultaSERASARelato.as_view(), name='consultaRelatoSERASA'),
    path('processaSERASA', processaSERASA.as_view(), name='processaSERASA'),
    path('geraToken', CustomTokenObtainPairView.as_view(), name='geraToken'),
    path('user', UserDetailView.as_view(), name='UserDetail'),
    path('consultaDadosEmpresa', consultaDadosEmpresa.as_view(), name='consultaDadosEmpresa'),
    path('consultaDadosPessoa', consultaDadosPessoa.as_view(), name='consultaDadosPessoa'),
    path('consultaDadosQSA', ConsultaDadosQSA.as_view(), name='consultaDadosQSA'),
    path('consultaProcessosEmpresa', ConsultaProcessosEmpresa.as_view(), name='consultaProcessosEmpresa'),
    path('obterCNAE', obterCNAE.as_view(), name='obterCNAE'),
    path('eriqueceCNAE', eriqueceCNAE.as_view(), name='eriqueceCNAE'),
    path('esteiraInativosNeoCredit', esteiraInativosNeoCredit.as_view(), name='esteiraInativosNeoCredit')
]
