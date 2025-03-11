from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return [
            'homepage',
            'orcamento',
            'registro_orcamento',
            'aboutUs',
            'politica_de_privacidade',
            'termos_e_condicoes',
            'security',
            'solutions',
        ]
    def location(self, item):
        try:
            return reverse(item)
        except Exception as e:
            print(f"Erro no reverse({item}): {e}")
            return '/'
