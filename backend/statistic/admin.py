from django.contrib import admin

from .models import ComparisonSallers, DailyStatistics


@admin.register(DailyStatistics)
class DailyStatisticsAdmin(admin.ModelAdmin):
    list_display = (
        'date',
        'daily_unverified_product',
        'unverified_product',
        'verified_product',
        'rejected_product',
    )
    search_fields = (
        'date',
        'daily_unverified_product',
        'unverified_product',
        'verified_product',
        'rejected_product',
    )
    list_filter = (
        'date',
        'daily_unverified_product',
        'unverified_product',
        'verified_product',
        'rejected_product',
    )
    empty_value_display = '-пусто-'


@admin.register(ComparisonSallers)
class ComparisonSallersAdmin(admin.ModelAdmin):
    list_display = (
        'saller_name',
        'verified_product',
        'unverified_product',
        'rejected_product',
        'all_product',
    )
    search_fields = (
        'saller_name',
        'verified_product',
        'unverified_product',
    )
    list_filter = (
        'saller_name',
        'verified_product',
        'unverified_product',
    )
    empty_value_display = '-пусто-'
