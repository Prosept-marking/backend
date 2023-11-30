from dealers.models import DealersNames, DealersProducts
from django_filters.rest_framework import DjangoFilterBackend
from owner.models import OwnerProducts, ProductRelation
from rest_framework import viewsets

from .paginators import LimitPageNumberPagination
from .serializers import (DelearNamesSerializer, DelearProductsSerializer,
                          OwnerProductsSerializer, ProductRelationSerializer)


class DealerNamesViewSet(viewsets.ModelViewSet):
    queryset = DealersNames.objects.all()
    serializer_class = DelearNamesSerializer
    pagination_class = LimitPageNumberPagination
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('dealer_id', 'name')


class DealerProductsViewSet(viewsets.ModelViewSet):
    queryset = DealersProducts.objects.all()
    serializer_class = DelearProductsSerializer
    pagination_class = LimitPageNumberPagination
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = (
        'dealer_id', 'product_key',
        'price', 'product_name',
        'date', 'matched',
        'product_name'
    )


class OwnerProductsViewSet(viewsets.ModelViewSet):
    queryset = OwnerProducts.objects.all()
    serializer_class = OwnerProductsSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = (
        'owner_id', 'ean_13',
        'article', 'name',
        'name_1c', 'cost',
        'recommended_price', 'category_id',
        'ozon_name', 'wb_name',
        'ozon_article', 'wb_article',
        'ym_article', 'wb_article_td'
    )


class ProductRelationViewSet(viewsets.ModelViewSet):
    queryset = ProductRelation.objects.all()
    serializer_class = ProductRelationSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = (
        'dealer_product', 'owner_product',
        'matched', 'date'
    )
