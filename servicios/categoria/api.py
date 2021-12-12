from rest_framework import viewsets
from .serializer import CategoriaServicioSerializer
from .models import CategoriaServicio


class CategoriaServiciosViewset(viewsets.ReadOnlyModelViewSet):
    serializer_class = CategoriaServicioSerializer
    queryset = CategoriaServicio.objects.filter(estado = True)