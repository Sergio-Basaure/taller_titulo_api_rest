from rest_framework import serializers
from .models import CategoriaServicio

class CategoriaServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaServicio
        exclude = ('estado', 'fecha_creacion', 'fecha_actualizacion')