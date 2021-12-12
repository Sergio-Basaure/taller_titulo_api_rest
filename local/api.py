# from rest_framework import status, viewsets
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from .models import Local
# from ..local.reclamo.models import Reclamos
# from .serializers import LocalSerializer
# from ..local.reclamo.serializer import ReclamoSerializer


# class LocalViewSet(viewsets.ReadOnlyModelViewSet):
#     # permission_classes = (IsAuthenticated,) # para bloquear solo la clases por token
#     serializer_class = LocalSerializer
#     queryset = Local.objects.filter(estado = True)


# class ReclamosApiViewSets(viewsets.ModelViewSet):
#     serializer_class = ReclamoSerializer

#     def get_queryset(self,pk = None):
#         if pk == None:
#             return Reclamos.objects.filter(estado = True)
#         return Reclamos.objects.filter(id = pk, estado = True)
#         #     return self.get_serializer().Meta.model.objects.filter(estado = True)
#         # return self.get_serializer().Meta.model.objects.filter(id = pk, estado = True).first()


"""
viewset metodos:
    create = post
    update = update
    delete = delete
    list = vendria siendo como el index algo asi

"""

    # def get_queryset(self):
    #     local = Local.objects.filter(estado = True)
    #     return local





# class LocalApiView(APIView):

#     def get(self, request):
#         locales = Local.objects.filter(estado = True)
#         locales_serializer = LocalSerializer(locales, many = True)
#         return Response(locales_serializer.data, status = status.HTTP_200_OK)

# class LocalDetalleApiView(APIView):

#     def get(self, request, pk):
#         local = Local.objects.get(id = pk)
#         local_serializer = LocalSerializer(local)
#         return Response(local_serializer.data, status = status.HTTP_200_OK)


# class ReclamosApiView(APIView):

#     def get(self, request):
#         reclamos = Reclamos.objects.filter(estado = True)
#         reclamos_serializer = ReclamoSerializer(reclamos, many = True)
#         return Response(reclamos_serializer.data, status = status.HTTP_200_OK)

#     def post(self, request):
#         reclamo_serializer = ReclamoSerializer(data = request.data)
#         if reclamo_serializer.is_valid():
#             reclamo_serializer.save()
#             return Response(ReclamoSerializer.data, status = status.HTTP_201_CREATED)
#         return Response(reclamo_serializer.errors)

# class ReclamoDetalleApiview(APIView):

#     def get(self, request, pk):
#         reclamo = Reclamos.objects.get(id = pk)
#         reclamo_serializer = ReclamoSerializer(reclamo)
#         return Response(reclamo_serializer.data, status = status.HTTP_200_OK)