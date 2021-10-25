from rest_framework import serializers
from .models import Local, Reclamos, TipoReclamo

class LocalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Local
        fields = '__all__'

class TipoReclamoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoReclamo

    def to_representation(self, instance):
        return {
            'nombre' : instance['nombre']
        }

class ReclamoSerializer(serializers.ModelSerializer):
    id_tipo = TipoReclamoSerializer
    id_local = serializers.StringRelatedField()
    class Meta:
        model = Reclamos
        fields = '__all__'