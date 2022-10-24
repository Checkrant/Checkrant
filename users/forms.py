from django import forms
from django.forms import fields, models
from .models import  UserRant


class rantForm(forms.ModelForm):
    class Meta:
        model = UserRant
        fields = ['nomeRant', 'endereco', 'horarioInicio', 'horarioFinal', 'tipo', 'email', 'password']
        labels = {
            'nomeRant': 'Nome Restaurante',
            'endereco': 'Endereço',
            'horarioInicio': 'Horário Inicio',
            'horarioFinal': 'Horário Final',
            'tipo': 'Tipo',
            'password': 'Senha',
        }



