from rest_framework import viewsets
from .models import Servicio
from .serializer import ServicioSerializer

class ServicioViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ServicioSerializer
    queryset = Servicio.objects.filter(estado = True)