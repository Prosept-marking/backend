# flake8: noqa

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dealers', '0009_dealersproducts_name_1c_owner_and_more'),
        ('statistic', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comparisonsallers',
            name='rejected_product',
            field=models.PositiveIntegerField(
                default=0, verbose_name='Колличество отклоненных сопоставленй'),
        ),
        migrations.AlterField(
            model_name='comparisonsallers',
            name='all_product',
            field=models.PositiveIntegerField(
                verbose_name='Все товары организации'),
        ),
        migrations.AlterField(
            model_name='comparisonsallers',
            name='saller_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                    to='dealers.dealersnames', verbose_name='Название организации дилера'),
        ),
        migrations.AlterField(
            model_name='comparisonsallers',
            name='unverified_product',
            field=models.PositiveIntegerField(
                default=0, verbose_name='Количество неразмеченных товаров дилера'),
        ),
        migrations.AlterField(
            model_name='comparisonsallers',
            name='verified_product',
            field=models.PositiveIntegerField(
                default=0, verbose_name='Количество сопоставленных товаров дилера'),
        ),
        migrations.AlterField(
            model_name='dailystatistics',
            name='daily_unverified_product',
            field=models.PositiveIntegerField(
                default=0, verbose_name='Количество неразмеченных товаров на начало дня'),
        ),
        migrations.AlterField(
            model_name='dailystatistics',
            name='rejected_product',
            field=models.PositiveIntegerField(
                default=0, verbose_name='Количество отклоненных сопоставлений'),
        ),
        migrations.AlterField(
            model_name='dailystatistics',
            name='unverified_product',
            field=models.PositiveIntegerField(
                default=0, verbose_name='Количество неразмеченных товаров на конец дня'),
        ),
        migrations.AlterField(
            model_name='dailystatistics',
            name='verified_product',
            field=models.PositiveIntegerField(
                default=0, verbose_name='Количество сопоставленных товаров на конец дня'),
        ),
    ]
