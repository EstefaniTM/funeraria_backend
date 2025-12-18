"""
Endpoints de autenticación (login, registro)
"""
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


@api_view(['POST'])
def login(request):
    """Endpoint para obtener token de autenticación"""
    username = request.data.get('username')
    password = request.data.get('password')
    
    if not username or not password:
        return Response(
            {'error': 'Se requieren username y password'},
            status=status.HTTP_400_BAD_REQUEST
        )
    
    user = authenticate(username=username, password=password)
    
    if user is None:
        return Response(
            {'error': 'Credenciales inválidas'},
            status=status.HTTP_401_UNAUTHORIZED
        )
    
    token, created = Token.objects.get_or_create(user=user)
    return Response({
        'token': token.key,
        'usuario': user.username,
        'email': user.email
    })


@api_view(['POST'])
def registro(request):
    """Endpoint para registrar nuevo usuario"""
    try:
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email')
        
        # Validar que todos los campos estén presentes
        if not username or not password or not email:
            return Response(
                {'error': 'Se requieren username, password y email'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # Verificar que el usuario no existe
        if User.objects.filter(username=username).exists():
            return Response(
                {'error': 'El usuario ya existe'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # Verificar que el email no está registrado
        if User.objects.filter(email=email).exists():
            return Response(
                {'error': 'El email ya está registrado'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # Crear usuario
        user = User.objects.create_user(username=username, password=password, email=email)
        token, created = Token.objects.get_or_create(user=user)
        
        return Response({
            'token': token.key,
            'usuario': user.username,
            'email': user.email
        }, status=status.HTTP_201_CREATED)
    
    except Exception as e:
        return Response(
            {'error': f'Error al crear usuario: {str(e)}'},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
