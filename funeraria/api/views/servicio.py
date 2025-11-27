"""
ViewSet para Servicio
"""
from rest_framework import viewsets, filters, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from ..models import Servicio
from ..serializers import ServicioSerializer
from .pagination import StandardResultsSetPagination


class ServicioViewSet(viewsets.ModelViewSet):
    queryset = Servicio.objects.all()
    serializer_class = ServicioSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['nombre', 'descripcion']
    pagination_class = StandardResultsSetPagination
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def destroy(self, request, *args, **kwargs):
        """Solo administradores pueden eliminar servicios"""
        if not request.user.is_staff:
            return Response(
                {'error': 'Solo administradores pueden eliminar'},
                status=status.HTTP_403_FORBIDDEN
            )
        return super().destroy(request, *args, **kwargs)
