# Generated by Django 4.2.4 on 2024-02-18 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Desempenho', '0018_alter_resultados_das_metas_plan_delete_perfomacemes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resultados_das_metas',
            name='Plan',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]