from rest_framework import serializers


class HabilidadeDataSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    nome = serializers.CharField(read_only=True)
    nv_habilidade = serializers.CharField(read_only=True)