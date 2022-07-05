from django.shortcuts import render,redirect
from django.http import HttpResponse

import cliente
from .models import Cliente
from .forms import Cadastar_cliente

def listar_cliente(request):
    form = Cadastar_cliente()
    clientes = Cliente.objects.all
    return render(request, 'lista_cliente.html', {'clientes': clientes, 'form':form})

def cadastrar_cliente(request):
    if request.method == 'POST':
        form = Cadastar_cliente(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/cliente')
        else:
            return HttpResponse('dados invalidos')

def detalhar_cliente(request, id):
    cliente = Cliente.objects.get(id=id)
    return render(request, 'detalhe_cliente.html', {'cliente':cliente, 'id_cliente':id})

def excluir_cliente(request,id):
    cliente = Cliente.objects.get(id = id).delete()
    return redirect('/cliente')