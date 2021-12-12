from rest_framework import serializers
from .models import Reclamos

class ReclamoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reclamos
        fields = ('id', 'descripcion', 'id_tipo', 'id_local')