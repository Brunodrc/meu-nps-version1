#import para criar rotas
from django.urls import path

#import da views
from . import views

#lista de rotas
urlpatterns = [
    path('cadastrar/', views.cadastrarq)
]