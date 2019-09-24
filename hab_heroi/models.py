from django.db import models

# Create your models here.
from habilidades.models import Habilidade
from universos.models import Universo


class Heroi(models.Model):
    nome = models.CharField(
        max_length=255
    )
    hab_heroi = models.ManyToManyField(
        Habilidade,
        related_name='hab_heroi'
    )
    uni_heroi = models.ManyToManyField(
        Universo,
        related_name='univer_heroi'
    )

    def __str__(self):
        return self.nome