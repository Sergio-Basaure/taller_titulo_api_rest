from rest_framework import serializers
from .models import Reclamos

class ReclamoSerializer(serializers.ModelSerializer):
    id_tipo = serializers.StringRelatedField()
    id_local = serializers.StringRelatedField()
    class Meta:
        model = Reclamos
        fields = '__all__'