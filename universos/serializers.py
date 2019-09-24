from rest_framework import serializers


class UniversoSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    nome = serializers.CharField(read_only=True)
