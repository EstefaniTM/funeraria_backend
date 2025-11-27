"""
ViewSet para Ubicación
"""
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from ..models import Ubicacion
from ..serializers import UbicacionSerializer
from .pagination import StandardResultsSetPagination


class UbicacionViewSet(viewsets.ModelViewSet):
    queryset = Ubicacion.objects.all()
    serializer_class = UbicacionSerializer
    pagination_class = StandardResultsSetPagination
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def destroy(self, request, *args, **kwargs):
        """Solo administradores pueden eliminar ubicaciones"""
        if not request.user.is_staff:
            return Response(
                {'error': 'Solo administradores pueden eliminar'},
                status=status.HTTP_403_FORBIDDEN
            )
        return super().destroy(request, *args, **kwargs)
