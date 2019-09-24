from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from ark_vilao.models import Vilao
from ark_vilao.serializers import VilaoSerializer


class VilaoViewSet(viewsets.ModelViewSet):
    queryset = Vilao.objects.all()
    serializer_class= VilaoSerializer
