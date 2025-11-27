"""
Views para la API Funeraria
Expone todos los ViewSets y endpoints
"""
from .auth import login, registro
from .cliente import ClienteViewSet
from .servicio import ServicioViewSet
from .vehiculo import VehiculoViewSet
from .material import MaterialViewSet
from .empleado import EmpleadoViewSet
from .ubicacion import UbicacionViewSet
from .servicio_contratado import ServicioContratadoViewSet
from .factura import FacturaViewSet
from .pagination import StandardResultsSetPagination

__all__ = [
    'login',
    'registro',
    'ClienteViewSet',
    'ServicioViewSet',
    'VehiculoViewSet',
    'MaterialViewSet',
    'EmpleadoViewSet',
    'UbicacionViewSet',
    'ServicioContratadoViewSet',
    'FacturaViewSet',
    'StandardResultsSetPagination',
]
