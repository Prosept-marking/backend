from datetime import date

from dealers.models import DealersNames
from django.db import models


class DailyStatistics(models.Model):
    """Модель для подсчета ежедневной статистики работы с товаром."""
    date = models.DateField(default=date.today)
    daily_unverified_product = models.PositiveIntegerField(
        'Непровернный товар на начало дня',
        default=0)
    unverified_product = models.PositiveIntegerField(
        'Непроверенный товар на конец дня',
        default=0)
    verified_product = models.PositiveIntegerField(
        'Проверенный товар на конец дня',
        default=0)
    rejected_product = models.PositiveIntegerField(
        'Отложенный товар',
        default=0)

    class Meta:
        verbose_name = 'Статистика по работе с товарами'

    def __str__(self):
        return 'Модель статистики по работе с товарами'


class ComparisonSallers(models.Model):
    """Модель статистики сопоставлений по продавцу."""
    saller_name = models.ForeignKey(
        DealersNames,
        on_delete=models.CASCADE,
        verbose_name='Название организации продавца'
    )
    verified_product = models.PositiveIntegerField(
        'Проверенный товар компании',
        default=0)
    unverified_product = models.PositiveIntegerField(
        'Непроверенный товар организации',
        default=0)
    all_product = models.PositiveIntegerField(
        'Все продукты компании'
    )

    class Meta:
        verbose_name = 'Статистика сопоставлений товара по продавцу'

    def __str__(self):
        return 'Статистика сопоставлений товара по продавцу'
