from django.contrib import admin
from .models import Anuncio


class AnuncioAdmin(admin.ModelAdmin):
    list_display = ('id', 'rua', 'numero')
    list_display_links = ('id',)


admin.site.register(Anuncio, AnuncioAdmin)


