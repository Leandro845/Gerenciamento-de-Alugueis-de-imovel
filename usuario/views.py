from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.messages import constants
from django.contrib import messages
from django.contrib import auth


def cadastro(request):
    if request.method == 'GET':
        return render(request, 'cadastro.html')
    elif request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')

        if senha != confirmar_senha:
            messages.add_message(request, constants.ERROR, 'As senhas não conferem')
            return redirect('cadastro')

        if not 8 <= len(senha) <= 16:
            messages.add_message(
                request, constants.ERROR, 'A senha tem que conter no minímo 8 caracteres e no maximo 16')
            return redirect('cadastro')

        if User.objects.filter(username=nome).exists():
            messages.add_message(request, constants.ERROR, 'Nome de usuário ja existente')
            return redirect('cadastro')

        if User.objects.filter(email=email).exists():
            messages.add_message(request, constants.ERROR, 'Email ja existente')
            return redirect('cadastro')

        usuario = User.objects.create_user(
            username=nome,
            email=email,
            password=senha
        )
        usuario.save()
        return redirect('login')

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        nome = request.POST.get('nome')
        senha = request.POST.get('senha')

        autenticar = auth.authenticate(username=nome, password=senha)

        if not autenticar:
            messages.add_message(request, constants.ERROR, 'Usuario ou senha inválido')
            return redirect('login')

        auth.login(request, autenticar)
        return redirect('anuncios')

