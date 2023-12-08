import csv

from dealers.models import DealersNames, DealersProducts
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Загрузка товаров дилеров из файла CSV'

    def handle(self, *args, **kwargs):
        csv_file = 'data/marketing_dealerprice.csv'
        with open(csv_file, encoding='utf-8') as file:
            csv_reader = csv.reader(file, delimiter=';')
            next(csv_reader)
            for row in csv_reader:
                dealer_id = int(row[6])
                dealer = DealersNames.objects.get(dealer_id=dealer_id)
                product_key = row[1]
                dealer, created = DealersProducts.objects.get_or_create(
                    product_key=product_key,
                    price=row[2],
                    product_url=row[3],
                    product_name=row[4],
                    date=row[5],
                    dealer_id=dealer,
                )
                if created:
                    self.stdout.write(
                        self.style.SUCCESS(f'товар "{product_key}" загружен.'))
                else:
                    self.stdout.write(self.style.SUCCESS(
                        f'товар "{product_key}" уже в базе.'))
