from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Usuario

from django.views.decorators.csrf import csrf_exempt

def login(request):
    status = request.GET.get('status')
    return render(request, 'login.html', {'status':status})

def cadastro(request):
    status = request.GET.get('status')
    return render(request, 'cadastro.html', {'status':status})

def valida_cadastro(request):
    nome = request.POST.get('nome')
    email = request.POST.get('email')
    senha = request.POST.get('senha')
    telefone = request.POST.get('telefone')

    
    usuario = Usuario.objects.filter(emal = email)
    #verifica se nome e e-mail estão em branco
    if len(nome.strip()) == 0 or len(email.strip()) == 0:
        return redirect('/auth/cadastro/?status=1')

    # verifica se o usario esta no banco de dados
    if (len(usuario) > 0):
        return redirect('/auth/cadastro/?status=2')

    try:
        usuario = Usuario(nome = nome, emal = email, senha = senha, telefone = telefone)
        usuario.save()

        return redirect('/auth/cadastro/?status=0')
    except:
        return redirect('/auth/cadastro/?status=3')

def valida_login(request):
    email = request.POST.get('email')
    senha = request.POST.get('senha')

    usuario = Usuario.objects.filter(emal=email).filter(senha=senha)

    if len(usuario)==0:
        return redirect('/auth/?status=1')
    elif len(usuario) > 0:
        request.session['usuario'] = usuario[0].id
        return redirect('/pesquisa/home')

def sair(request):
    request.session.flush()
    return redirect('/auth/')