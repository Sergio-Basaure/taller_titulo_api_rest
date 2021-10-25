from rest_framework.routers import DefaultRouter
from django.urls import path
from .local.api import LocalViewSet
from .reclamo.api import ReclamosApiViewSets

router = DefaultRouter()
router.register(r'', LocalViewSet, basename = 'local'),
router.register(r'reclamos', ReclamosApiViewSets, basename = 'reclamos')

# urlpatterns = [
#     path('', LocalApiView.as_view(), name = 'local'),
#     path('<int:pk>/', LocalDetalleApiView.as_view(), name = 'detalle_local'),
#     path('reclamos/', ReclamosApiView.as_view(), name = 'reclamos'),
#     path('reclamos/<int:pk>/', ReclamoDetalleApiview.as_view(), name = 'detalle_reclamo'),
# ]

urlpatterns = router.urls