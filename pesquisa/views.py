from unicodedata import name
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Pesquisa, Item_pesquisa
from questao.models import Questao, Tipo_atendimento
from usuario.models import Usuario
from .forms import Cadastar_titulo_pesquisa, Cadastar_item_pesquisa, Cadastar_questao_pesquisa, Cadastar_atendimento_pesquisa

def home(request):
    
    return render(request, 'home.html', {'usuario_logado': request.session.get('usuario')})

def listar_pesquisa(request):
    #if(request.session.get('usuario')):
        #usuario = Usuario.objects.get(id=request.session['usuario'])
        pesquisas = Pesquisa.objects.all
        form1 = Cadastar_titulo_pesquisa()
        #pesquisas = Pesquisa.objects.filter(usuario = usuario)
        return render(request, 'lista_pesquisa.html', {'pesquisas': pesquisas, 'usuario_logado': request.session.get('usuario'), 'form1':form1})
    #else:
    #    return redirect('pagina de login/?status=2')

def detalhe_pesquisa(request, id):
    item_pesquisa = Item_pesquisa.objects.get(id=id)
    pesquisa = Pesquisa.objects.get(id=id)
    #questao = Questao.objects.get(id=id)
    return render(request, 'detalhe_pesquisa.html', {'item_pesquisa':item_pesquisa, 'pesquisa':pesquisa,'usuario_logado': request.session.get('usuario')})

def cria_pesquisa(request):
    
    form2 = Cadastar_item_pesquisa()
    form3 = Cadastar_questao_pesquisa()
    form4 = Cadastar_atendimento_pesquisa()
    return render(request, 'cria_pesquisa.html', {'form2':form2, 'form3':form3, 'form4':form4})

def cadastra_titulo_pesquisa(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        validade = request.POST.get('validade')
        item_pesquisa = nome
        nova_pesquisa = Pesquisa(nome = nome, validade = validade)
        nova_pesquisa.save()
        return redirect('/pesquisa/cria_pesquisa')
    else:
        return HttpResponse('dados invalidos')
""" def detalhe_pesquisa(request, id):
    #if(request.session.get('usuario')):
        item_pesquisa = Item_pesquisa.objects.get(id=id)
        #if request.session.get('usuario') == item_pesquisa.usuario.id:
            #item_pesquisa = Item_pesquisa.objects.get()
            return render(request, 'detalhe_pesquisa.html',{'pesquisa':pesquisa},{'item_pesquisa':item_pesquisa})
    #else:
     #   redirect('pagina de login/?status=2')
 """