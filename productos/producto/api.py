from rest_framework import viewsets
from .serializer import ProductoSerializer
from .models import Producto


class ProductoViewset(viewsets.ReadOnlyModelViewSet):
    serializer_class = ProductoSerializer
    queryset = Producto.objects.filter(estado = True)