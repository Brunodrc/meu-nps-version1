from tabnanny import verbose
from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=90)
    email = models.CharField(max_length=80)
    whatsapp = models.IntegerField()

    class Meta:
        verbose_name = 'Cliente'
    
    def __str__(self) -> str:
        return self.nome



