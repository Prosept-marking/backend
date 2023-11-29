import csv

from dealers.models import DealersNames
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Загрузка имён дилеров из файла CSV'

    def handle(self, *args, **kwargs):
        csv_file = 'data/marketing_dealer.csv'
        with open(csv_file, encoding='utf-8') as file:
            csv_reader = csv.reader(file, delimiter=';')
            next(csv_reader)
            for row in csv_reader:
                dealer_id, name = row
                dealer, created = DealersNames.objects.get_or_create(
                    dealer_id=dealer_id,
                    name=name
                )
                if created:
                    self.stdout.write(
                        self.style.SUCCESS(f'dealer "{name}" загружен.'))
                else:
                    self.stdout.write(self.style.SUCCESS(
                        f'dealer "{name}" уже в базе.'))
