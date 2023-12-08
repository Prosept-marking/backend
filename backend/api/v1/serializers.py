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


class DealerNamesSerializer(serializers.ModelSerializer):
    class Meta:
        model = DealersNames
        fields = (
            'pk',
            'dealer_id',
            'name',
        )


class ComparisonSallersSerializer(serializers.ModelSerializer):
    saller_name = serializers.SerializerMethodField()

    def get_saller_name(self, obj):
        return obj.saller_name.name

    class Meta:
        model = ComparisonSallers
        fields = (
            'saller_name',
            'verified_product',
            'unverified_product',
            'rejected_product',
            'all_product',
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

    def validate(self, data):
        required_fields = ['dealer_name', 'product_name', 'product_key']
        for field in required_fields:
            if not data.get(field):
                raise serializers.ValidationError(f'{field} is required')
        return data


class OwnerProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OwnerProducts
        fields = (
            'id',
            'article', 'ean_13',
            'name', 'name_1c',
            'cost', 'recommended_price',
            'category_id', 'ozon_name',
            'wb_name', 'ozon_article',
            'wb_article', 'ym_article',
            'wb_article_td'
        )

    def validate(self, data):
        required_fields = ['article', 'ean_13', 'name_1c']
        for field in required_fields:
            if not data.get(field):
                raise serializers.ValidationError(f'{field} is required')
        return data


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
