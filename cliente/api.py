from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Cliente
from .serializers import ClienteSerializer
from .serializer_list import ClienteSerializerList

class ClienteViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = ClienteSerializerList
    queryset = Cliente.objects.filter(estado = True)




#     def get(self,request):
#         cliente = Cliente.objects.filter(estado = True)
#         cliente_serializer = ClienteSerializer(cliente, many = True)
#         return Response(cliente_serializer.data)

#     def post(self,request):
#         cliente_serializer = ClienteSerializer(data = request.data)
#         if cliente_serializer.is_valid():
#             cliente_serializer.save()
#             return Response(cliente_serializer.data)
#         return Response(cliente_serializer.errors)

# class ClienteDetalleApiView(APIView):

#     def get(self, request, pk):
#         cliente = Cliente.objects.get(id = pk)
#         if cliente.estado == True:
#             cliente_serializer = ClienteSerializer(cliente)
#             return Response(cliente_serializer.data)
#         else:
#             return Response('Cliente no encontrado o eliminado')

#     def put(self, request, pk):
#         cliente = Cliente.objects.get(id = pk)
#         cliente_serializer = ClienteSerializer(cliente, data = request.data)
#         if cliente_serializer.is_valid():
#             cliente_serializer.save()
#             return Response(cliente_serializer.data)
#         return Response(cliente_serializer.errors)

    # def delete(self, request, pk):
    #     cliente = Cliente.objects.get(id = pk)
    #     cliente.estado = False
    #     cliente.save()
    #     return Response('Cliente eliminado')