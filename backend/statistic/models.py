from datetime import date

from dealers.models import DealersNames
from django.db import models


class DailyStatistics(models.Model):
    """Модель для подсчета ежедневной статистики работы с товаром."""
    date = models.DateField(default=date.today)
    daily_unverified_product = models.PositiveIntegerField(
        'Количество неразмеченных товаров на начало дня',
        default=0)
    unverified_product = models.PositiveIntegerField(
        'Количество неразмеченных товаров на конец дня',
        default=0)
    verified_product = models.PositiveIntegerField(
        'Количество сопоставленных товаров на конец дня',
        default=0)
    rejected_product = models.PositiveIntegerField(
        'Количество отклоненных сопоставлений',
        default=0)

    class Meta:
        verbose_name = 'Статистика по работе с товарами'

    def __str__(self):
        return 'Модель статистики по работе с товарами'


class ComparisonSallers(models.Model):
    """Модель статистики сопоставлений по дилеру."""
    saller_name = models.ForeignKey(
        DealersNames,
        on_delete=models.CASCADE,
        verbose_name='Название организации дилера'
    )
    verified_product = models.PositiveIntegerField(
        'Количество сопоставленных товаров дилера',
        default=0)
    unverified_product = models.PositiveIntegerField(
        'Количество неразмеченных товаров дилера',
        default=0)
    all_product = models.PositiveIntegerField(
        'Все товары организации'
    )
    rejected_product = models.PositiveIntegerField(
        'Колличество отклоненных сопоставленй',
        default=0)

    class Meta:
        verbose_name = 'Статистика сопоставлений товара по продавцу'

    def __str__(self):
        return 'Статистика сопоставлений товара по продавцу'
