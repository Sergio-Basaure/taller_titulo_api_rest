import re
from rest_framework import serializers
from .models import Cliente

class ClienteSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Cliente
        # fields o exclude
        fields = '__all__'


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

# class ClienteSerializer(serializers.Serializer):

#     # def validate_rut(self,value):
#     #     rut_validador = re.compile(r'^([0-9]{7,8}+-[0-9kK]{1})$')
#     #     if value == rut_validador:
#     #         return value
#     #     else:

#     #         raise serializers.ValidationError('Formato del rut incorrecto ')