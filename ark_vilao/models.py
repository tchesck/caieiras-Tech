from django.db import models
from universos.models import Universo
from habilidades.models import Habilidade
# Create your models here.

class Vilao(models.Model):
    nome = models.CharField(
        max_length=255
    )
    hab_vilao = models.ManyToManyField(
        Habilidade,
        related_name='hab_vilao'
    )
    uni_vilao = models.ManyToManyField(
        Universo,
        related_name='univer_vilao'
    )

    def __str__(self):
        return self.nome