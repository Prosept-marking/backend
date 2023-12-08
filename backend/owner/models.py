from dealers.models import DealersProducts
from django.conf import settings
from django.db import models


class OwnerProducts(models.Model):
    """Товары производителя Просепт."""
    owner_id = models.IntegerField(default=0)
    article = models.CharField(
        'Артикул',
        max_length=settings.MAX_NAME_LENGTH,
        null=True,
        blank=True,
    )
    ean_13 = models.CharField(
        'European Article Number',
        null=True,
        blank=True,
    )
    name = models.CharField(
        'Наименование товара',
        max_length=settings.MAX_NAME_LENGTH,
        null=True,
        blank=True,
    )
    name_1c = models.CharField(
        'Наименование товара Просепт в 1С',
        max_length=settings.MAX_NAME_LENGTH,
        null=True,
        blank=True,
    )
    cost = models.DecimalField(
        'Цена',
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
    )
    recommended_price = models.DecimalField(
        'Рекомендуемая стоимость',
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
    )
    category_id = models.CharField(
        'ID категории',
        null=True,
        blank=True,
    )
    ozon_name = models.CharField(
        'Наименование товара в OZON',
        max_length=settings.MAX_NAME_LENGTH,
        null=True,
        blank=True,
    )
    wb_name = models.CharField(
        'Наименование товара в WB',
        max_length=settings.MAX_NAME_LENGTH,
        null=True,
        blank=True,
    )
    ozon_article = models.CharField(
        'Артикул OZON',
        max_length=settings.MAX_NAME_LENGTH,
        null=True,
        blank=True,
    )
    wb_article = models.CharField(
        'Артикул WB',
        max_length=settings.MAX_NAME_LENGTH,
        null=True,
        blank=True,
    )
    ym_article = models.CharField(
        'Артикул YM',
        max_length=settings.MAX_NAME_LENGTH,
        null=True,
        blank=True,
    )
    wb_article_td = models.CharField(
        'Артикул WB_TD',
        max_length=settings.MAX_NAME_LENGTH,
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = 'Товар Просепт'
        verbose_name_plural = 'Товары Просепт'

    def __str__(self):
        return self.name_1c


class ProductRelation(models.Model):
    """
    Модель для сопоставления товаров между DealersProducts и OwnerProducts.
    """
    dealer_product = models.ForeignKey(
        DealersProducts,
        on_delete=models.CASCADE,
        verbose_name='Товар дилера',
    )
    owner_product = models.ForeignKey(
        OwnerProducts,
        on_delete=models.CASCADE,
        verbose_name='Товар производителя',
    )
    date = models.DateField(auto_now=True)

    class Meta:
        verbose_name = 'Сопоставление товаров'
        verbose_name_plural = 'Сопоставления товаров'

    def __str__(self):
        return f'Сопоставление {self.dealer_product.product_name}  и' \
               f' {self.owner_product.name_1c}'
