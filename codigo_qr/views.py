from rest_framework import viewsets
from .serializer import QrAgendaSerializer
from .models import QrAgenda
from local.agenda.models import Agenda

class QrAgendaViewSet(viewsets.GenericViewSet):
    serializer_class = QrAgendaSerializer
    queryset = None
    def update(self, request, pk = None):
        queryset = Agenda.objects.filter().first