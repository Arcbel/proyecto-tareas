# Generated by Django 3.2.13 on 2023-08-08 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrar', '0002_auto_20230804_0016'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tarea',
            options={'verbose_name_plural': 'Mis lista de tareas'},
        ),
        migrations.AlterField(
            model_name='tarea',
            name='titulo',
            field=models.CharField(default='---', max_length=64),
        ),
    ]
