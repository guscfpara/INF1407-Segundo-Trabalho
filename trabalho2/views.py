from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse

def homeSec(request):
    return render(request, "registro/homeSec.html")

'''
permite criar um usuario
GET -> cria o formulario para criar usuario
POST -> pega os dados do formulario e cria um usuario
'''
def registro(request):
    if request.method == 'POST':
        #cria usuario
        formulario = UserCreationForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('sec-home')
        else:
            context = {'form': formulario,}
            return render(request,"registro/registro.html", context)
    else:
        #mostra o formulario
        formulario = UserCreationForm()
        context = {'form': formulario,}
        return render(request,"registro/registro.html", context)

@login_required
def paginaSecreta(request):
    return render(request, "registro/paginaSecreta.html")

'''
Recebe um pedido de verificacao com um username
Procurar no banco de dados o verificaUsername

'''

def verificaUsername(request):
    #GET --> dicionario com todos os campos do formulario
    username = request.GET.get('username', None)
    existe = User.objects.filter(username__iexact=username).exists()
    resposta = {
        "existe": existe,
        "mensagem": "Esse usuario já existe" if existe else "Esse usuario nao existe",
        "cor": "#FF0000" if existe else "#FFFFFF"
    }
    return JsonResponse(resposta)
