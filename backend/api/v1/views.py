from dealers.models import DealersNames, DealersProducts
from owner.models import OwnerProducts, ProductRelation
from rest_framework import viewsets

from .paginators import LimitPageNumberPagination
from .serializers import (DelearNamesSerializer, DelearProductsSerializer,
                          OwnerProductsSerializer, ProductRelationSerializer)


class DealerNamesViewSet(viewsets.ModelViewSet):
    queryset = DealersNames.objects.all()
    serializer_class = DelearNamesSerializer
    pagination_class = LimitPageNumberPagination


class DealerProductsViewSet(viewsets.ModelViewSet):
    queryset = DealersProducts.objects.all()
    serializer_class = DelearProductsSerializer
    pagination_class = LimitPageNumberPagination


class OwnerProductsViewSet(viewsets.ModelViewSet):
    queryset = OwnerProducts.objects.all()
    serializer_class = OwnerProductsSerializer


class ProductRelationViewSet(viewsets.ModelViewSet):
    queryset = ProductRelation.objects.all()
    serializer_class = ProductRelationSerializer
