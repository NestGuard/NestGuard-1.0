from django import forms
from .models import Orcamento, EmailCliente

class OrcamentoForm(forms.ModelForm):
    class Meta:
        model = Orcamento
        fields = [
            'nome_cliente',
            'telefone_cliente',
            'email_cliente',
            'descricao_servico',
            'data_entrega',
            'tipo_servico',
        ]
        widgets = {
            'data_entrega': forms.DateInput(attrs={'type': 'date'}),
        }
        labels = {
            'nome_cliente': 'Nome',
            'telefone_cliente': 'Número do celular',
            'email_cliente': 'Email',
            'descricao_servico': 'Descreva o serviço',
            'data_entrega': 'Selecione a data de entrega desejada',
            'tipo_servico': 'Selecione o tipo de serviços',
        }

class EmailClienteForm(forms.ModelForm):
    class Meta:
        model = EmailCliente
        fields = [
            'email_cliente',
        ]
        labels = {
            'email_cliente': 'Seu endereco de email',
        }