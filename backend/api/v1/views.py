from dealers.models import DealersNames, DealersProducts
from django_filters.rest_framework import DjangoFilterBackend
from owner.models import OwnerProducts, ProductRelation
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .paginators import LimitPageNumberPagination
from .serializers import (DealerNamesSerializer, DelearProductsSerializer,
                          OwnerProductsSerializer,
                          ProductRelationCreateSerializer,
                          ProductRelationSerializer)
from .utils.product_matching import matching


class BaseProductViewSet(viewsets.ModelViewSet):
    pagination_class = LimitPageNumberPagination
    filter_backends = (DjangoFilterBackend,)

    def match_product(self, request, dealer_product_id=None):
        if dealer_product_id:
            dealer_product = self.queryset.get(id=dealer_product_id)
            name = dealer_product.product_name
            matched_products = matching(name)
            products = OwnerProducts.objects.filter(
                name_1c__in=matched_products).values()
            serializer = OwnerProductsSerializer(products, many=True)
            return Response(serializer.data)
        else:
            return Response('No id')


class DealerNamesViewSet(BaseProductViewSet):
    queryset = DealersNames.objects.all()
    serializer_class = DealerNamesSerializer
    filterset_fields = ('dealer_id', 'name')


class DealerProductsViewSet(BaseProductViewSet):
    queryset = DealersProducts.objects.all().order_by('id')
    serializer_class = DelearProductsSerializer
    filterset_fields = (
        'dealer_id', 'product_key',
        'price', 'product_name',
        'date', 'matched',
        'product_name', 'postponed'
    )

    @action(detail=True, methods=['PATCH'])
    def set_postponed(self, request, pk=None):
        dealer_product = self.get_object()
        dealer_product.postponed = True
        dealer_product.matched = False
        dealer_product.save()
        return Response({'postponed': True})


class OwnerProductsViewSet(BaseProductViewSet):
    queryset = OwnerProducts.objects.all()
    serializer_class = OwnerProductsSerializer
    filterset_fields = (
        'owner_id', 'ean_13',
        'article', 'name',
        'name_1c', 'cost',
        'recommended_price', 'category_id',
        'ozon_name', 'wb_name',
        'ozon_article', 'wb_article',
        'ym_article', 'wb_article_td'
    )


class ProductRelationViewSet(BaseProductViewSet):
    queryset = ProductRelation.objects.all()
    serializer_class = ProductRelationSerializer
    filterset_fields = (
        'dealer_product', 'owner_product',
        'date'
    )

    def get_serializer_class(self):
        if self.action == 'create':
            return ProductRelationCreateSerializer
        return ProductRelationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        dealer_product_id = request.data.get('dealer_product')
        if dealer_product_id:
            dealer_product = DealersProducts.objects.filter(
                pk=dealer_product_id).first()
            if dealer_product:
                dealer_product.matched = True
                dealer_product.postponed = False
                dealer_product.save()
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED,
                        headers=headers)
