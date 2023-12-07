from django.contrib import admin

from .models import OwnerProducts, ProductRelation


@admin.register(OwnerProducts)
class OwnerProductsAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'owner_id',
        'name_1c',
        'article',
        'ean_13',
        'cost',
        'recommended_price',
        'category_id',
    )
    search_fields = ('name_1c', 'ean_13', 'article')
    list_filter = ('name_1c', 'ean_13', 'article')
    empty_value_display = '-пусто-'


@admin.register(ProductRelation)
class ProductRelationAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'dealer_product',
        'get_dealer_product_name',
        'owner_product',
        'get_owner_product_name',
        'date'
    )
    search_fields = ('date',)
    list_filter = ('date', )

    def get_dealer_product_name(self, obj):
        return obj.dealer_product.product_name

    def get_owner_product_name(self, obj):
        return obj.owner_product.name_1c
