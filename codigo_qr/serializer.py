from rest_framework import serializers
from .models import QrAgenda

class QrAgendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = QrAgenda
        fields = '__all__'