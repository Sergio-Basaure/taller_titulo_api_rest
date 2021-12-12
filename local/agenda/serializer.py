from rest_framework import serializers
from .models import Agenda, Hora

class AgendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agenda
        fields = '__all__'

class HoraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hora
        fields = '__all__'