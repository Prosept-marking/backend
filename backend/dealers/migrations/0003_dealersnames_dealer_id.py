# Generated by Django 4.2.7 on 2023-11-28 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dealers', '0002_alter_dealersnames_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='dealersnames',
            name='dealer_id',
            field=models.IntegerField(default=0),
        ),
    ]