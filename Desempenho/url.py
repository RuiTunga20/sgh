from django.urls import path

from . import views

urlpatterns = [
    path('tarefa/adicionar/', views.tarefa_adicionar, name='tarefa_adicionar'),
    path('tarefa/editar/<int:pk>/', views.tarefa_editar, name='tarefa_editar'),
    path('tarefa/concl/<int:pk>/', views.tarefa_concluida, name='concluida'),
    path('tarefa/aprovado/<int:pk>/', views.tarefa_aprovada, name='aprovado'),

    path('tarefa/listar/', views.tarefa_listar, name='tarefa_listar'),
    path('tarefa/eliminar/<int:pk>/', views.tarefa_eliminar, name='tarefa_eliminar'),
    path('tarefa/Delegar/<int:pk>/', views.DelegarTarefa, name='delegar_tarefa'),
    path('Desempenho/', views.Desempenho, name='Desempenho'),

    path('performance/adicionar/', views.performance_adicionar, name='performance_adicionar'),
    path('performance/editar/<int:pk>/', views.performance_editar, name='performance_editar'),
    path('performance/eliminar/<int:pk>/', views.performance_eliminar, name='performance_eliminar'),
    path('performance/', views.performance_listar, name='performance_listar'),

    path('perfomacemes/adicionar/', views.perfomacemes_adicionar, name='perfomacemes_adicionar'),
    path('perfomacemes/editar/<int:pk>/', views.perfomacemes_editar, name='perfomacemes_editar'),
    path('perfomacemes/eliminar/<int:pk>/', views.perfomacemes_eliminar, name='perfomacemes_eliminar'),
    path('perfomacemes/', views.perfomacemes_listar, name='perfomacemes_listar'),
    path('Graficos',views.DesempenhoAnual,name="Graficos"),

]
