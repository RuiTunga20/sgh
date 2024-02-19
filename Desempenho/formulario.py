from django import forms
from .models import Tarefa,PerformanceModel,NivelPerforme,Resultados_das_Metas,MESES

class TarefaForm(forms.ModelForm):
    class Meta:
        model = Tarefa
        fields = '__all__'

        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'id': 'titulo'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'id': 'descricao'}),
            'data_inicio': forms.DateInput(attrs={'type': 'date', 'class': 'form-control', 'id': 'data_inicio'}),
            'data_fim': forms.DateInput(attrs={'type': 'date', 'class': 'form-control', 'id': 'data_fim'}),
            'prioridade': forms.NumberInput(attrs={'class': 'form-control', 'id': 'prioridade'}),
            'estado': forms.Select(attrs={'class': 'form-select', 'id': 'estado'}),
            'Aprovado': forms.Select(attrs={'class': 'form-select', 'id': 'Aprovado'}),


            'data_estado': forms.DateInput(attrs={'type': 'date', 'class': 'form-control', 'id': 'data_fim'}),
            'hierarquia_responsabilidade': forms.SelectMultiple(attrs={'class': 'form-select', 'id': 'hierarquia_responsabilidade'}),  # For ManyToManyField
        }



class Delegartarefas(forms.ModelForm):
    class Meta:
        model = Tarefa
        fields = ['hierarquia_responsabilidade']

        widgets = {

            'hierarquia_responsabilidade': forms.SelectMultiple(attrs={'class': 'form-select', 'id': 'hierarquia_responsabilidade'}),  # For ManyToManyField
        }


class PerformanceForm(forms.ModelForm):
    class Meta:
        model = PerformanceModel
        fields = '__all__'

        widgets = {
            'NivePr': forms.SelectMultiple(attrs={'class': 'form-select', 'id': 'NivePr'}),  # Select for ForeignKey
            'nome_meta': forms.TextInput(attrs={'class': 'form-control', 'id': 'nome_meta'}),
            'formula_meta': forms.Textarea(attrs={'class': 'form-control', 'id': 'formula_meta'}),
            'Baseline': forms.NumberInput(attrs={'class': 'form-control', 'id': 'Baseline'}),
            'Hoshin': forms.NumberInput(attrs={'class': 'form-control', 'id': 'Hoshin'}),
            'unidade_meta': forms.Select(attrs={'class': 'form-select', 'id': 'unidade_meta'}),
        }


class PerfomacemesForm(forms.ModelForm):
    class Meta:
        model = Resultados_das_Metas
        fields = '__all__'
        exclude=('status_indicador',)

        widgets = {
            'Metas': forms.Select(attrs={'class': 'form-select', 'id': 'Metas'}),  # Select for ForeignKey
            'Plan': forms.NumberInput(attrs={'class': 'form-control', 'id': 'Plan'}),
            'status_indicador': forms.Select(attrs={'class': 'form-select', 'id': 'status_indicador'}),
            'data_mes': forms.DateInput(attrs={'type': 'date', 'class': 'form-control', 'id': 'data_medicao'}),
        }

        choices = [
            ('verde', 'Verde'),
            ('amarelo', 'Amarelo'),
            ('vermelho', 'Vermelho'),
        ]

class PlanForm(forms.ModelForm):
    class Meta:
        model = Resultados_das_Metas
        fields = ('Metas','Plan')

        widgets = {
            'Metas': forms.Select(attrs={'class': 'form-select', 'id': 'Metas'}),  # Select for ForeignKey
            'Plan': forms.NumberInput(attrs={'class': 'form-control', 'id': 'Plan'}),

        }

