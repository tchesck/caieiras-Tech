from rest_framework import serializers


class HeroiSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    nome = serializers.CharField(read_only=True)
    hab_heroi = serializers.CharField(read_only=True)
    univer_heroi = serializers.CharField(read_only=True)