from rest_framework import serializers
from .models import Noticia

class NoticiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Noticia
        fields = '__all__'

class MemoriaNoticiaSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)  # Apenas leitura
    titulo = serializers.CharField(max_length=255)
    conteudo = serializers.CharField()
    autor = serializers.CharField(max_length=255)
    publicado = serializers.BooleanField(default=False)
    data_criacao = serializers.DateTimeField(read_only=True)