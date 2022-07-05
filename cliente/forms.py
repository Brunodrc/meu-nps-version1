from django import forms
from .models import Cliente

class Cadastar_cliente(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = "__all__"