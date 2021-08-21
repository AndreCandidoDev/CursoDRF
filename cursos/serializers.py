# Tranforma model para json

from rest_framework import serializers
from django.db.models import Avg

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

    def validate_avaliacao(self, valor):
        if valor in range(1, 6):  # 1, 2, 3, 4, 5
            return valor
        raise serializers.ValidationError('A avaliação precisa ser um inteiro entre 1 e 5')


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

    media_avaliacoes = serializers.SerializerMethodField()

    class Meta:
        model = Curso
        fields = (
            'id',
            'titulo',
            'url',
            'criacao',
            'ativo',
            'avaliacoes',
            'media_avaliacoes'
        )

    def get_media_avaliacoes(self, obj):
        media = obj.avaliacoes.aggregate(Avg('avaliacao')).get('avaliacao__avg')
        if media is None:
            return 0
        return round(media*2) / 2
