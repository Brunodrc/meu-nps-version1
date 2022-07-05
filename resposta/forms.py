from django import forms
from .models import Resposta

class Resposta_cliente(forms.ModelForm):
    class Meta:
        Model = Resposta
        fields ="resposta_cli"
