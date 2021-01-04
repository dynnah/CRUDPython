from django import forms
from .models import Client


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['nome', 'telefone', 'endereco', 'numero', 'cidade', 'estado', 'pais', 'cep']
