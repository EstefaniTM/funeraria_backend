from django.contrib import admin
from .models import (
    Cliente, Servicio, Vehiculo, Material, Empleado, 
    Ubicacion, ServicioContratado, Factura
)

# Registrar modelos en el admin
admin.site.register(Cliente)
admin.site.register(Servicio)
admin.site.register(Vehiculo)
admin.site.register(Material)
admin.site.register(Empleado)
admin.site.register(Ubicacion)
admin.site.register(ServicioContratado)
admin.site.register(Factura)
