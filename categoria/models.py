from django.db import models


class Categoria(models.Model):
    nome_categoria = models.CharField(max_length=15)

    def __str__(self) -> str:
        return self.nome_categoria
    

