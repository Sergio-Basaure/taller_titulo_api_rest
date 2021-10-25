from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import LoginToken
from ..serializers import ClienteSerializer
from ..models import Cliente

class LoginApi(TokenObtainPairView):
    serializer_class = LoginToken

    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')
        cliente = authenticate(
            email = email,
            password = password
        )
        if cliente:
            login_serializer = self.serializer_class(data = request.data)
            if login_serializer.is_valid():
                cliente_serializer = ClienteSerializer(cliente)
                return Response({
                    'token' : login_serializer.validated_data.get('access'),
                    'refresh-token' : login_serializer.validated_data.get('refresh'),
                    'cliente' : cliente_serializer.data,
                    'mensaje' : 'Inicio de session exitoso'
                }, status = status.HTTP_200_OK)
            return Response({'error': 'Password o nombre de usuario incorrecto'})
        return Response({'error': 'Password o nombre de usuario incorrecto'}, status = status.HTTP_401_UNAUTHORIZED)

class Logout(GenericAPIView):
    def post(self, request, *args, **kwargs):
        cliente = Cliente.objects.filter(id = request.data.get('cliente'))
        if cliente.exists():
            RefreshToken.for_user(cliente.first())
            return Response({'mensaje' : 'Session cerrada exitosamente'}, status = status.HTTP_200_OK)
        return Response({'error' : 'Cliente no existe'}, status = status.HTTP_400_BAD_REQUEST)