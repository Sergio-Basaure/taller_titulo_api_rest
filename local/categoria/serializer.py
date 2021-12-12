from rest_framework import serializers
from .models import TipoReclamo

class TipoReclamoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoReclamo
        exclude = ('estado', 'fecha_creacion', 'fecha_actualizacion')
