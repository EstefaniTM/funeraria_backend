"""
ViewSet para Factura
"""
from rest_framework import viewsets, filters, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from ..models import Factura
from ..serializers import FacturaSerializer
from .pagination import StandardResultsSetPagination


class FacturaViewSet(viewsets.ModelViewSet):
    queryset = Factura.objects.all()
    serializer_class = FacturaSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['cliente__nombre']
    pagination_class = StandardResultsSetPagination
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def destroy(self, request, *args, **kwargs):
        """Solo administradores pueden eliminar facturas"""
        if not request.user.is_staff:
            return Response(
                {'error': 'Solo administradores pueden eliminar'},
                status=status.HTTP_403_FORBIDDEN
            )
        return super().destroy(request, *args, **kwargs)
