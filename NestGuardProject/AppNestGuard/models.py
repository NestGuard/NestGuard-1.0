from django.db import models


    
class NestGuardCard(models.Model):
    titulo = models.TextField(blank=True, null=True)
    descricao = models.TextField(blank=True, null=True)
    link_img = models.URLField(blank=True, null=True)
    descricaoModal = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.titulo
    


class Orcamento(models.Model):
    nome_cliente = models.CharField(max_length=100, verbose_name="Nome do Cliente")
    telefone_cliente = models.CharField(max_length=15, verbose_name="Telefone do Cliente")
    email_cliente = models.EmailField(verbose_name="Email do Cliente")
    descricao_servico = models.TextField(verbose_name="Descrição do Serviço")
    data_entrega = models.DateField(verbose_name="Data de Entrega")
    tipo_servico = models.CharField(
        max_length=50,
        choices=[
            ('criar_site', 'Criação de site'),
            ('criar_design', 'Criação de design'),
            ('criar_bot', 'Criação de bot'),
            ('hospedagem', 'Hospedagem'),
            ('automacao', 'Automação'),

            ('outros', 'Outros')
        ],
        verbose_name="Tipo de Serviço"
    )
    data_criacao = models.DateTimeField(auto_now_add=True, verbose_name="Data de Criação")

    def __str__(self):
        return f"{self.nome_cliente} - {self.tipo_servico}"
    
class EmailCliente(models.Model):
    email_cliente = models.EmailField(verbose_name="Email do Cliente")

    def __str__(self):
        return self.email_cliente

class AboutUs(models.Model):
    titulo1 = models.TextField(blank=True, null=True)
    titulo2 = models.TextField(blank=True, null=True)
    paragrafo1 = models.TextField(blank=True, null=True)
    paragrafo2 = models.TextField(blank=True, null=True)
    paragrafo3 = models.TextField(blank=True, null=True)
    paragrafo4 = models.TextField(blank=True, null=True)

class Homepage(models.Model):
    tituloCarrosel = models.TextField(blank=True, null=True, max_length=40)
    subtituloCarrosel1 = models.TextField(blank=True, null=True)
    subtituloCarrosel2 = models.TextField(blank=True, null=True)
    subtituloCarrosel3 = models.TextField(blank=True, null=True)
    carrosselImg1 = models.ImageField(upload_to='imagesCarrosel/')
    carrosselImg2 = models.ImageField(upload_to='imagesCarrosel/')
    carrosselImg3 = models.ImageField(upload_to='imagesCarrosel/')
    tituloSection1 = models.TextField(blank=True, null=True)
    subtituloSection1 = models.TextField(blank=True, null=True)
    tituloCard1 = models.TextField(blank=True, null=True)
    descricaoCard1 = models.TextField(blank=True, null=True)
    tituloCard2 = models.TextField(blank=True, null=True)
    descricaoCard2 = models.TextField(blank=True, null=True)
    tituloCard3 = models.TextField(blank=True, null=True)
    descricaoCard3 = models.TextField(blank=True, null=True)
    tituloSection2 = models.TextField(blank=True, null=True)
    textoSection2 = models.TextField(blank=True, null=True)
    imgSection2 = models.ImageField(upload_to='imagesSection2/')
    tituloSection3 = models.TextField(blank=True, null=True)
    textoSection3 = models.TextField(blank=True, null=True)
    tituloSection4 = models.TextField(blank=True, null=True)
    textoSection4 = models.TextField(blank=True, null=True)
    imgSection4 = models.ImageField(upload_to='imagesSection4/')
    textoSection5 = models.TextField(blank=True, null=True)
    tituloSection5 = models.TextField(blank=True, null=True)
    imgSection5 = models.ImageField(upload_to='imagesSection5/')

