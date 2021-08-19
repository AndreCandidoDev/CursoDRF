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

    # nested relationship ---> recomendavel utilizar em one to one
    # um curso possui muitas avaliações e so devem ser lidas
    # avaliacoes = AvaliacaoSerializer(many=True, read_only=True)

    # HyperLink Related Field ---> manda link da api com acesso aos detalhes de cada avaliação
    # forma recomendada para APIs REST
    # avaliacoes = serializers.HyperlinkedRelatedField(
    #     many=True,
    #     read_only=True,
    #     view_name='avaliacao-detail'
    # )

    # Primary key related field
    # retorna ids na lista de avaliações do curso ---> forma mais performatica
    avaliacoes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Curso
        fields = (
            'id',
            'titulo',
            'url',
            'criacao',
            'ativo',
            'avaliacoes',
        )
