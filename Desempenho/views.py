import datetime
from datetime import date
from django.db.models import Count
from django.db.models.functions import ExtractMonth
import calendar
# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .formulario import *

def tarefas_por_estado(modelo, data_atual):
    tarefas_pendentes = modelo.objects.filter(
        data_fim__gt=data_atual,
        estado='Pendente',
    ).count()

    tarefas_concluídas = modelo.objects.filter(
        data_fim__lte=data_atual,
        estado='Concluída',
    ).count()

    return {
        'pendentes': tarefas_pendentes,
        'concluídas': tarefas_concluídas,
    }
@login_required
def tarefa_adicionar(request):
    form = TarefaForm(request.POST or None)
    context = {
        'formulario': form,
    }
    if form.is_valid():
        form.save()
        return redirect('tarefa_listar')

    return render(request, 'Desempenho/Desempenho.html', context)


@login_required
def tarefa_editar(request, pk):
    tarefa = Tarefa.objects.get(pk=pk)
    form = TarefaForm(request.POST or None,instance=tarefa)

    context = {
        'formulario': form,
        'tarefa': tarefa,
    }
    if form.is_valid():
        form.save()

        return redirect('tarefa_listar')


    return render(request, 'Desempenho/Desempenho.html', context)

@login_required
def DelegarTarefa(request, pk):
    tarefa = Tarefa.objects.get(pk=pk)
    form = Delegartarefas(request.POST or None,instance=tarefa)

    context = {
        'formulario': form,
        'tarefa': tarefa,
    }
    if form.is_valid():
        form.save()
        return redirect('tarefa_listar')
    return render(request, 'Desempenho/Desempenho.html', context)
@login_required
def tarefa_concluida(request, pk):
    tarefa = Tarefa.objects.get(pk=pk)
    tarefa.estado='Concluída'
    tarefa.data_estado=datetime.datetime.now()
    tarefa.save()
    return redirect('tarefa_listar')
def tarefa_aprovada(request, pk):
    tarefa = Tarefa.objects.get(pk=pk)
    tarefa.Aprovado='Sim'
    try:
        tarefa.save()
    except Exception as e:
        print(e)
    return redirect('tarefa_listar')




@login_required
def tarefa_listar(request):
    tarefas = Tarefa.objects.filter(hierarquia_responsabilidade=request.user)
    context = {
        'tarefas': tarefas,
    }
    return render(request, 'Desempenho/DesempenhoLista.html', context)

@login_required
def Desempenho(request):
    tarefas1 = Tarefa.objects.values('data_inicio__month').annotate(
        count=Count('id'))
    contagem_tarefas_por_mes = Tarefa.objects.annotate(mes=ExtractMonth('data_atualizado')).values('mes').annotate(total=Count('id')).order_by('mes')


    tarefas_pendentes = Tarefa.objects.filter(
        hierarquia_responsabilidade=request.user,
        estado='Pendente',
        data_fim__gte=date.today(),
    ).count()
    tarefas_concluídas = Tarefa.objects.filter(
        estado='Concluída',
        hierarquia_responsabilidade=request.user,

        data_fim__gte=date.today(),

    ).count()

    tarefas_Aprovadas = Tarefa.objects.filter(
        Aprovado='Sim',
        data_fim__gte=date.today(),
        hierarquia_responsabilidade=request.user,

    ).count()

    tarefas = Tarefa.objects.filter(
        data_fim__gte=date.today(),
        hierarquia_responsabilidade=request.user,

    ).count()
    percentagem = (tarefas_concluídas / tarefas) * 100
    percentagem = round(percentagem)

    percentagemD = (tarefas_Aprovadas/tarefas)*100
    percentagemD = round(percentagemD)
    pendenteD=tarefas-tarefas_Aprovadas

    context = {
        'tarefas_pendentes': tarefas_pendentes,
        'tarefas_concluídas': tarefas_concluídas,
        'tarefas_Aprovadas': tarefas_Aprovadas,

        'tarefas': tarefas,
        'percentagem':percentagem,
        'percentagemD':percentagemD,
        'pendenteD':pendenteD,
    }
    print(tarefas,tarefas_Aprovadas)

    meses = dict(enumerate(calendar.month_name))

    # Você pode acessar as informações assim:
    for item in contagem_tarefas_por_mes:
        numero_do_mes = item['mes']
        total = item['total']
        nome_do_mes = meses.get(numero_do_mes, 'Mês Desconhecido')
        print(f"Tarefas feitas no mês de {nome_do_mes}: {total}")

    return render(request, 'Desempenho/Desempenhografico.html',context)


@login_required
def tarefa_eliminar(request, pk):
    tarefa = Tarefa.objects.get(pk=pk)
    tarefa.delete()
    return redirect('tarefa_listar')


@login_required
def performance_adicionar(request):
    form = PerformanceForm(request.POST or None)
    context = {
        'formulario': form,
    }
    if form.is_valid():
        form.save()
        return redirect('performance_listar')

    return render(request, 'Desempenho/bolewer.html', context)

@login_required
def performance_editar(request, pk):
    meta = PerformanceModel.objects.get(pk=pk)
    form = PerformanceForm(request.POST or None, instance=meta)
    context = {
        'formulario': form,
        'meta': meta,
    }
    if form.is_valid():
        form.save()
        return redirect('performance_listar')

    return render(request, 'Desempenho/bolewer.html', context)

@login_required
def performance_eliminar(request, pk):
    meta = PerformanceModel.objects.get(pk=pk)
    meta.delete()
    return redirect('performance_listar')

@login_required
def performance_listar(request):
    metas = PerformanceModel.objects.all()
    context = {
        'metas': metas,
    }
    return render(request, 'Desempenho/Listarbolewer.html', context)

@login_required
def perfomacemes_adicionar(request):
    form = PerfomacemesForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('perfomacemes_listar')
    context = {'formulario': form}
    return render(request, 'Desempenho/bolewerResul.html', context)
@login_required
def perfomacemes_editar(request, pk):
    meta = Resultados_das_Metas.objects.get(pk=pk)
    form = PerfomacemesForm(request.POST or None, instance=meta)
    if form.is_valid():
        form.save()
        return redirect('perfomacemes_listar')
    context = {'formulario': form, 'meta': meta}
    return render(request, 'Desempenho/bolewerResul.html', context)
@login_required
def perfomacemes_eliminar(request, pk):
    meta = Resultados_das_Metas.objects.get(pk=pk)
    meta.delete()
    return redirect('perfomacemes_listar')
@login_required
def perfomacemes_listar(request):
    metas = Resultados_das_Metas.objects.filter(
        data_mes__month=datetime.datetime.now().month,
        data_mes__year=datetime.datetime.now().year
    )
    context = {'metas': metas}
    return render(request, 'Desempenho/ListarbolewerResult.html', context)
@login_required
def perfomacemes_detalhes(request, pk):
    meta = Resultados_das_Metas.objects.get(pk=pk)
    niveis = PerformanceModel.objects.all()
    meses = MESES
    context = {'meta': meta, 'niveis': niveis, 'meses': meses}
    return render(request, 'perfomacemes/perfomacemes_detalhes.html', context)

def DesempenhoAnual(request):
    metas = Resultados_das_Metas.objects.filter(
        data_mes__month=request.POST.get('mes'),
        data_mes__year=request.POST.get('ano')

    )
    dados_performace = Resultados_das_Metas.objects.filter(
        Metas__unidade_meta="%",
        data_mes__month=datetime.datetime.now().month,
        data_mes__year=datetime.datetime.now().year

        )
    dados_performace2 = Resultados_das_Metas.objects.filter(
        Metas__unidade_meta="hr",
        data_mes__month=datetime.datetime.now().month,
        data_mes__year=datetime.datetime.now().year
    )
    if request.POST:
        dados_performace = Resultados_das_Metas.objects.filter(
            Metas__unidade_meta="%",
            data_mes__month=request.POST.get('mes'),
            data_mes__year=request.POST.get('ano')

        )
        dados_performace2 = Resultados_das_Metas.objects.filter(
            Metas__unidade_meta="hr",
            data_mes__month=request.POST.get('mes'),
            data_mes__year=request.POST.get('ano')
        )


    # Formate os dados para serem usados no gráfico
        dados_grafico = []
        dados_grafico2 = []

        for dado in dados_performace:
            dados_grafico.append({
                'y': dado.Metas.nome_meta,
                'a': float(dado.Baseline),
                'b': float(dado.Plan)
            })

        for dado in dados_performace2:
            dados_grafico2.append({
                'y': dado.Metas.nome_meta,
                'a': float(dado.Baseline),
                'b': float(dado.Plan)
            })

        context = {'metas': metas,
                   'dados_grafico': dados_grafico,
                   'dados_grafico2': dados_grafico2

                   }
    else:
        dados_grafico = []
        dados_grafico2 = []

        for dado in dados_performace:
            dados_grafico.append({
                'y': dado.Metas.nome_meta,
                'a': float(dado.Baseline),
                'b': float(dado.Plan)
            })

        for dado in dados_performace2:
            dados_grafico2.append({
                'y': dado.Metas.nome_meta,
                'a': float(dado.Baseline),
                'b': float(dado.Plan)
            })

        context = {'metas': metas,
                   'dados_grafico': dados_grafico,
                   'dados_grafico2': dados_grafico2

                   }


    return render (request,'Desempenho/DesemenhoAnual.html',context)


