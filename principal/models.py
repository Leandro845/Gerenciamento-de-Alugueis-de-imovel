from django.db import models
from categoria.models import Categoria
from django.utils import timezone
from django.contrib.auth.models import User


class Anuncio(models.Model):
    usuario_anuncio = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    categoria_anuncio = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    valor = models.CharField(max_length=10)
    estado = models.CharField(max_length=2)
    cidade = models.CharField(max_length=20)
    rua = models.CharField(max_length=50)
    numero = models.CharField(max_length=4)
    quantidade_banheiro = models.CharField(max_length=3)
    quantidade_quartos = models.CharField(max_length=3)
    area_terreno = models.CharField(max_length=8)
    andares = models.CharField(max_length=3)
    garagens = models.CharField(max_length=3)
    img = models.ImageField(upload_to='img/%Y/%m/%h')

    # Dados pessoais

    telefone_anunciante = models.CharField(max_length=30)
    email_anunciante = models.EmailField(max_length=60)