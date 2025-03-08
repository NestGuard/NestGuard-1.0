from .models import *
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import OrcamentoForm
from django.core.mail import send_mail
from django.conf import settings
from .models import EmailCliente
from .forms import EmailClienteForm

def url_invalida(request):
    return render(request, 'url-invalida.html')

# Create your views here.
def homepage(request):
    homepage_data = Homepage.objects.all()
    email_form = EmailClienteForm()

    if request.method == 'POST':
        email_form = EmailClienteForm(request.POST)
        if email_form.is_valid():
            novo_email = email_form.save()

            # Configuração do e-mail
            assunto = "Obrigado por se inscrever!"
            mensagem = f"Olá, obrigado por se inscrever! Em breve, enviaremos novidades para {novo_email.email_cliente}."
            destinatario = [novo_email.email_cliente]

            try:
                send_mail(assunto, mensagem, settings.EMAIL_HOST_USER, destinatario)
                messages.success(request, "E-mail cadastrado com sucesso! Verifique sua caixa de entrada.")
            except Exception as e:
                messages.error(request, f"Erro ao enviar e-mail: {e}")

            return redirect('homepage')

    context = {'homepage': homepage_data, 'email_form': email_form}
    return render(request, 'homepage.html', context)


def termos_e_condicoes(request):
    return render(request, 'termos-e-condicoes.html')

def solutions(request):
    return render (request, 'solutions.html')

def politica_de_privacidade(request):
    return render(request, 'politica-de-privacidade.html')

def security(request):
    return render(request, 'security.html')

def orcamento(request):
    """
    Exibe e processa o formulário de orçamento.
    """
    if request.method == 'POST':
        form = OrcamentoForm(request.POST)
        if form.is_valid():
            # Salva os dados no banco de dados
            orcamento = form.save()

            # Monta o conteúdo do e-mail
            print('email enviado')
            assunto = f"Novo orçamento registrado por {orcamento.nome_cliente}"
            mensagem = (
                f"Detalhes do orçamento:\n\n"
                f"Nome do cliente: {orcamento.nome_cliente}\n"
                f"Telefone: {orcamento.telefone_cliente}\n"
                f"E-mail: {orcamento.email_cliente}\n"
                f"Descrição do serviço: {orcamento.descricao_servico}\n"
                f"Data de entrega: {orcamento.data_entrega}\n"
                f"Tipo de serviço: {orcamento.tipo_servico}\n"
            )
            destinatario = ['ga375464@gmail.com']

            # Envia o e-mail
            try:
                send_mail(assunto, mensagem, settings.EMAIL_HOST_USER, destinatario)
                messages.success(request, 'Orçamento registrado e e-mail enviado com sucesso!')
            except Exception as e:
                messages.error(request, f"Erro ao enviar e-mail: {e}")
                print(f"Erro ao enviar e-mail: {e}")

            return redirect('orcamento')  # Redireciona para a mesma página após o sucesso
        else:
            print('erro no registro')
            messages.error(request, 'Houve um erro no registro. Verifique os dados e tente novamente.')
    else:
        form = OrcamentoForm()

    # Renderiza o formulário na página de orçamento
    return render(request, 'orcamento.html', {'form': form})

def aboutUs(request):
    context = {}
    aboutUs = AboutUs.objects.all()
    context['aboutUs'] = aboutUs
    return render(request, 'aboutUs.html', context)


def registro_orcamento(request):
    """
    View para exibir e processar o formulário de registro de orçamento.
    """
    if request.method == 'POST':
        form = OrcamentoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Orçamento registrado com sucesso!')
            return redirect('pagina_de_sucesso')  # Substitua pela URL da página de sucesso
        else:
            messages.error(request, 'Houve um erro no registro. Verifique os dados e tente novamente.')
    else:
        form = OrcamentoForm()

    # Adicione debug temporário
    print(f"Formulário: {form}")

    return render(request, 'registro_orcamento.html', {'form': form})

