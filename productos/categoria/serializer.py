from rest_framework import serializers
from .models import CategoriaProducto
from ..producto.serializer import ProductoSerializer


class CategoriaProductoSerializer(serializers.ModelSerializer):
    # producto_categoria = ProductoSerializer(many = True, read_only = True)
    class Meta:
        model = CategoriaProducto
        exclude = ('estado', 'fecha_creacion', 'fecha_actualizacion')
        # fields = ['id', 'nombre', 'producto_categoria']