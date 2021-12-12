from rest_framework import serializers
from .models import Producto


class ProductoSerializer(serializers.ModelSerializer):
    # id_categoria = serializers.StringRelatedField()
    class Meta:
        model = Producto
        # exclude = ('estado', 'fecha_creacion', 'fecha_actualizacion')
        fields = '__all__'