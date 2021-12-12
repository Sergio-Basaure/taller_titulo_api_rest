from rest_framework import viewsets
from .serializer import CategoriaProductoSerializer
from .models import CategoriaProducto


class CategoriaProductoViewset(viewsets.ReadOnlyModelViewSet):
    serializer_class = CategoriaProductoSerializer
    queryset = CategoriaProducto.objects.filter(estado = True)