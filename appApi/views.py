from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.utils.datastructures import MultiValueDictKeyError
from django.views.generic import View
import requests

# Create your views here.

@login_required
def ApiResquest(request):
    return render(request,'api.html')

def cadastrar_usuario(request):
    if request.method == "POST":
        form_usuario = UserCreationForm(request.POST)
        if form_usuario.is_valid():
            form_usuario.save()
            return redirect('procura_nome')
    else:
        form_usuario = UserCreationForm
    return render(request, 'registrar.html',{'form_usuario':form_usuario})

@login_required
def procura_nome(request):
    try:
        nome = request.GET["nome"]
        j_son_nome = requests.get('https://api.agify.io?name='+nome).json()
    except MultiValueDictKeyError:
        j_son_nome=''
    return render(request,'procura_nome.html',{'json_nome':j_son_nome})
