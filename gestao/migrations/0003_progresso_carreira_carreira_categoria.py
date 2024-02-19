# Generated by Django 4.2.4 on 2023-12-27 14:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestao', '0002_alter_nivelcarreira_bandafuncional'),
    ]

    operations = [
        migrations.CreateModel(
            name='Progresso_Carreira',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('descricao', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='carreira',
            name='categoria',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='gestao.progresso_carreira'),
            preserve_default=False,
        ),
    ]
