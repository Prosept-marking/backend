from django.contrib import admin

from .models import DealersNames, DealersProducts


@admin.register(DealersNames)
class DealersNamesAdmin(admin.ModelAdmin):
    list_display = ('dealer_id', 'name',)


admin.site.register(DealersProducts)
