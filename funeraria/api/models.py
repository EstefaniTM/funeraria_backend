from django.db import models


class Cliente(models.Model):
    """Clientes de la funeraria"""
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_funeral = models.DateField()
    habitacion = models.CharField(max_length=50, blank=True)
    velatorio = models.CharField(max_length=100, blank=True)
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Servicio(models.Model):
    """Servicios disponibles"""
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.TextField(blank=True)
    
    def __str__(self):
        return self.nombre


class Vehiculo(models.Model):
    """Vehículos de la funeraria"""
    placa = models.CharField(max_length=10, unique=True)
    modelo = models.CharField(max_length=50)
    capacidad = models.IntegerField()
    
    def __str__(self):
        return f"{self.modelo} - {self.placa}"


class Material(models.Model):
    """Inventario de materiales"""
    tipo = models.CharField(max_length=50)
    cantidad = models.IntegerField()
    descripcion = models.TextField(blank=True)
    
    def __str__(self):
        return f"{self.tipo} - {self.cantidad}"


class Empleado(models.Model):
    """Empleados de la funeraria"""
    nombre = models.CharField(max_length=100)
    cargo = models.CharField(max_length=50)
    telefono = models.CharField(max_length=15, blank=True)
    
    def __str__(self):
        return self.nombre


class Ubicacion(models.Model):
    """Ubicación del servicio"""
    cliente = models.OneToOneField(Cliente, on_delete=models.CASCADE)
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.SET_NULL, null=True, blank=True)
    direccion = models.CharField(max_length=200)
    
    def __str__(self):
        return f"Ubicación - {self.cliente.nombre}"


class ServicioContratado(models.Model):
    """Servicios contratados por clientes"""
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    fecha_contratacion = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.cliente.nombre} - {self.servicio.nombre}"


class Factura(models.Model):
    """Facturas de servicios"""
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_emision = models.DateField(auto_now_add=True)
    estado = models.CharField(max_length=20, default='pendiente')
    
    def __str__(self):
        return f"Factura {self.id} - {self.cliente.nombre}"
