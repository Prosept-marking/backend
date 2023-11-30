from dealers.models import DealersNames, DealersProducts
from owner.models import OwnerProducts, ProductRelation
from rest_framework import serializers


class DelearNamesSerializer(serializers.ModelSerializer):
    class Meta:
        model = DealersNames
        fields = (
            'pk', 'dealer_id', 'name',
        )


class DelearProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DealersProducts
        fields = (
            'pk', 'dealer_id',
            'product_key', 'price',
            'product_url', 'product_name',
            'date', 'matched',
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


class ProductRelationSerializer(serializers.Serializer):
    class Meta:
        model = ProductRelation
        fields = (
            'pk', 'dealer_product',
            'owner_product', 'matched',
            'date'
        )