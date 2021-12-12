from rest_framework import serializers
from ..models import Cliente
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class LoginToken(TokenObtainPairSerializer):
    pass

class LogoutSerializar(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'