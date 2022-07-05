from dataclasses import fields
from pyexpat import model
from django.urls import clear_script_prefix
from django import forms
from .models import Pesquisa, Item_pesquisa
from questao.models import Questao, Tipo_atendimento

class Cadastar_titulo_pesquisa(forms.ModelForm):
    class Meta:
        model = Pesquisa
        fields = "__all__"
class Cadastar_item_pesquisa(forms.ModelForm):
    class Meta:       
        model = Item_pesquisa
        fields = "__all__"
class Cadastar_questao_pesquisa(forms.ModelForm):
    class Meta:
        model = Questao
        fields = "__all__"
class Cadastar_atendimento_pesquisa(forms.ModelForm):
    class Meta:
        model = Tipo_atendimento
        fields = "__all__"
