from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.
estado=(
        ("Pendente", "Pendente"),
        ("Em Andamento", "Em Andamento"),
        ("Concluída", "Concluída"),
    )
MESES = (
    ('janeiro', 'Janeiro'),
    ('fevereiro', 'Fevereiro'),
    ('marco', 'Março'),
    ('abril', 'Abril'),
    ('maio', 'Maio'),
    ('junho', 'Junho'),
    ('julho', 'Julho'),
    ('agosto', 'Agosto'),
    ('setembro', 'Setembro'),
    ('outubro', 'Outubro'),
    ('novembro', 'Novembro'),
    ('dezembro', 'Dezembro'),
)
class Tarefa(models.Model):
    titulo = models.CharField(max_length=255)
    descricao = models.TextField()
    data_inicio = models.DateField()
    data_fim = models.DateField()
    prioridade = models.IntegerField()
    estado=models.CharField(max_length=100,choices=estado,default='Pendente')
    data_estado = models.DateField(null=True,blank=True)

    Aprovado=models.CharField(max_length=100,choices=(
        ("Sim", "Sim"),
        ("Não", "Não"),

    ),default='Não')
    data_atualizado = models.DateField(auto_now=True)

    hierarquia_responsabilidade = models.ManyToManyField(
        to='auth.User',
        related_name='tarefas',
    )

    def __str__(self):
        return self.titulo

class NivelPerforme(models.Model):
    nome= models.CharField(max_length=255)
    Descricao=models.TextField()
    def __str__(self):
        return self.nome
class PerformanceModel(models.Model):
    NivePr=models.ManyToManyField(NivelPerforme)
    nome_meta = models.CharField(max_length=255)
    formula_meta = models.CharField(max_length=255)
    unidade_meta = models.CharField(max_length=10,choices=[('hr', 'hr'), ('%', '%')])
    def __str__(self):
        return self.nome_meta




class Resultados_das_Metas(models.Model):
    Metas=models.ForeignKey(PerformanceModel,on_delete=models.CASCADE)
    Baseline = models.DecimalField(max_digits=10, decimal_places=2)
    Plan = models.DecimalField(max_digits=10, decimal_places=2,default=0)
    status_indicador = models.CharField(max_length=10, choices=[('verde', 'Verde'), ('amarelo', 'Amarelo'), ('vermelho', 'Vermelho')],blank=True,null=True)
    data_medicao = models.DateField(auto_now=True)
    data_mes = models.DateField()

    # Campo para armazenar a fórmula de cálculo da linha de base (opcional)
    def __str__(self):
        return self.Metas.nome_meta
