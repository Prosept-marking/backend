from django.contrib import admin

from .models import DealersNames, DealersProducts


@admin.register(DealersNames)
class DealersNamesAdmin(admin.ModelAdmin):
    list_display = ('pk', 'dealer_id', 'name',)


@admin.register(DealersProducts)
class DealersProductsAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'dealer_id',
        'product_key',
        'price',
        'product_url',
        'product_name',
        'date',
        'real_date',
        'matched',
    )
    search_fields = ('product_key', 'product_name', 'real_date', 'matched')
    list_filter = ('product_key', 'product_name', 'real_date', 'matched')
    empty_value_display = '-пусто-'
