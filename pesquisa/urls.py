from struct import pack
from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name='home'),
    #lista de pesquisas
    path('', views.listar_pesquisa, name='listar_pesquisa'),
    path('detalhe_pesquisa/<int:id>', views.detalhe_pesquisa, name= 'detalhe_pesquisa'),
    path('cria_pesquisa', views.cria_pesquisa, name= 'cria_pesquisa'),
    path('cadastra_titulo_pesquisa', views.cadastra_titulo_pesquisa, name= 'cadastra_titulo_pesquisa'),
    #path('cadastra_tipo_atendimento', views.cadastra_tipo_atendimento, name= 'cadastra_tipo_atendimento'),
]