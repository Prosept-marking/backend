# flake8: noqa

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dealers', '0008_dealersproducts_combined_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='dealersproducts',
            name='name_1c_owner',
            field=models.CharField(blank=True, default=None, max_length=254,
                                   null=True, verbose_name='Наименование товара производителя'),
        ),
        migrations.AddField(
            model_name='dealersproducts',
            name='pk_owner_product',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
    ]
