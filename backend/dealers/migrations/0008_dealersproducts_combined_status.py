# flake8: noqa

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dealers', '0007_dealersproducts_postponed'),
    ]

    operations = [
        migrations.AddField(
            model_name='dealersproducts',
            name='combined_status',
            field=models.CharField(choices=[('matched', 'Согласованный'), ('postponed', 'Отложенный'), (
                'unprocessed', 'Необработанный')], default='unprocessed', max_length=20, verbose_name='Комбинированный статус'),
        ),
    ]
