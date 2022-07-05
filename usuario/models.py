from tabnanny import verbose
from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    emal = models.CharField(max_length=90)
    senha = models.CharField(max_length=30)
    telefone = models.CharField(max_length=30)

    class Meta:
        verbose_name = 'Usuário'

    def __str__(self) -> str:
        return self.nome
