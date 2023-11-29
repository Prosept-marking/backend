import csv

from django.core.management.base import BaseCommand

from owner.models import OwnerProducts


class Command(BaseCommand):
    help = 'Загрузка товаров производителя Просепт из файла CSV'

    def handle(self, *args, **kwargs):
        csv_file = 'data/marketing_product.csv'
        with open(csv_file, 'r', encoding='utf-8') as file:
            csv_reader = csv.reader(file, delimiter=';')
            next(csv_reader)
            for row in csv_reader:
                ean_13 = row[3]
                cost = row[5] if row[5] else None
                recommended_price = row[6] if row[6] else None
                owner, created = OwnerProducts.objects.get_or_create(
                    owner_id=row[0],
                    article=row[2],
                    ean_13=ean_13,
                    cost=cost,
                    recommended_price=recommended_price,
                    category_id=row[7],
                    name_1c=row[9],
                )
                if created:
                    self.stdout.write(
                        self.style.SUCCESS(f'товар "{ean_13}" загружен.'))
                else:
                    self.stdout.write(self.style.SUCCESS(
                        f'товар "{ean_13}" уже в базе.'))
