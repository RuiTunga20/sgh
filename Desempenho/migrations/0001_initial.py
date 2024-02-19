# Generated by Django 4.2.4 on 2024-01-05 23:48

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tarefa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('descricao', models.TextField()),
                ('data_inicio', models.DateField()),
                ('data_fim', models.DateField()),
                ('prioridade', models.IntegerField()),
                ('estado', models.CharField(choices=[('Pendente', 'Pendente'), ('Em Andamento', 'Em Andamento'), ('Concluída', 'Concluída')], default='Pendente', max_length=100)),
                ('data_estado', models.DateField()),
                ('Aprovado', models.CharField(choices=[('Pendente', 'Pendente'), ('Em Andamento', 'Em Andamento'), ('Concluída', 'Concluída')], default='Pendente', max_length=100)),
                ('data_atualizado', models.DateField(auto_now=True)),
                ('hierarquia_responsabilidade', models.ManyToManyField(related_name='tarefas', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
