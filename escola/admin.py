from django.contrib import admin
from escola.models import Aluno,Curso

class Alunos(admin.ModelAdmin):
    list_display = ('id','nome','rg','cpf','data_nascimento')
    list_display_links = ('id','nome')
    search_fields = ('nome',)
    list_per_page = 20

admin.site.register(Aluno,Alunos)

class Cursos(admin.ModelAdmin):
    list_display = ('id','curso','descricao')
    list_display_links = ('id','curso')
    search_fields = ('curso',)
    
admin.site.register(Curso,Cursos)

# Register your models here.
