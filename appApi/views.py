from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import requests

# Create your views here.

@login_required
def ApiResquest(request):
    j_son = requests.get('https://api.agify.io?name=michael').json()
    print(j_son)
    return render(request,'api.html',{'nomes':j_son})

def cadastrar_usuario(request):
    if request.method == "POST":
        form_usuario = UserCreationForm(request.POST)
        if form_usuario.is_valid():
            form_usuario.save()
            return redirect('api')
    else:
        form_usuario = UserCreationForm
    return render(request, 'registrar.html',{'form_usuario':form_usuario})

@login_required
def procura_nome(request):
    nome = request.GET["nome"]
    print(nome)
    j_son_nome = requests.get('https://api.agify.io?name='+nome).json()
    return render(request,'procura_nome.html',{'json_nome':j_son_nome})
