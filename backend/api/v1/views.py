from datetime import timedelta

from dealers.models import DealersNames, DealersProducts
from django.utils import timezone
from django_filters.rest_framework import DjangoFilterBackend
from owner.models import OwnerProducts, ProductRelation
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from statistic.models import ComparisonSallers, DailyStatistics

from .paginators import LimitPageNumberPagination
from .serializers import (ComparisonSallersSerializer,
                          DailyStatisticsSerializer, DealerNamesSerializer,
                          DelearProductsSerializer, OwnerProductsSerializer,
                          ProductRelationCreateSerializer,
                          ProductRelationSerializer)
from .utils.product_matching import matching


class BaseProductViewSet(viewsets.ModelViewSet):
    pagination_class = LimitPageNumberPagination
    filter_backends = (DjangoFilterBackend,)


class DealerNamesViewSet(BaseProductViewSet):
    queryset = DealersNames.objects.all()
    serializer_class = DealerNamesSerializer
    filterset_fields = ('dealer_id', 'name')


class DealerProductsViewSet(BaseProductViewSet):
    queryset = DealersProducts.objects.all().order_by('id')
    serializer_class = DelearProductsSerializer
    filterset_fields = (
        'dealer_id', 'product_key',
        'price', 'product_name', 'pk_owner_product',
        'name_1c_owner',
        'date', 'matched', 'real_date',
        'product_name', 'postponed',
        'combined_status'
    )

    def get_queryset(self):
        queryset = super().get_queryset()
        days = self.request.query_params.get('days')
        if days and days.isdigit():
            days_count = int(days)
            end_date = timezone.now().date()
            start_date = end_date - timedelta(days=days_count)
            queryset = queryset.filter(real_date__range=(start_date, end_date))
        return queryset

    @action(detail=True, methods=['PATCH'])
    def set_postponed(self, request, pk=None):
        dealer_product = self.get_object()
        if dealer_product.matched:
            dealer_product.matched = False
        dealer_product.postponed = True
        dealer_product.save()
        return Response({'postponed': True})

    @action(detail=True, methods=['PATCH'])
    def set_unprocessed(self, request, pk=None):
        dealer_product = self.get_object()
        dealer_product.postponed = False
        dealer_product.matched = False
        dealer_product.save()
        return Response({'postponed': False})


class OwnerProductsViewSet(BaseProductViewSet):
    queryset = OwnerProducts.objects.all().order_by('id')
    serializer_class = OwnerProductsSerializer
    filterset_fields = (
        'pk',
        'owner_id', 'ean_13',
        'article', 'name',
        'name_1c', 'cost',
        'recommended_price', 'category_id',
        'ozon_name', 'wb_name',
        'ozon_article', 'wb_article',
        'ym_article', 'wb_article_td'
    )

    @action(detail=False, methods=['GET'],
            url_path=r'match_product/(?P<dealer_product_id>\d+)')  # noqa: W605
    def match_product(self, request, dealer_product_id=None):
        if dealer_product_id:
            dealer_product = DealersProducts.objects.get(id=dealer_product_id)
            name = dealer_product.product_name
            matched_products = matching(name)
            products = OwnerProducts.objects.filter(
                name_1c__in=matched_products).values()
            serializer = OwnerProductsSerializer(products, many=True)
            return Response(serializer.data)
        else:
            return Response('No id')


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


class DailyStatisticsViewSet(BaseProductViewSet):
    queryset = DailyStatistics.objects.all()
    serializer_class = DailyStatisticsSerializer
    filterset_fields = (
        'date',
        'daily_unverified_product',
        'unverified_product',
        'verified_product',
        'rejected_product',
    )


class ComparisonSallersViewSet(BaseProductViewSet):
    queryset = ComparisonSallers.objects.all()
    serializer_class = ComparisonSallersSerializer
    filterset_fields = (
        'saller_name',
        'verified_product',
        'unverified_product',
        'all_product',
    )
