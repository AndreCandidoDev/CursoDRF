from django.db import models


# classe abstrata
class Base(models.Model):
    criacao = models.DateTimeField(auto_now_add=True)
    atualizacao = models.DateTimeField(auto_now_add=True)
    ativo = models.BooleanField(default=True)

    class Meta:
        abstract = True


# herda a classe abstrata Base
class Curso(Base):
    titulo = models.CharField(max_length=255)
    url = models.URLField(unique=True)

    class Meta:
        verbose_name = 'curso'
        verbose_name_plural = 'cursos'

    def __str__(self):
        return self.titulo


# herda a classe abstrata Base
class Avaliacao(Base):
    curso = models.ForeignKey(Curso, related_name='avaliacoes', on_delete=models.CASCADE)
    nome = models.CharField(max_length=255)
    email = models.EmailField()
    comentario = models.TextField(blank=True, default="")
    avaliacao = models.DecimalField(max_digits=2, decimal_places=1)

    class Meta:
        verbose_name = 'avaliação'
        verbose_name_plural = 'avaliações'
        unique_together = ['email', 'curso']  # uma pessoa com email so pode avaliar uma vez

    def __str__(self):
        return f'{self.nome} avaliou o curso {self.curso} com nota {self.avaliacao}'
