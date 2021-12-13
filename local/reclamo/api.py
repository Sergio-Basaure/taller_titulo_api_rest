from rest_framework import viewsets
# from rest_framework.permissions import IsAuthenticated
from .serializer import ReclamoSerializer
from .models import Reclamos

class ReclamosApiViewSets(viewsets.ModelViewSet):
    serializer_class = ReclamoSerializer
    queryset = Reclamos.objects.filter(estado = True)
    # permission_classes = (IsAuthenticated,)
    # def get_queryset(self,pk = None):
    #     if pk == None:
    #         return self.get_serializer().Meta.model.objects.filter(estado = True)
    #     return self.get_serializer().Meta.model.objects.filter(id = pk, estado = True).first()

# class ReclamoCliente(viewsets.GenericViewSet):
