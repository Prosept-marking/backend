# flake8: noqa

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('owner', '0007_ownerproducts_name_ownerproducts_ozon_article_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ownerproducts',
            name='wb_name',
            field=models.CharField(
                blank=True, max_length=254, null=True, verbose_name='Наименование товара в WB'),
        ),
    ]
