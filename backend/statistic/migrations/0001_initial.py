# flake8: noqa

import datetime

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dealers', '0007_dealersproducts_postponed'),
    ]

    operations = [
        migrations.CreateModel(
            name='DailyStatistics',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.date.today)),
                ('daily_unverified_product', models.PositiveIntegerField(
                    default=0, verbose_name='Непровернный товар на начало дня')),
                ('unverified_product', models.PositiveIntegerField(
                    default=0, verbose_name='Непроверенный товар на конец дня')),
                ('verified_product', models.PositiveIntegerField(
                    default=0, verbose_name='Проверенный товар на конец дня')),
                ('rejected_product', models.PositiveIntegerField(
                    default=0, verbose_name='Отложенный товар')),
            ],
            options={
                'verbose_name': 'Статистика по работе с товарами',
            },
        ),
        migrations.CreateModel(
            name='ComparisonSallers',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('verified_product', models.PositiveIntegerField(
                    default=0, verbose_name='Проверенный товар компании')),
                ('unverified_product', models.PositiveIntegerField(
                    default=0, verbose_name='Непроверенный товар организации')),
                ('all_product', models.PositiveIntegerField(
                    verbose_name='Все продукты компании')),
                ('saller_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                 to='dealers.dealersnames', verbose_name='Название организации продавца')),
            ],
            options={
                'verbose_name': 'Статистика сопоставлений товара по продавцу',
            },
        ),
    ]
