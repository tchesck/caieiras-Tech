from django.db import models

# Create your models here.
from django.db import models


# Create your models here.

class Habilidade(models.Model):
    nome = models.CharField(max_length=55)
    nv_hab = models.CharField(max_length=10)

    def __str__(self):
        return self.nome

    def __str__(self):
        return self.nv_hab
