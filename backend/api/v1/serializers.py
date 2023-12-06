from dealers.models import DealersNames, DealersProducts
from owner.models import OwnerProducts, ProductRelation
from rest_framework import serializers
from statistic.models import ComparisonSallers, DailyStatistics


class DailyStatisticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyStatistics
        fields = (
            'date',
            'daily_unverified_product',
            'unverified_product',
            'verified_product',
            'rejected_product',
        )


class ComparisonSallersSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComparisonSallers
        fields = (
            'saller_name',
            'verified_product',
            'unverified_product',
            'all_product',
        )


class DealerNamesSerializer(serializers.ModelSerializer):
    class Meta:
        model = DealersNames
        fields = (
            'pk',
            'dealer_id',
            'name',
        )


class DelearProductsSerializer(serializers.ModelSerializer):
    dealer_name = serializers.StringRelatedField(source='dealer_id.name',
                                                 read_only=True)

    class Meta:
        model = DealersProducts
        fields = (
            'pk', 'dealer_name', 'combined_status',
            'product_key', 'price',
            'product_url', 'product_name', 'pk_owner_product',
            'name_1c_owner',
            'date', 'matched', 'postponed', 'real_date'
        )


class OwnerProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OwnerProducts
        fields = (
            'pk', 'owner_id',
            'article', 'ean_13',
            'name', 'name_1c',
            'cost', 'recommended_price',
            'category_id', 'ozon_name',
            'wb_name', 'ozon_article',
            'wb_article', 'ym_article',
            'wb_article_td'
        )


class ProductRelationSerializer(serializers.ModelSerializer):
    dealer_product = DelearProductsSerializer(read_only=True)
    owner_product = OwnerProductsSerializer(read_only=True)

    class Meta:
        model = ProductRelation
        fields = (
            'pk', 'dealer_product',
            'owner_product',
            'date'
        )


class ProductRelationCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductRelation
        fields = (
            'dealer_product',
            'owner_product',
            'date'
        )
