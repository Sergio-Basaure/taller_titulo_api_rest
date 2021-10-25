# Generated by Django 3.2.8 on 2021-10-25 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('local', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='local',
            name='contacto',
            field=models.IntegerField(verbose_name='Conatcto'),
        ),
        migrations.AlterField(
            model_name='local',
            name='direccion',
            field=models.CharField(max_length=200, unique=True, verbose_name='Dirección del local'),
        ),
        migrations.AlterField(
            model_name='local',
            name='estado',
            field=models.BooleanField(default=True, verbose_name='Estado'),
        ),
        migrations.AlterField(
            model_name='local',
            name='fecha_actualizacion',
            field=models.DateField(auto_now=True, verbose_name='fecha de actualización'),
        ),
        migrations.AlterField(
            model_name='local',
            name='fecha_creacion',
            field=models.DateField(auto_now_add=True, verbose_name='Fecha de creación'),
        ),
        migrations.AlterField(
            model_name='local',
            name='nombre',
            field=models.CharField(max_length=100, unique=True, verbose_name='Nombre del local'),
        ),
        migrations.AlterField(
            model_name='reclamos',
            name='fecha_actualizacion',
            field=models.DateField(auto_now=True, verbose_name='fecha de actualización'),
        ),
        migrations.AlterField(
            model_name='reclamos',
            name='fecha_creacion',
            field=models.DateField(auto_now_add=True, verbose_name='Fecha de creación'),
        ),
        migrations.AlterField(
            model_name='tiporeclamo',
            name='fecha_actualizacion',
            field=models.DateField(auto_now=True, verbose_name='fecha de actualización'),
        ),
        migrations.AlterField(
            model_name='tiporeclamo',
            name='fecha_creacion',
            field=models.DateField(auto_now_add=True, verbose_name='Fecha de creación'),
        ),
    ]
