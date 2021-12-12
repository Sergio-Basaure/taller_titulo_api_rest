from rest_framework.routers import DefaultRouter
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from local.local.api import LocalViewSet
from local.reclamo.api import ReclamosApiViewSets
from local.categoria.api import TipoReclamoViewsets
from local.agenda.api import AgendaViewsets, HoraViewsets, AgendaGenericViewSet
from productos.producto.api import ProductoViewset
from productos.categoria.api import CategoriaProductoViewset
from servicios.servicio.api import ServicioViewSet
from servicios.categoria.api import CategoriaServiciosViewset
from cliente.api import ClienteViewSet
from codigo_qr.views import QrAgendaViewSet
from cliente.login.login import LoginApi, Logout, Registro
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf import settings
from django.views.static import serve

schema_view = get_schema_view(
   openapi.Info(
      title="Documentacion API CCS",
      default_version='v0.1',
      description="Doocumentcion publica de API CCS (Taller de titulacion)",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="ccs@ccs.cl"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

router = DefaultRouter()
router.register(r'api/local', LocalViewSet, basename = 'local'),
router.register(r'api/reclamos', ReclamosApiViewSets, basename = 'reclamos')
router.register(r'api/categoria_reclamo', TipoReclamoViewsets, basename = 'categoria_reclamo')
router.register(r'api/producto', ProductoViewset, basename = 'productos')
router.register(r'api/categoria_producto', CategoriaProductoViewset, basename = 'categoria_producto')
router.register(r'api/servicio', ServicioViewSet, basename = 'servicio')
router.register(r'api/categoria_servicio', CategoriaServiciosViewset, basename = 'categoria_servicio')
router.register(r'api/cliente', ClienteViewSet, basename = 'cliente')
router.register(r'api/agenda', AgendaGenericViewSet, basename = 'agenda')
router.register(r'api/hora', HoraViewsets, basename = 'hora')
router.register(r'api/qr', QrAgendaViewSet, basename = 'qr')

urlpatterns = [

   re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),


    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/login/', LoginApi.as_view(), name = 'login'),
    path('api/logout/', Logout.as_view(), name = 'logout'),
    path('api/registro/', Registro.as_view(), name = 'registro')

]
if settings.DEBUG:
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]

urlpatterns += router.urls