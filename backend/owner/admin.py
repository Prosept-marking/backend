from django.contrib import admin
from .models import OwnerProducts


@admin.register(OwnerProducts)
class OwnerProductsAdmin(admin.ModelAdmin):
    list_display = (
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



