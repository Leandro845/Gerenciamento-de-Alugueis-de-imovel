from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Anuncio
from categoria.models import Categoria
from django.contrib import messages
from django.contrib.messages import constants
from django.contrib.auth.models import User
from django.contrib import auth


def anuncios(request):
    anuncios = Anuncio.objects.all()
    return render(request, 'anuncios.html', {'anuncios': anuncios})


def detalhes_anuncio(request, id):
    anuncio = get_object_or_404(Anuncio, id=id)
    return render(request, 'detalhes_anuncio.html', {'anuncio': anuncio})


def excluir(request, id):
    anuncio = get_object_or_404(Anuncio, id=id)
    anuncio.delete()
    return redirect('meus_anuncios')


def deslogar(request):
    auth.logout(request)
    return redirect('pagina_inicial')


def adicionar_anuncio(request):
    categorias = Categoria.objects.all()
    if request.method == 'GET':
        return render(request, 'adicionar_anuncio.html', {'categorias': categorias})
    elif request.method == 'POST':
        categoria = request.POST.get('categoria')
        valor_aluguel = request.POST.get('valor_aluguel')
        estado = request.POST.get('estado')
        cidade = request.POST.get('cidade')
        rua = request.POST.get('rua')
        numero = request.POST.get('numero')
        quantidade_banheiro = request.POST.get('quantidade_banheiro')
        quantidade_quarto = request.POST.get('quantidade_quartos')
        area = request.POST.get('area')
        andares = request.POST.get('andares')
        garagens = request.POST.get('garagens')
        imagem = request.POST.get('iamagem')

        telefone_anunciante = request.POST.get('telefone_anunciante')
        email_anunciante = request.POST.get('email_anunciante')


        if not categoria \
        and not valor_aluguel \
        and not estado \
        and not cidade \
        and not rua \
        and not numero \
        and not quantidade_banheiro \
        and not quantidade_quarto \
        and not area \
        and not andares \
        and not garagens \
        and not imagem: 
            messages.add_message(request, constants.ERROR, 'Todos os campos tem que serem preenchidos')
            return redirect('adicionar_anuncio')


        categoria_do_anuncio = Categoria.objects.filter(nome_categoria=categoria)[0]

        

        anuncio = Anuncio(
            usuario_anuncio=request.user,
            categoria_anuncio=categoria_do_anuncio,
            valor=valor_aluguel,
            estado=estado,
            cidade=cidade,
            rua=rua,
            numero=numero,
            quantidade_banheiro=quantidade_banheiro,
            quantidade_quartos=quantidade_quarto,
            area_terreno=area,
            andares=andares,
            garagens=garagens,
            img=imagem,
            telefone_anunciante=telefone_anunciante,
            email_anunciante=email_anunciante,
        )
        anuncio.save()
        return redirect('anuncios')
    

def meus_anuncios(request):
    anuncios = Anuncio.objects.filter(usuario_anuncio=request.user)
    return render(request, 'meus_anuncios.html', {'anuncios': anuncios})
