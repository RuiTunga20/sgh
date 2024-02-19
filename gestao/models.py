from django.db import models

# Create your models here.
motivos = [
    ('acidente_de_trabalho', 'Acidente de trabalho'),
    ('doença', 'Doença'),
    ('ausencia_por_funeral', 'Ausência por funeral'),
    ('doacao_de_sangue', 'Doação de sangue'),
    ('ausencia_em_servico', 'Ausência em serviço'),
    ('falecimento_de_familiar_do_1_grau', 'Falecimento de familiar do 1º grau'),
    ('casamento', 'Casamento'),
    ('falecimento_de_familiar_do_2_grau', 'Falecimento de familiar do 2º grau'),
    ('convocacao_oficial', 'Convocação oficial'),
    ('maternidade/paternidade', 'Maternidade/Paternidade'),
    ('dispensa_mensal_de_servico', 'Dispensação mensal de serviço'),
    ('tratamento_de_assuntos_pessoais', 'Tratamento de assuntos pessoais'),
]
Aprovado = [
    ('Sim', 'Sim'),
    ('Não', 'Não'),

]
class Progresso_Carreira(models.Model):
    nome=models.CharField(max_length=255,blank=False)
    descricao=models.TextField()

    def __str__(self):
        return self.nome

class Carreira(models.Model):
    nome=models.CharField(max_length=255,blank=False)
    categoria=models.ForeignKey(Progresso_Carreira,on_delete=models.CASCADE)
    descricao=models.TextField()
    def __str__(self):
         return self.nome
class NivelCarreira(models.Model):
    nome=models.CharField(max_length=255,blank=False,null=False)
    carreira=models.ForeignKey(Carreira,on_delete=models.CASCADE)
    bandafuncional=models.IntegerField()
    salario=models.DecimalField(max_digits=12,decimal_places=2)

    def get_carreira(self):
        return self.carreira.categoria.nome

    def __str__(self):
        return self.nome + " - "  + str(self.carreira)+" - "+ str(self.carreira.categoria)



class Departamento(models.Model):
    nome=models.CharField(max_length=255,blank=False)
    descricao=models.TextField()
    def __str__(self):
        return self.nome

class Funcao(models.Model):
    codigo=models.CharField(max_length=10,blank=False,null=False,unique=True)
    nome=models.CharField(max_length=255,blank=False)
    departamento=models.ForeignKey(Departamento,on_delete=models.CASCADE)
    nivelCarreira=models.ManyToManyField(NivelCarreira)
    def __str__(self):
        return self.nome

class Colaboradores(models.Model):
    nome_completo = models.CharField('Nome Completo',max_length=255)
    bi = models.CharField(max_length=14)
    data_nascimento = models.DateField(default='2000-11-11')
    naturalidade = models.CharField(max_length=255)
    nacionalidade = models.CharField(max_length=255)
    genero = models.CharField(max_length=1, choices=[("M", "Masculino"), ("F", "Feminino")])
    morada = models.CharField(max_length=255)
    telefone = models.CharField(max_length=10)
    email = models.EmailField()
    DataIncio=models.DateField('Inicio de Contrato',default='2018-11-11')
    DataFim=models.DateField('Fim do Contrato',default='2018-11-11',null=True,blank=True)
    TipodeContrato=models.CharField(verbose_name="Tipo de Contrato",max_length=200, choices=[("Tempo Determinado", "Tempo Determinado"), ("Indeterminado", "Indeterminado")])
    funcao=models.ForeignKey(Funcao,on_delete=models.CASCADE,default=1,verbose_name='Função')
    Curriculo=models.FileField('Currículo',upload_to='media/Funcionario',blank=True,null=True)
    ExtratoBancario=models.FileField('Extrato Bancário',upload_to='media/Funcionario',blank=True,null=True)
    AtestadoMedico=models.FileField('Atestado Médico',upload_to='media/Funcionario',blank=True,null=True)
    FBI=models.FileField('Copia do BI',upload_to='media/Funcionario',blank=True,null=True)
    Certificado=models.FileField('Certificado',upload_to='media/Funcionario',blank=True,null=True)
    NFI=models.FileField('Número de Contribuinte',upload_to='media/Funcionario',blank=True,null=True)

    nivel_carreira_atual = models.ForeignKey(NivelCarreira, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.nome_completo

    def get_salario(self):
        return self.nivel_carreira_atual.salario

class CursosPagos(models.Model):
    colaborador = models.ForeignKey(Colaboradores, on_delete=models.CASCADE)
    curso = models.CharField(max_length=255)
    instituicao = models.CharField('Instituição',max_length=255)
    periodo = models.CharField(max_length=255)
    valor_pago = models.DecimalField('Custo',max_digits=10, decimal_places=2)
    nota = models.FloatField(null=True, blank=True)

    # Adicionando as novas colunas
    data_inicio = models.DateField('Data de Início do Curso')
    data_fim = models.DateField('Data do Fim do Curso',null=True, blank=True)
    status = models.CharField('Estado do Curso',max_length=20, choices=[("Concluído", "Concluído"), ("Em andamento", "Em andamento"), ("Não concluído", "Não concluído")])

    def __str__(self):
        return f"{self.colaborador.nome_completo} - {self.curso}"

class Justificativo(models.Model):
    Colaboradores=models.ForeignKey(Colaboradores,on_delete=models.CASCADE)
    Motivo=models.CharField(max_length=100,choices=motivos)
    inicio_falta=models.DateField()
    inicio_Fim=models.DateField(blank=True,null=True)
    Justificado=models.CharField(max_length=100,choices=Aprovado,default='Não')
    ficheiro=models.FileField(upload_to='media/justificativo',blank=True,null=True)
    def __str__(self):
        return self.Colaboradores.nome_completo

