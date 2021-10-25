from rest_framework import serializers
from .models import Cliente

class ClienteSerializerList(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        exclude = ('estado', 'last_login', 'fecha_creacion', 'fecha_actualizacion')

    def create(self, validated_data):
        cliente = Cliente(**validated_data)
        cliente.set_password(validated_data['password'])
        cliente.save()
        return cliente

    def update(self, instance, validated_data):
        cliente_update = super().update(instance, validated_data)
        cliente_update.set_password(validated_data['password'])
        cliente_update.save()
        return cliente_update