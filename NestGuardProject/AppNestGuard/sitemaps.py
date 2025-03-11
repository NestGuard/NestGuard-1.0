from django.contrib.sitemaps import Sitemap
from django.urls import reverse





class SimpleSitemap(Sitemap):
    def items(self):
        return [
            'homepage',  # Página inicial
            'orcamento',  # Página de orçamento
            'aboutUs',  # Sobre nós
            'politica_de_privacidade',  # Política de privacidade
            'termos_e_condicoes',  # Termos e condições
            'security',  # Segurança
            'solutions',  # Soluções
            'url_invalida',  # URL inválida
            
        ]

    def location(self, item):
        return reverse(item)  # Gera a URL completa a partir do nome