from struct import pack
from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_cliente, name='listar_cliente'),
    path('cadastrar_cliente', views.cadastrar_cliente, name='cadastrar_cliente'),
    path('detalhar_cliente/<int:id>', views.detalhar_cliente, name='detalhar_cliente'),
    path('excluir_cliente/<int:id>', views.excluir_cliente, name='excluir_cliente'),
]