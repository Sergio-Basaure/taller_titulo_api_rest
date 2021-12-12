from rest_framework import viewsets
from .models import TipoReclamo
from .serializer import TipoReclamoSerializer

class TipoReclamoViewsets(viewsets.ReadOnlyModelViewSet):
    serializer_class = TipoReclamoSerializer
    queryset = TipoReclamo.objects.all()