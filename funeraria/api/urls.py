from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'clientes', views.ClienteViewSet, basename='cliente')
router.register(r'servicios', views.ServicioViewSet, basename='servicio')
router.register(r'vehiculos', views.VehiculoViewSet, basename='vehiculo')
router.register(r'materiales', views.MaterialViewSet, basename='material')
router.register(r'empleados', views.EmpleadoViewSet, basename='empleado')
router.register(r'ubicaciones', views.UbicacionViewSet, basename='ubicacion')
router.register(r'servicios-contratados', views.ServicioContratadoViewSet, basename='servicio-contratado')
router.register(r'facturas', views.FacturaViewSet, basename='factura')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/login/', views.login, name='login'),
    path('auth/registro/', views.registro, name='registro'),
]
