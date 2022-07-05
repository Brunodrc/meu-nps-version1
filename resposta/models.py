from django.db import models
from datetime import date
from pesquisa.models import Item_pesquisa
from cliente.models import Cliente

class Resposta(models.Model):
    escolha_escala = [
        ("Muito satisfeito", "Muito satisfeito"),
        ("Satisfeito", "Satisfeito"),
        ("Neutro", "Neutro"),
        ("Insatisfeito", "Insatisfeito"),
        ("Muito insatisfeito", "Muito insatisfeito"),
    ]
    item_pesquisa = models.ForeignKey(Item_pesquisa, on_delete=models.DO_NOTHING)
    resposta_cli = models.CharField(max_length=20, choices= escolha_escala,default='Neutro')
    data_resposta = models.DateTimeField(auto_now_add=True)
    nome_cliente = models.ForeignKey(Cliente, on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return f"{self.item_pesquisa} | {self.nome_cliente}"
