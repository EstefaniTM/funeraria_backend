"""
ViewSet para Material
"""
from rest_framework import viewsets, filters, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from ..models import Material
from ..serializers import MaterialSerializer
from .pagination import StandardResultsSetPagination


class MaterialViewSet(viewsets.ModelViewSet):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['tipo', 'descripcion']
    pagination_class = StandardResultsSetPagination
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def destroy(self, request, *args, **kwargs):
        """Solo administradores pueden eliminar materiales"""
        if not request.user.is_staff:
            return Response(
                {'error': 'Solo administradores pueden eliminar'},
                status=status.HTTP_403_FORBIDDEN
            )
        return super().destroy(request, *args, **kwargs)
