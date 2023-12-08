from datetime import date, timedelta

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
            queryset = queryset.filter(date__range=(start_date, end_date))
        return queryset

    @action(detail=True, methods=['PATCH'])
    def set_postponed(self, request, pk=None):
        dealer_product = self.get_object()
        if dealer_product.matched:
            dealer_product.matched = False
        dealer_product.postponed = True
        dealer_product.pk_owner_product = None
        dealer_product.name_1c_owner = None
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

    @action(detail=False, methods=['DELETE'],
            url_path='delete-product-relation-by-dealer-product/('
                     '?P<dealer_product_id>[^/.]+)')
    def delete_product_relation_by_dealer_product(self, request,
                                                  dealer_product_id=None):
        product_relations = ProductRelation.objects.filter(
            dealer_product=dealer_product_id)
        if product_relations.exists():
            product_relations.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({'error': 'Связь товаров не найдена.'},
                            status=status.HTTP_404_NOT_FOUND)


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

    def get_queryset(self):
        update_daily_statistics()
        return DailyStatistics.objects.all()

    def create(self, request, *args, **kwargs):
        return Response(
            {'error': 'Создание статистики через метод POST запрещено.'},
            status=status.HTTP_405_METHOD_NOT_ALLOWED
        )


def update_daily_statistics():
    today = date.today()
    daily_stats_today, created = DailyStatistics.objects.get_or_create(
        date=today)
    if created:
        previous_stats = DailyStatistics.objects.filter(
            date__lt=today).order_by('-date').first()
        daily_stats_today.unverified_product = DealersProducts.objects.filter(
            combined_status='unprocessed').count()
        daily_unverified_product = previous_stats.unverified_product if \
            previous_stats else daily_stats_today.unverified_product
        daily_stats_today.daily_unverified_product = daily_unverified_product
        daily_stats_today.unverified_product = daily_unverified_product
    daily_stats_today.verified_product = DealersProducts.objects.filter(
        combined_status='matched').count()
    daily_stats_today.rejected_product = DealersProducts.objects.filter(
        combined_status='postponed').count()
    daily_stats_today.unverified_product = DealersProducts.objects.filter(
        combined_status='unprocessed').count()
    daily_stats_today.save()


class ComparisonSallersViewSet(BaseProductViewSet):
    queryset = ComparisonSallers.objects.all()
    serializer_class = ComparisonSallersSerializer
    filterset_fields = (
        'saller_name',
        'verified_product',
        'unverified_product',
        'rejected_product',
        'all_product',
    )

    def get_queryset(self):
        update_dealers_statistics()
        return ComparisonSallers.objects.all()

    def create(self, request, *args, **kwargs):
        return Response(
            {'error': 'Создание объектов через метод POST запрещено.'},
            status=status.HTTP_405_METHOD_NOT_ALLOWED
        )


def update_dealers_statistics():
    dealers = DealersNames.objects.all()
    for dealer in dealers:
        matched_count = DealersProducts.objects.filter(
            dealer_id=dealer,
            matched=True
        ).count()
        postponed_count = DealersProducts.objects.filter(
            dealer_id=dealer,
            postponed=True
        ).count()
        unprocessed_count = DealersProducts.objects.filter(
            dealer_id=dealer,
            matched=False,
            postponed=False
        ).count()
        daily_stats, created = ComparisonSallers.objects.get_or_create(
            saller_name=dealer,
        )
        all_products = matched_count + postponed_count + unprocessed_count
        daily_stats.verified_product = matched_count
        daily_stats.rejected_product = postponed_count
        daily_stats.unverified_product = unprocessed_count
        daily_stats.all_product = all_products
        daily_stats.save()
