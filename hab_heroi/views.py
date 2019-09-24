from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from hab_heroi.models import Heroi
from hab_heroi.serializers import HeroiSerializer


class HeroiViewSet(viewsets.ModelViewSet):
    filter_backends = [SearchFilter]
    search_fields = ['^nome', '^hab_vilao', '^uni_vilao']
    queryset = Heroi.objects.all()
    serializer_class= HeroiSerializer
