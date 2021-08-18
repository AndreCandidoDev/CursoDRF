from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Curso, Avaliacao
from .serializers import CursoSerealizer, AvaliacaoSerializer


class CursoAPIView(APIView):
    """
    API de cursos teste
    """
    def get(self, request):  # http GET
        # print(request)
        cursos = Curso.objects.all()
        serializer = CursoSerealizer(cursos, many=True)
        return Response(serializer.data)


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