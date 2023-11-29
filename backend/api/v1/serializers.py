from dealers.models import DealersNames, DealersProducts
from owner.models import OwnerProducts
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
            'name_1c', 'cost',
            'recommended_price', 'category_id',
        )
