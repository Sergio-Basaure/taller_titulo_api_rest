import rest_framework


from rest_framework import viewsets
from .serializer import ReclamoSerializer

class ReclamosApiViewSets(viewsets.ModelViewSet):
    serializer_class = ReclamoSerializer

    def get_queryset(self,pk = None):
        if pk == None:
            return self.get_serializer().Meta.model.objects.filter(estado = True)
        return self.get_serializer().Meta.model.objects.filter(id = pk, estado = True).first()
