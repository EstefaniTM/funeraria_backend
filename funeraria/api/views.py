from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from .models import (
    Cliente, Servicio, Vehiculo, Material, Empleado, 
    Ubicacion, ServicioContratado, Factura
)
from .serializers import (
    ClienteSerializer, ServicioSerializer, VehiculoSerializer, 
    MaterialSerializer, EmpleadoSerializer, UbicacionSerializer,
    ServicioContratadoSerializer, FacturaSerializer
)


# Autenticación
@api_view(['POST'])
def login(request):
    """Endpoint para obtener token de autenticación"""
    username = request.data.get('username')
    password = request.data.get('password')
    
    user = authenticate(username=username, password=password)
    
    if user is None:
        return Response({'error': 'Credenciales inválidas'}, status=status.HTTP_401_UNAUTHORIZED)
    
    token, created = Token.objects.get_or_create(user=user)
    return Response({'token': token.key, 'usuario': user.username})


@api_view(['POST'])
def registro(request):
    """Endpoint para registrar nuevo usuario"""
    username = request.data.get('username')
    password = request.data.get('password')
    email = request.data.get('email')
    
    if User.objects.filter(username=username).exists():
        return Response({'error': 'El usuario ya existe'}, status=status.HTTP_400_BAD_REQUEST)
    
    user = User.objects.create_user(username=username, password=password, email=email)
    token, created = Token.objects.get_or_create(user=user)
    
    return Response({'token': token.key, 'usuario': user.username}, status=status.HTTP_201_CREATED)


# ViewSets para CRUD automático
class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    search_fields = ['nombre', 'apellido']
    ordering_fields = ['fecha_funeral']
    permission_classes = [AllowAny]
    
    def create(self, request, *args, **kwargs):
        """Override para generar token al crear cliente"""
        # Crear el cliente normalmente
        response = super().create(request, *args, **kwargs)
        
        # Generar usuario y token automáticamente
        if response.status_code == 201:
            cliente_id = response.data.get('id')
            nombre = response.data.get('nombre', '').lower()
            apellido = response.data.get('apellido', '').lower()
            
            # Crear nombre de usuario único basado en cliente
            username = f"cliente_{cliente_id}"
            email = f"cliente{cliente_id}@funeraria.local"
            password = f"cliente_{cliente_id}_temp"
            
            try:
                # Crear usuario
                user = User.objects.create_user(
                    username=username,
                    email=email,
                    password=password
                )
                # Generar token
                token, created = Token.objects.get_or_create(user=user)
                
                # Agregar token a la respuesta
                response.data['token'] = token.key
                response.data['usuario'] = username
                response.data['contraseña_temporal'] = password
            except Exception as e:
                # Si hay error creando usuario, igualmente devuelve el cliente
                pass
        
        return response


class ServicioViewSet(viewsets.ModelViewSet):
    queryset = Servicio.objects.all()
    serializer_class = ServicioSerializer
    search_fields = ['nombre']
    permission_classes = [IsAuthenticatedOrReadOnly]


class VehiculoViewSet(viewsets.ModelViewSet):
    queryset = Vehiculo.objects.all()
    serializer_class = VehiculoSerializer
    search_fields = ['placa', 'modelo']
    permission_classes = [IsAuthenticatedOrReadOnly]


class MaterialViewSet(viewsets.ModelViewSet):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer
    search_fields = ['tipo']
    permission_classes = [IsAuthenticatedOrReadOnly]


class EmpleadoViewSet(viewsets.ModelViewSet):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer
    search_fields = ['nombre', 'cargo']
    permission_classes = [IsAuthenticatedOrReadOnly]


class UbicacionViewSet(viewsets.ModelViewSet):
    queryset = Ubicacion.objects.all()
    serializer_class = UbicacionSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class ServicioContratadoViewSet(viewsets.ModelViewSet):
    queryset = ServicioContratado.objects.all()
    serializer_class = ServicioContratadoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class FacturaViewSet(viewsets.ModelViewSet):
    queryset = Factura.objects.all()
    serializer_class = FacturaSerializer
    search_fields = ['cliente__nombre']
    permission_classes = [IsAuthenticatedOrReadOnly]

