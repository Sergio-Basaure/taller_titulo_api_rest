from rest_framework import routers
from rest_framework.routers import DefaultRouter
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from local.local.api import LocalViewSet
from local.reclamo.api import ReclamosApiViewSets
from productos.producto.api import ProductoViewset
from servicios.servicio.api import ServicioViewSet
from cliente.api import ClienteViewSet
from cliente.login.login import LoginApi, Logout, Registro
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

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
router.register(r'api/producto', ProductoViewset, basename='productos')
router.register(r'api/servicio', ServicioViewSet, basename = 'servicio')
router.register(r'api/cliente', ClienteViewSet, basename = 'cliente')

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

urlpatterns += router.urls