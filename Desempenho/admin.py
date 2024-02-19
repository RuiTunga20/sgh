from django.contrib import admin
from Desempenho.models import Tarefa,PerformanceModel,Resultados_das_Metas,NivelPerforme
# Register your models here.
class TarefaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data_inicio', 'data_fim', 'prioridade', 'estado', 'Aprovado', 'data_atualizado', 'mostrar_responsaveis')
    list_filter = ('estado', 'Aprovado', 'data_inicio', 'data_fim')
    search_fields = ('titulo', 'descricao')
    date_hierarchy = 'data_inicio'
    ordering = ('-data_inicio',)

    def mostrar_responsaveis(self, obj):
        return ', '.join([responsavel.username for responsavel in obj.hierarquia_responsabilidade.all()])
    mostrar_responsaveis.short_description = 'Responsáveis'
class PerffaAdmin(admin.ModelAdmin):
    list_display = ('nome_meta', 'formula_meta')
    list_filter = ('nome_meta',)
    search_fields = ('nome_meta',)

class PerfMesAdmin(admin.ModelAdmin):
    list_display = ( 'Plan', 'data_medicao')


admin.site.register(PerformanceModel,PerffaAdmin)

admin.site.register(Resultados_das_Metas,PerfMesAdmin)
admin.site.register(NivelPerforme)


admin.site.register(Tarefa, TarefaAdmin)