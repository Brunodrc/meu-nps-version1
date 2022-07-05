
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('questao/', include('questao.urls')),
    path('pesquisa/', include('pesquisa.urls')),
    path('resposta/', include('resposta.urls')),
    path('auth/', include('usuario.urls')),
    path('cliente/', include('cliente.urls')),
]
