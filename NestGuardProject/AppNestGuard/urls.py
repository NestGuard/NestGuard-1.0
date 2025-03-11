from django.urls import path, re_path
from . import views
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, re_path
from . import views
from .views import *
from django.contrib.sitemaps.views import sitemap
from .sitemaps import SimpleSitemap


sitemaps = {
    'static': SimpleSitemap(),  # Use o SimpleSitemap aqui
}

urlpatterns = [
    path('', views.homepage, name="homepage"),    
    path('orcamento', views.orcamento, name="orcamento"),
    path('registro-orcamento/', registro_orcamento, name='registro_orcamento'),
    path('sobre_nos', views.aboutUs, name="aboutUs"),
    path('politica-de-privacidade', views.politica_de_privacidade, name="politica_de_privacidade"),
    path('termos-e-condicoes', views.termos_e_condicoes, name="termos_e_condicoes"),
    path('seguranca', views.security, name="security"),
    path('solucoes', views.solutions, name="solutions"),
    path('url-invalida', views.url_invalida, name="url_invalida"),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap'),
    # Captura todas as URLs inválidas, exceto arquivos estáticos e mídias
    re_path(r'^(?!media/|static/).*$', views.url_invalida),
    
]

# Adiciona rotas para servir mídia e arquivos estáticos em DEBUG
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
