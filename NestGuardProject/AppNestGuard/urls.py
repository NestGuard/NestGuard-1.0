from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.homepage, name="homepage"),    
    path('orcamento', views.orcamento, name="orcamento"),
    path('registro-orcamento/', registro_orcamento, name='registro_orcamento'),
    path('sobre_nos', views.aboutUs, name="aboutUs"),
    path('politica-de-privacidade', views.politica_de_privacidade, name="politica_de_privacidade"),
    path('termos-e-condicoes', views.termos_e_condicoes, name="termos_e_condicoes"),
    path('seguranca', views.security, name="security"),
    path('solucoes', views.solutions, name="solutions"),
]