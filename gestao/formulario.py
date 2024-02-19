from django import forms
from .models import Colaboradores

from django import forms
from .models import *


class ColaboradorForm(forms.ModelForm):

    class Meta:
        model = Colaboradores
        fields = '__all__'

        widgets = {
            'nome_completo': forms.TextInput(attrs={'class': 'form-control', 'id': 'nome_completo','required':'false'}),
            'bi': forms.TextInput(attrs={'class': 'form-control', 'id': 'bi'}),
            'data_nascimento': forms.DateInput(attrs={'type': 'date', 'class': 'form-control', 'id': 'data_nascimento'}),
            'naturalidade': forms.TextInput(attrs={'class': 'form-control', 'id': 'naturalidade'}),
            'nacionalidade': forms.TextInput(attrs={'class': 'form-control', 'id': 'nacionalidade'}),
            'genero': forms.Select(attrs={'class': 'form-select', 'id': 'genero'}),
            'morada': forms.TextInput(attrs={'class': 'form-control', 'id': 'morada'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control', 'id': 'telefone'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'id': 'email'}),
            'funcao': forms.Select(attrs={'class': 'form-select', 'id': 'funcao'}),
            'DataFim': forms.DateInput(attrs={'type': 'date', 'class': 'form-control', 'id': 'data_fim'}),
            'DataIncio': forms.DateInput(attrs={'type': 'date', 'class': 'form-control', 'id': 'data_fim'}),

            'nivel_carreira_atual': forms.Select(attrs={'class': 'form-select', 'id': 'nivel_carreira_atual'}),
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['Curriculo'] = forms.FileField(label='Currículo ', required=False)
            self.fields['ExtratoBancario'] = forms.FileField(label='Extrato Bancário', required=False)
            self.fields['AtestadoMedico'] = forms.FileField(label='Atestado Médico', required=False)
            self.fields['FBI'] = forms.FileField(label='Copia do BI', required=False)
            self.fields['Certificado'] = forms.FileField(label='Certificado', required=False)
            self.fields['NFI'] = forms.FileField(label='Número de Contribuinte', required=False)
            self.fields['enctype'] = 'multipart/form-data'

            for field_name, field in self.fields.items():
                field.widget.attrs.update({'class': 'form-control', 'id': field_name})



class CarreiraForm(forms.ModelForm):

    class Meta:
        model = Carreira
        fields = '__all__'

        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'id': 'nome'}),
            'categoria': forms.Select(attrs={'class': 'form-select', 'id': 'categoria'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'id': 'descricao'}),
        }


class NivelCarreiraForm(forms.ModelForm):

    class Meta:
        model = NivelCarreira
        fields = '__all__'

        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'id': 'nome'}),
            'carreira': forms.Select(attrs={'class': 'form-select', 'id': 'carreira'}),
            'bandafuncional': forms.NumberInput(attrs={'class': 'form-control', 'id': 'bandafuncional'}),
            'salario': forms.NumberInput(attrs={'class': 'form-control', 'id': 'salario'}),
        }

class DepartamentoForm(forms.ModelForm):

    class Meta:
        model = Departamento
        fields = '__all__'

        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'id': 'nome'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'id': 'descricao'}),
        }

class FuncaoForm(forms.ModelForm):

    class Meta:
        model = Funcao
        fields = '__all__'

class JustificativoForm(forms.ModelForm):

    class Meta:
        model = Justificativo
        fields = '__all__'
        widgets = {
            'inicio_falta':  forms.DateInput(attrs={'type': 'date', 'class': 'form-control', 'id': 'data_nascimento'}),
            'inicio_Fim':  forms.DateInput(attrs={'type': 'date', 'class': 'form-control', 'id': 'data_nascimento'}),
        }

class CursoForm(forms.ModelForm):
    class Meta:
        model = CursosPagos
        fields = '__all__'

        widgets = {
            'curso': forms.TextInput(attrs={'class': 'form-control', 'id': 'curso'}),
            'instituicao': forms.TextInput(attrs={'class': 'form-control', 'id': 'instituicao'}),
            'periodo': forms.TextInput(attrs={'class': 'form-control', 'id': 'periodo'}),
            'valor_pago': forms.NumberInput(attrs={'class': 'form-control', 'id': 'valor_pago'}),
            'nota': forms.NumberInput(attrs={'class': 'form-control', 'id': 'nota'}),
            'data_inicio': forms.DateInput(attrs={'type': 'date', 'class': 'form-control', 'id': 'data_inicio'}),
            'data_fim': forms.DateInput(attrs={'type': 'date', 'class': 'form-control', 'id': 'data_fim'}),
            #'status': forms.Select(attrs={'class': 'form-select', 'id': 'status'}),
            'colaborador': forms.Select(attrs={'class': 'form-select', 'id': 'colaborador'}),  # Select for ForeignKey
        }

