from django.urls import path
from . import views


urlpatterns = [   
    path('adicionar_anuncio/', views.adicionar_anuncio, name='adicionar_anuncio'),
    path('anuncios/', views.anuncios, name='anuncios'),
    path('detalhes_anuncio/<int:id>', views.detalhes_anuncio, name='detalhes_anuncio'),
    path('meus_anuncios/', views.meus_anuncios, name='meus_anuncios'),
    path('excluir/<int:id>', views.excluir, name='excluir'),
    path('deslogar/', views.deslogar, name='deslogar')
]
