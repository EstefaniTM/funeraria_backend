"""
ViewSet para Cliente
"""
from rest_framework import viewsets, filters, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.exceptions import ValidationError
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

from ..models import Cliente
from ..serializers import ClienteSerializer
from .pagination import StandardResultsSetPagination


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['nombre', 'apellido']
    pagination_class = StandardResultsSetPagination
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def create(self, request, *args, **kwargs):
        """Override para opcionalmente generar credenciales al crear cliente"""
        try:
            # Crear el cliente normalmente
            response = super().create(request, *args, **kwargs)
            
            # Si se solicitan credenciales
            if response.status_code == 201 and request.data.get('create_credentials'):
                cliente_id = response.data.get('id')
                email = request.data.get('email') or f"cliente{cliente_id}@funeraria.local"
                username = request.data.get('username') or f"cliente_{cliente_id}"
                password = request.data.get('password') or f"cliente_{cliente_id}_temp"
                
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
                    response.data['email'] = email
                except Exception as e:
                    response.data['warning'] = f"Usuario no creado: {str(e)}"
            
            return response
        except ValidationError as e:
            return Response(
                {'error': 'Datos inválidos', 'detalles': e.detail},
                status=status.HTTP_400_BAD_REQUEST
            )
        except Exception as e:
            return Response(
                {'error': 'Error al crear cliente', 'detalles': str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    
    def destroy(self, request, *args, **kwargs):
        """Solo administradores pueden eliminar clientes"""
        if not request.user.is_staff:
            return Response(
                {'error': 'Solo administradores pueden eliminar'},
                status=status.HTTP_403_FORBIDDEN
            )
        return super().destroy(request, *args, **kwargs)
