# Generated by Django 3.2.8 on 2021-12-13 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=50, unique=True, verbose_name='Usuario')),
                ('email', models.EmailField(max_length=100, unique=True, verbose_name='Correo electrónico')),
                ('nombres', models.CharField(max_length=100, verbose_name='Nombres del usuario')),
                ('apellidos', models.CharField(max_length=100, verbose_name='Apellidos del usuario')),
                ('rut', models.CharField(max_length=10, unique=True, verbose_name='Rut del usuario')),
                ('contacto', models.IntegerField(verbose_name='Contacto del usuario')),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Usuario',
            },
        ),
    ]
