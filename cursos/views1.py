from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Curso, Avaliacao
from .serializers import CursoSerializer, AvaliacaoSerializer


class CursoAPIView(APIView):
    """
    API de cursos teste
    """
    def get(self, request):  # http GET
        # print(request)
        cursos = Curso.objects.all()
        serializer = CursoSerializer(cursos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CursoSerializer(data=request.data)  # recebe dados do body da request
        serializer.is_valid(raise_exception=True)  # verifica se a requisição para a API é valida
        serializer.save()  # salva os dados obtidos no banco de dados

        # ao criar retorna o objeto criado no BD
        return Response(serializer.data, status=status.HTTP_201_CREATED)

        # retorna a mensagem
        # return Response({"msg": "Objeto criado com sucesso"}, status=status.HTTP_201_CREATED)

        # retorna apenas o id e o nome do curso
        # return Response({"id": serializer.data['id'],
        # "curso": serializer.data['titulo']}, status=status.HTTP_201_CREATED)


class AvaliacaoAPIView(APIView):
    """
    API de avaliações teste
    """
    def get(self, request):
        # print(dir(request))
        # print(request.user)
        # print(request.user.id)
        avaliacoes = Avaliacao.objects.all()
        serializer = AvaliacaoSerializer(avaliacoes, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AvaliacaoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
