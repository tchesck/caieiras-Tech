from django.db import models


# Create your models here.

class Universo(models.Model):
    nome = models.CharField(max_length=55)

    def __str__(self):
        return self.nome
