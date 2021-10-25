from rest_framework import viewsets
from .models import Local
from .serializer import LocalSerializer

class LocalViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = LocalSerializer
    queryset = Local.objects.filter(estado = True)