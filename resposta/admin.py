from django.contrib import admin
from .models import Resposta
from cliente.models import Cliente

admin.site.register(Resposta)
admin.site.register(Cliente)
