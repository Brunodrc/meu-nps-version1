from django.shortcuts import render
from django.http import HttpResponse
from .models import Resposta


def respoder_pesquisa(request, id):
    return HttpResponse('teste')

def lista_respostas(request):
    resposta = Resposta.objects.all
    print(resposta)
    return render(request, 'respostas/lista_respostas.html', {'resposta':resposta, 'usuario_logado': request.session.get('usuario')} )

def confirmar_cliente(request):
    return HttpResponse('teste')