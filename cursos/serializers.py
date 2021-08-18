# Tranforma model para json

from rest_framework import serializers
from .models import Curso, Avaliacao


class AvaliacaoSerializer(serializers.ModelSerializer):

    class Meta:

        # usar para informações que possam comprometer a segurança
        extra_kwargs = {
            'email': {'write_only': True}  # email nao sera exibido na response, exigido apenas no cadastro
        }

        # model que sera serializado
        model = Avaliacao

        # campos que serão exibidos na response da api
        fields = (
            'id',
            'curso',
            'nome',
            'email',
            'comentario',
            'avaliacao',
            'criacao',
            'ativo',
        )


class CursoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Curso
        fields = (
            'id',
            'titulo',
            'url',
            'criacao',
            'ativo',
        )