from django.db import models
from django.conf import settings


class DealersNames(models.Model):
    """Перечень Дилеров"""
    name = models.CharField(
            'Наименование Дилера',
            unique=True,
            max_length=settings.MAX_NAME_LENGTH,
    )


class DealersProducts(models.Model):
    """Товары всех дилеров"""
    dealer_id = models.ForeignKey(
            DealersNames,
            verbose_name='ID дилера',
            on_delete=models.CASCADE,
            related_name='dealer',
    )
    product_key = models.CharField(
            'Ключ(id) товара дилера',
            max_length=settings.MAX_NAME_LENGTH,
    )
    price = models.DecimalField(
        'Цена дилера',
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
    )
    product_url = models.URLField(
        'Ссылка на товар дилера',
        max_length=settings.MAX_NAME_LENGTH,
    )
    product_name = models.CharField(
            'Наименование товара дилера',
            unique=True,
            max_length=settings.MAX_NAME_LENGTH,
    )
    date = models.CharField(
        'date',
        max_length=10,
        help_text='Format: YYYY-MM-DD',
    )
    matched = models.BooleanField(
        'Согласованный',
        default=False,
    )

    class Meta:
        verbose_name = 'Продукт дилера'
        verbose_name_plural = 'Продукты дилеров'

    def __str__(self):
        return self.product_name