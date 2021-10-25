from rest_framework import serializers
from .models import Cliente

class ClienteSerializerList(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        exclude = ('password', 'estado', 'last_login', 'fecha_creacion', 'fecha_actualizacion')