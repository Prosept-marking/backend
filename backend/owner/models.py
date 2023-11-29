from django.db import models
from django.conf import settings


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

    class Meta:
        verbose_name = 'Товар Просепт'
        verbose_name_plural = 'Товары Просепт'

    def __str__(self):
        return self.name_1c
