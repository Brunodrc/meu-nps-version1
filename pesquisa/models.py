from tabnanny import verbose
from django.db import models
from datetime import date
from questao.models import Questao
from usuario.models import Usuario

class Pesquisa(models.Model):
    nome = models.CharField(max_length=80)
    data_criada = models.DateField(auto_now_add=True)
    validade = models.DateField(blank=True, null=True)
    #nome_usuario = models.ForeignKey(Usuario, on_delete= models.DO_NOTHING)

    class Meta:
        verbose_name = 'Pesquisa'
    
    def __str__(self) -> str:
        return self.nome

class Item_pesquisa(models.Model):
    nome_pesquisa = models.ForeignKey(Pesquisa, on_delete=models.DO_NOTHING)
    nome_questao = models.ForeignKey(Questao, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = "Item_pesquisa"
        verbose_name_plural = "Itens_pesquisa"
    
    def __str__(self) -> str:
        return f"{self.nome_pesquisa} | {self.nome_questao}"
