from rest_framework import serializers

from universos.models import Universo
from universos.serializers import UniversoSerializer


class VilaoSerializer(serializers.ModelSerializer):
    universo = serializers.SlugRelatedField(UniversoSerializer, queryset=Universo.objects.all())
    class Meta:
        model = Universo
        fields = ('id', 'nome')
