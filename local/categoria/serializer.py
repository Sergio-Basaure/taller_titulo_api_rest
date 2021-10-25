from rest_framework import serializers
from .models import TipoReclamo

class TipoReclamoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoReclamo
        fields = '__all__'
