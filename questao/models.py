from django.db import models
from datetime import date

# ORM do django - as classes funcionam como tabelas do banco de dados
class Tipo_atendimento(models.Model):
    nome_atendimento = models.CharField(max_length=80)
    descricao = models.TextField()

    def __str__(self) -> str:
        return self.nome_atendimento

class Questao(models.Model):
    escolha_escala = [
        ("Muito satisfeito", "Muito satisfeito"),
        ("Satisfeito", "Satisfeito"),
        ("Neutro", "Neutro"),
        ("Insatisfeito", "Insatisfeito"),
        ("Muito insatisfeito", "Muito insatisfeito"),
    ]
    pergunta = models.CharField(max_length=200)
    o_atendimento_foi = models.CharField(max_length=20, choices= escolha_escala,default='Neutro') 
    cadastrado_em = models.DateField(auto_now_add=True)
    tipo_atendimento = models.ForeignKey(Tipo_atendimento, on_delete = models.DO_NOTHING, null=True)

    class Meta:
        verbose_name = "Questão"
        verbose_name_plural = "Questões"
    
    def __str__(self):
        return self.pergunta
