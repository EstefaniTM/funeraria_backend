"""
Handlers personalizados para excepciones de la API
"""
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist, ValidationError as DjangoValidationError
from rest_framework.exceptions import ValidationError as DRFValidationError


def custom_exception_handler(exc, context):
    """
    Handler personalizado de excepciones que devuelve respuestas consistentes
    """
    response = None
    
    if isinstance(exc, DRFValidationError):
        response = Response(
            {
                'error': 'Datos inválidos',
                'detalles': exc.detail if hasattr(exc, 'detail') else str(exc)
            },
            status=status.HTTP_400_BAD_REQUEST
        )
    
    # Manejar excepciones de validación de Django
    elif isinstance(exc, DjangoValidationError):
        response = Response(
            {
                'error': 'Validación fallida',
                'detalles': str(exc)
            },
            status=status.HTTP_400_BAD_REQUEST
        )
    
    # Manejar objetos no encontrados
    elif isinstance(exc, ObjectDoesNotExist):
        response = Response(
            {
                'error': 'Recurso no encontrado',
                'detalles': 'El objeto solicitado no existe'
            },
            status=status.HTTP_404_NOT_FOUND
        )
    
    # Manejar otras excepciones
    else:
        response = Response(
            {
                'error': 'Error interno del servidor',
                'detalles': str(exc) if str(exc) else 'Error desconocido'
            },
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
    
    return response
