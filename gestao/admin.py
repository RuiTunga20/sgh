
from django.contrib import admin
from gestao.models import *


class Progresso_CarreiraAdmin(admin.ModelAdmin):
    list_display = ("nome", "descricao")


class CarreiraAdmin(admin.ModelAdmin):
    list_display = ("nome", "categoria", "descricao")


class NivelCarreiraAdmin(admin.ModelAdmin):
    list_display = ("nome", "carreira","get_carreira", "bandafuncional", "salario")


class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ("nome", "descricao")


class FuncaoAdmin(admin.ModelAdmin):
    list_display = ("codigo", "nome", "departamento")


class ColaboradoresAdmin(admin.ModelAdmin):
    list_display = (
        "nome_completo",
        "bi",
        "data_nascimento",
        "funcao",
        "nivel_carreira_atual",

    )

admin.site.register(Progresso_Carreira, Progresso_CarreiraAdmin)
admin.site.register(Carreira, CarreiraAdmin)
admin.site.register(NivelCarreira, NivelCarreiraAdmin)
admin.site.register(Departamento, DepartamentoAdmin)
admin.site.register(Funcao, FuncaoAdmin)
admin.site.register(Colaboradores, ColaboradoresAdmin)
admin.site.register(Justificativo)
