from rest_framework import serializers
from .models import Local

class LocalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Local
        exclude = ('estado', 'fecha_creacion', 'fecha_actualizacion')
