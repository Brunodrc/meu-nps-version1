from django.urls import path
from . import views

urlpatterns = [
    path('respoder_pesquisa/<int:id>', views.respoder_pesquisa, name= 'respoder_pesquisa'),
    path('confirmar_cliente/', views.confirmar_cliente, name= 'confirmar_cliente'),
    path('', views.lista_respostas, name='lista_respostas')
]