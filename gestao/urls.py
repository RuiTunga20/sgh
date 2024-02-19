from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from gestao import views
urlpatterns = [
    path('Colaborador',views.Colaborador,name='Colaborador'),
    path('Colaborador/<id>', views.Edite_Colaborador, name='Editar_Colaborador'),
    path('EliColaborador/<id>', views.Eliminar_colaborador, name='Eliminar_Colaborador'),
    path('Lista', views.Lista_Colaborador, name='Listar_Colaborador'),

    path('Adicionar_carreira/', views.Adicionar_Carreira, name='Adicionar_carreira'),
    path('editar_carreira/<int:id>/', views.Editar_Carreira, name='editar_carreira'),
    path('eliminar_carreira/<int:id>/', views.Eliminar_Carreira, name='eliminar_carreira'),
    path('listar_carreira/', views.Listar_Carreira, name='listar_carreira'),

    path('adicionar_nivelcarreira/', views.Adicionar_NivelCarreira, name='adicionar_nivelcarreira'),
    path('editar_nivelcarreira/<int:id>/', views.Editar_NivelCarreira, name='editar_nivelcarreira'),
    path('eliminar_nivelcarreira/<int:id>/', views.Eliminar_NivelCarreira, name='eliminar_nivelcarreira'),
    path('listar_nivelcarreira/', views.Listar_NivelCarreira, name='listar_nivelcarreira'),

    path('adicionar_departamento/', views.Adicionar_Departamento, name='adicionar_departamento'),
    path('editar_departamento/<int:id>/', views.Editar_Departamento, name='editar_departamento'),
    path('eliminar_departamento/<int:id>/', views.Eliminar_Departamento, name='eliminar_departamento'),
    path('listar_departamento/', views.Listar_Departamento, name='listar_departamento'),

    path('adicionar_funcao/', views.Adicionar_Funcao, name='adicionar_funcao'),
    path('editar_funcao/<int:id>/', views.Editar_Funcao, name='editar_funcao'),
    path('eliminar_funcao/<int:id>/', views.Eliminar_Funcao, name='eliminar_funcao'),
    path('listar_funcao/', views.Listar_Funcao, name='listar_funcao'),

    path('justificativo/adicionar/', views.justificativa_adicionar, name='justificativo_adicionar'),
    path('justificativo/editar/<int:pk>/', views.justificativa_editar, name='justificativo_editar'),
    path('justificativo/listar/', views.justificativa_listar, name='justificativo_listar'),
    path('justificativo/eliminar/<int:pk>/', views.justificativa_eliminar, name='justificativo_eliminar'),
    path('cursos/adicionar/', views.curso_adicionar, name='curso_adicionar'),
    path('cursos/editar/<int:pk>/', views.curso_editar, name='curso_editar'),
    path('cursos/eliminar/<int:pk>/', views.curso_eliminar, name='curso_eliminar'),
    path('cursos/', views.curso_listar, name='curso_listar'),





]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)