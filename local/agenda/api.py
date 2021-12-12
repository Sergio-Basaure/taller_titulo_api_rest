from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from .models import Agenda, Hora
from .serializer import AgendaSerializer, HoraSerializer


class AgendaViewsets(viewsets.ModelViewSet):
    serializer_class = AgendaSerializer
    queryset = Agenda.objects.all()

class HoraViewsets(viewsets.ReadOnlyModelViewSet):
    serializer_class = HoraSerializer
    queryset = Hora.objects.all()

class AgendaGenericViewSet(viewsets.GenericViewSet):
    serializer_class = AgendaSerializer
    queryset = Agenda.objects.all()
    permission_classes = (IsAuthenticated,)

    def create(self, request):
        agenda_serializer = AgendaSerializer(data = request.data)
        if agenda_serializer.is_valid():
            agenda_serializer.save()
            return Response(agenda_serializer.data, status = status.HTTP_201_CREATED)
        return Response(agenda_serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk = None):
        queryset = Agenda.objects.all()
        agenda = get_object_or_404(queryset, pk = pk)
        agenda_serializer = AgendaSerializer(agenda, data = request.data)
        if agenda_serializer.is_valid():
            agenda_serializer.save()
            return Response({
                'mensaje' : 'Agenda actualizada correctamente'
            }, status = status.HTTP_200_OK)
        return Response({
            'mensaje' : 'Error al actualizar agenda',
            'errors' : agenda_serializer.errors
        }, status = status.HTTP_400_BAD_REQUEST)


    def list(self, request):
        queryset = Agenda.objects.all()
        agenda_serializer = AgendaSerializer(queryset, many = True)
        return Response(agenda_serializer.data, status = status.HTTP_200_OK)

    def retrieve(self, request, pk = None):
        queryset = Agenda.objects.all()
        agenda = get_object_or_404(queryset, pk = pk)
        if agenda.estado == True:
            agenda_serialize = AgendaSerializer(agenda)
            return Response(agenda_serialize.data, status = status.HTTP_200_OK)
        else:
            return Response({'mensaje' : 'Reserva no disponible'})

    def destroy(self, request, pk = None):
        queryset = Agenda.objects.all()
        agenda = get_object_or_404(queryset, pk = pk)
        if agenda.estado == True:
            agenda.estado = False
            agenda.save()
            return Response({
                'mensaje' : 'Bienvenido!!!'
            }, status = status.HTTP_200_OK)
        return Response({
            'mensaje' : 'Agenda no encontrada o no disponible'
        }, status = status.HTTP_400_BAD_REQUEST)

