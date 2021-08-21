from rest_framework import generics
from rest_framework.generics import get_object_or_404

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework import permissions

from .models import Curso, Avaliacao
from .serializers import CursoSerializer, AvaliacaoSerializer
from .permissions import EhSUperUser

"""
    API versão 1
"""


# ListCreateAPIView ---> GET e POST ---->listar coleção e criar objeto
class CursosAPIView(generics.ListCreateAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer


# RetrieveUpdateDestroyAPIView -----> necessario ID ----> update e delete
class CursoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer


class AvaliacoesAPIView(generics.ListCreateAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer

    # metodo retorna uma lista de objetos
    def get_queryset(self):

        # cursos/curso_pk/avaliacoes
        # verifica se na url há curso_pk
        if self.kwargs.get('curso_pk'):

            # se houver atribui id a pk e procura no bd
            return self.queryset.filter(curso_id=self.kwargs.get('curso_pk'))

        return self.queryset.all()  # se não houver retorna todas avaliações


class AvaliacaoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer

    # retorna objeto com determinada pk
    def get_object(self):
        if self.kwargs.get('curso_pk'):
            return get_object_or_404(self.get_queryset(), curso_id=self.kwargs.get('curso_pk'),
                                     pk=self.kwargs.get('avaliacao_pk'))
        return get_object_or_404(self.get_queryset(), pk=self.kwargs.get('avaliacao_pk'))


"""
    API versão 2
"""


class CursoViewSet(viewsets.ModelViewSet):

    permission_classes = (
        EhSUperUser,
        permissions.DjangoModelPermissions,
    )  # o acesso aos GET é padão

    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

    # paginação padrão não influencia nos métodos sobrescritos
    @action(detail=True, methods=['get'])  # cria router com avaliacoes na router cursos
    def avaliacoes(self, request, pk=None):
        self.pagination_class.page_size = 2  # define o tamanho de cada página
        avaliacoes = Avaliacao.objects.filter(curso_id=pk)
        page = self.paginate_queryset(avaliacoes)

        if page is not None:
            serializer = AvaliacaoSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        # curso = self.get_object()  # chave estrangeira da model Avaliacoes
        # serializer = AvaliacaoSerializer(curso.avaliacoes.all(), many=True)
        serializer = AvaliacaoSerializer(avaliacoes, many=True)
        return Response(serializer.data)


# class AvaliacaoViewSet(viewsets.ModelViewSet):
#     queryset = Avaliacao.objects.all()
#     serializer_class = AvaliacaoSerializer


# usar da seguinte forma para desativar algum metodo da viewset
class AvaliacaoViewSet(
    mixins.ListModelMixin,   # list all ---- GET
    mixins.CreateModelMixin,   # create --- POST
    mixins.RetrieveModelMixin,  # retrieve one --- GET
    mixins.UpdateModelMixin,    # update ----- PUT
    mixins.DestroyModelMixin,   # delete ---- DELETE
    viewsets.GenericViewSet
):

    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer
