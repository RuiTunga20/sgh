# Generated by Django 4.2.4 on 2024-02-18 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Desempenho', '0010_remove_perfomacemes_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfomacemes',
            name='Mes',
            field=models.DateField(default=1),
            preserve_default=False,
        ),
    ]