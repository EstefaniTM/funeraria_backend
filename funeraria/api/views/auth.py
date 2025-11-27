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
    username = request.data.get('username')
    password = request.data.get('password')
    email = request.data.get('email')
    
    if User.objects.filter(username=username).exists():
        return Response({'error': 'El usuario ya existe'}, status=status.HTTP_400_BAD_REQUEST)
    
    user = User.objects.create_user(username=username, password=password, email=email)
    token, created = Token.objects.get_or_create(user=user)
    
    return Response({'token': token.key, 'usuario': user.username}, status=status.HTTP_201_CREATED)
