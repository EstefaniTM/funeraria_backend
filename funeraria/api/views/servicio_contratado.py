"""
ViewSet para ServicioContratado
"""
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from ..models import ServicioContratado
from ..serializers import ServicioContratadoSerializer
from .pagination import StandardResultsSetPagination


class ServicioContratadoViewSet(viewsets.ModelViewSet):
    queryset = ServicioContratado.objects.all()
    serializer_class = ServicioContratadoSerializer
    pagination_class = StandardResultsSetPagination
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def destroy(self, request, *args, **kwargs):
        """Solo administradores pueden eliminar servicios contratados"""
        if not request.user.is_staff:
            return Response(
                {'error': 'Solo administradores pueden eliminar'},
                status=status.HTTP_403_FORBIDDEN
            )
        return super().destroy(request, *args, **kwargs)
