from django.contrib import admin
from .models import Curso, Avaliacao


class CursoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'url', 'criacao', 'atualizacao', 'ativo')


class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = ('curso', 'nome', 'email', 'avaliacao', 'criacao', 'atualizacao', 'ativo')


admin.site.register(Curso, CursoAdmin)
admin.site.register(Avaliacao, AvaliacaoAdmin)