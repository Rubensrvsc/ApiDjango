from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('api/',ApiResquest,name='api'),
    path('cadastrar_usuario/', cadastrar_usuario, name="cadastrar_usuario"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('procura_nome/',procura_nome,name="procura_nome"),
]