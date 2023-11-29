# flake8: noqa

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dealers', '0004_alter_dealersnames_options'),
        ('owner', '0006_productrelation'),
    ]

    operations = [
        migrations.AddField(
            model_name='ownerproducts',
            name='name',
            field=models.CharField(
                blank=True, max_length=254, null=True, verbose_name='Наименование товара'),
        ),
        migrations.AddField(
            model_name='ownerproducts',
            name='ozon_article',
            field=models.CharField(
                blank=True, max_length=254, null=True, verbose_name='Артикул OZON'),
        ),
        migrations.AddField(
            model_name='ownerproducts',
            name='ozon_name',
            field=models.CharField(
                blank=True, max_length=254, null=True, verbose_name='Наименование товара в OZON'),
        ),
        migrations.AddField(
            model_name='ownerproducts',
            name='wb_article',
            field=models.CharField(
                blank=True, max_length=254, null=True, verbose_name='Артикул WB'),
        ),
        migrations.AddField(
            model_name='ownerproducts',
            name='wb_article_td',
            field=models.CharField(
                blank=True, max_length=254, null=True, verbose_name='Артикул WB_TD'),
        ),
        migrations.AddField(
            model_name='ownerproducts',
            name='wb_name',
            field=models.CharField(
                blank=True, max_length=254, null=True, verbose_name='Наименование товара в OZON'),
        ),
        migrations.AddField(
            model_name='ownerproducts',
            name='ym_article',
            field=models.CharField(
                blank=True, max_length=254, null=True, verbose_name='Артикул YM'),
        ),
        migrations.AlterField(
            model_name='productrelation',
            name='dealer_product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                    to='dealers.dealersproducts', verbose_name='Товар дилера'),
        ),
    ]
