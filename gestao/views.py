from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from gestao.formulario import *
from gestao.models import *
from django.contrib.auth.decorators import login_required


# Create your views here.

def Colaborador(request):
        formulario=ColaboradorForm(request.POST or None,request.FILES or None)
        context={
            'formulario':formulario
        }
        if formulario.is_valid():
            formulario.save()
            return redirect('/Gestao/Lista')

        return render (request,'gestao/Colaborador.html',context)
def Edite_Colaborador(request, id):

    formulario = ColaboradorForm(request.POST or None, instance=Colaboradores.objects.get(id=id))
    context = {
        'formulario': formulario
    }
    if formulario.is_valid():
        formulario.save()
        return redirect('/Gestao/Lista')

    return render(request, 'gestao/Colaborador.html', context)
def Lista_Colaborador(request):
    Listar=Colaboradores.objects.all()
    context={
        'Listar':Listar
    }
    return render(request, 'gestao/ColaboradorLista.html', context)
def Eliminar_colaborador (request,id):
    funcionario=Colaboradores.objects.get(id=id)
    funcionario.delete()
    return redirect('/Gestao/Lista')


def Adicionar_Carreira(request):
    form = CarreiraForm(request.POST or None)
    context = {
        'formulario': form,
    }
    if form.is_valid():
        form.save()
        return redirect('listar_carreira')

    return render(request, 'gestao/carreira.html', context)

def Editar_Carreira(request, id):
    carreira = Carreira.objects.get(id=id)
    form = CarreiraForm(request.POST or None, instance=carreira)
    context = {
        'formulario': form,
    }
    if form.is_valid():
        form.save()
        return redirect('listar_carreira')

    return render(request, 'gestao/carreira.html', context)

def Eliminar_Carreira(request, id):
    carreira = Carreira.objects.get(id=id)
    carreira.delete()
    return redirect('listar_carreira')

def Listar_Carreira(request):
    carreiras = Carreira.objects.all()
    context = {
        'carreiras': carreiras,
    }
    return render(request, 'gestao/carreiraLista.html', context)

def Adicionar_NivelCarreira(request):
    form = NivelCarreiraForm(request.POST or None)
    context = {
        'formulario': form,
    }
    if form.is_valid():
        form.save()
        return redirect('listar_nivelcarreira')

    return render(request, 'gestao/Nivelcarreira.html', context)

def Editar_NivelCarreira(request, id):
    nivelcarreira = NivelCarreira.objects.get(id=id)
    form = NivelCarreiraForm(request.POST or None, instance=nivelcarreira)
    context = {
        'formulario': form,
    }
    if form.is_valid():
        form.save()
        return redirect('listar_nivelcarreira')

    return render(request, 'gestao/Nivelcarreira.html', context)

def Eliminar_NivelCarreira(request, id):
    nivelcarreira = NivelCarreira.objects.get(id=id)
    nivelcarreira.delete()
    return redirect('listar_nivelcarreira')

def Listar_NivelCarreira(request):
    nivelcarreiras = NivelCarreira.objects.all()
    context = {
        'nivelcarreira': nivelcarreiras,
    }
    return render(request, 'gestao/NivelLista.html', context)


def Adicionar_Departamento(request):
    form = DepartamentoForm(request.POST or None)
    context = {
        'formulario': form,
    }
    if form.is_valid():
        form.save()
        return redirect('listar_departamento')

    return render(request, 'gestao/Departamento.html', context)

def Editar_Departamento(request, id):
    departamento = Departamento.objects.get(id=id)
    form = DepartamentoForm(request.POST or None, instance=departamento)
    context = {
        'formulario': form,
    }
    if form.is_valid():
        form.save()
        return redirect('listar_departamento')

    return render(request, 'gestao/Departamento.html', context)

def Eliminar_Departamento(request, id):
    departamento = Departamento.objects.get(id=id)
    departamento.delete()
    return redirect('listar_departamento')

def Listar_Departamento(request):
    departamentos = Departamento.objects.all()
    context = {
        'departamentos': departamentos,
    }
    return render(request, 'gestao/Listardepartamento.html', context)

def Adicionar_Funcao(request):
    form = FuncaoForm(request.POST or None)
    context = {
        'formulario': form,
    }
    if form.is_valid():
        form.save()
        return redirect('listar_funcao')

    return render(request, 'gestao/funcao.html', context)

def Editar_Funcao(request, id):
    funcao = Funcao.objects.get(id=id)
    form = FuncaoForm(request.POST or None, instance=funcao)
    context = {
        'formulario': form,
    }
    if form.is_valid():
        form.save()
        return redirect('listar_funcao')

    return render(request, 'gestao/funcao.html', context)

def Eliminar_Funcao(request, id):
    funcao = Funcao.objects.get(id=id)
    funcao.delete()
    return redirect('listar_funcao')

def Listar_Funcao(request):
    funcoes = Funcao.objects.all()
    context = {
        'funcoes': funcoes,
    }
    return render(request, 'gestao/FuncaoLista.html', context)

def justificativa_adicionar(request):
    form = JustificativoForm(request.POST or None, request.FILES)
    context = {
        'formulario': form,
    }
    if form.is_valid():
        form.save()
        return redirect('justificativo_listar')

    return render(request, 'gestao/justificativo.html', context)

def justificativa_editar(request, pk):
    justificativa = Justificativo.objects.get(pk=pk)
    form = JustificativoForm(request.POST , request.FILES,instance=justificativa)
    context = {
        'formulario': form,
    }
    if form.is_valid():
        form.save()
        return redirect('justificativo_listar')

    return render(request, 'gestao/justificativo.html', context)

def justificativa_listar(request):
    justificativas = Justificativo.objects.all()
    context = {
        'justificativos': justificativas,
    }
    return render(request, 'gestao/JustificativoLista.html', context)
def justificativa_eliminar(request, pk):
    justificativa = Justificativo.objects.get(pk=pk)
    justificativa.delete()
    return redirect('justificativo_listar')


@login_required
def curso_adicionar(request):
    form = CursoForm(request.POST or None,request.FILES)
    context = {
        'formulario': form,
    }
    if form.is_valid():
        form.save()
        return redirect('curso_listar')  # Assuming a view for listing courses

    return render(request, 'gestao/Curso.html', context)  # Adapt the template path

@login_required
def curso_editar(request, pk):
    curso = CursosPagos.objects.get(pk=pk)
    form = CursoForm(request.POST or None, instance=curso)
    context = {
        'formulario': form,
        'curso': curso,
    }
    if form.is_valid():
        form.save()
        return redirect('curso_listar')  # Assuming a view for listing courses

    return render(request, 'gestao/Curso.html', context)  # Adapt the template path

@login_required
def curso_eliminar(request, pk):
    curso = CursosPagos.objects.get(pk=pk)
    curso.delete()
    return redirect('curso_listar')

@login_required
def curso_listar(request):
    cursos = CursosPagos.objects.all()
    context = {
        'cursos': cursos,
    }
    return render(request, 'gestao/Cursolista.html', context)


