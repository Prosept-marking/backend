from dealers.models import DealersNames, DealersProducts
from django.test import TestCase
from owner.models import OwnerProducts, ProductRelation
from statistic.models import ComparisonSallers, DailyStatistics


class DealerModelTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.task = DealersNames.objects.create(
            dealer_id=101,
            name='Тестовое название',
        )

    def test_title_label(self):
        """verbose_name поля name совпадает с ожидаемым."""
        task = DealerModelTest.task
        field_verboses = {
            'name': 'Наименование Дилера',
        }
        for field, expected_value in field_verboses.items():
            with self.subTest(field=field):
                self.assertEqual(
                    task._meta.get_field(field).verbose_name, expected_value)

    def test_object_name_is_title_fild(self):
        """__str__  task - это строчка с содержимым task.title."""
        task = DealerModelTest.task
        expected_object_name = task.name
        self.assertEqual(expected_object_name, str(task))


class DealerProductModelTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.task = DealersProducts.objects.create(
            dealer_id=101,
            product_key='key10',
            price=3,
            product_url='http://test.ru',
            product_name='Тестовое название',
            pk_owner_product=10,
            name_1c_owner='тестовое название производителя',
            date='2002-10-10',
            matched=True,
            postponed=False,
        )
        cls.task_post = DealersProducts.objects.create(
            dealer_id=101,
            product_key='key10',
            price=3,
            product_url='http://test.ru',
            product_name='Тестовое название',
            pk_owner_product=10,
            name_1c_owner='тестовое название производителя',
            date='2002-10-10',
            matched=False,
            postponed=True,
        )
        cls.task_unproc = DealersProducts.objects.create(
            dealer_id=101,
            product_key='key10',
            price=3,
            product_url='http://test.ru',
            product_name='Тестовое название',
            pk_owner_product=10,
            name_1c_owner='тестовое название производителя',
            date='2002-10-10',
            matched=False,
            postponed=False,
        )

    def test_titles_label(self):
        """verbose_name полей DealerProduct совпадает с ожидаемым."""
        task = DealerProductModelTest.task
        field_verboses = {
            'dealer_id': 'ID дилера',
            'product_key': 'Ключ(id) товара дилера',
            'price': 'Цена дилера',
            'product_url': 'Ссылка на товар дилера',
            'product_name': 'Наименование товара дилера',
            'name_1c_owner': 'Наименование товара производителя',
            'matched': 'Согласованный',
            'postponed': 'Отложенный',
            'combined_status': 'Комбинированный статус',
        }
        for field, expected_value in field_verboses.items():
            with self.subTest(field=field):
                self.assertEqual(
                    task._meta.get_field(field).verbose_name, expected_value)

    def test_title_help_text(self):
        """help_text поля date совпадает с ожидаемым."""
        task = DealerProductModelTest.task
        help_text = task._meta.get_field('date').help_text
        self.assertEqual(help_text, 'Format: YYYY-MM-DD')

    def test_object_name_is_title_fild(self):
        """__str__  task - это строчка с содержимым task.title."""
        task = DealerProductModelTest.task
        expected_object_name = task.product_name
        self.assertEqual(expected_object_name, str(task))

    def test_combined_status_save_matched(self):
        """Содержимое поля combined_status преобразуется в matched."""
        task = DealerProductModelTest.task
        combined_status = task.combined_status
        self.assertEqual(combined_status, 'matched')

    def test_combined_status_save_postponed(self):
        """Содержимое поля combined_status преобразуется в postponed."""
        task = DealerProductModelTest.task_post
        combined_status = task.combined_status
        self.assertEqual(combined_status, 'postponed')

    def test_combined_status_save_unprocessed(self):
        """Содержимое поля combined_status преобразуется в unprocessed."""
        task = DealerProductModelTest.task_unproc
        combined_status = task.combined_status
        self.assertEqual(combined_status, 'unprocessed')


class OwnerProductModelTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.task = OwnerProducts.objects.create(
            dealer_id=101,
            name='Тестовое название',
        )

    def test_titles_label(self):
        """verbose_name поля title совпадает с ожидаемым."""
        task = ProductRelationModelTest.task
        field_verboses = {
            'article': 'Артикул',
            'ean_13': 'European Article Number',
            'name': 'Наименование товара',
            'name_1c': 'Наименование товара Просепт в 1С',
            'cost': 'Цена',
            'recommended_price': 'Рекомендуемая стоимость',
            'category_id': 'ID категории',
            'ozon_name': 'Наименование товара в OZON',
            'wb_name': 'Наименование товара в WB',
            'ozon_article': 'Артикул OZON',
            'wb_article': 'Артикул WB',
            'ym_article': 'Артикул YM',
            'wb_article_td': 'Артикул WB_TD'
        }
        for field, expected_value in field_verboses.items():
            with self.subTest(field=field):
                self.assertEqual(
                    task._meta.get_field(field).verbose_name, expected_value)

    def test_object_name_is_title_fild(self):
        """__str__  task - это строчка с содержимым task.title."""
        task = ProductRelationModelTest.task
        expected_object_name = task.name_1c
        self.assertEqual(expected_object_name, str(task))


class ProductRelationModelTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.task = ProductRelation.objects.create(
            dealer_product=101,
            owner_product='Тестовое название',
        )

    def test_titles_label(self):
        """verbose_name полей title совпадает с ожидаемым."""
        task = ProductRelationModelTest.task
        field_verboses = {
            'dealer_product': 'Товар дилера',
            'owner_product': 'Товар производителя',
        }
        for field, expected_value in field_verboses.items():
            with self.subTest(field=field):
                self.assertEqual(
                    task._meta.get_field(field).verbose_name, expected_value)

    def test_object_name_is_title_fild(self):
        """__str__  task - это строчка с содержимым task.title."""
        task = ProductRelationModelTest.task
        expected_object_name = (
            f'Сопоставление {task.dealer_product.product_name}  и'
            f' {task.owner_product.name_1c}'
        )
        self.assertEqual(expected_object_name, str(task))


class DayilyStatModelTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.task = DailyStatistics.objects.create(
            daily_unverified_product=12,
            unverified_product=6,
            verified_product=5,
            rejected_product=1
        )

    def test_titles_label(self):
        """verbose_name полей DailyStatistic совпадает с ожидаемым."""
        task = DayilyStatModelTest.task
        field_verboses = {
            'daily_unverified_product': 'Непровернный товар на начало дня',
            'unverified_product': 'Непроверенный товар на конец дня',
            'verified_product': 'Проверенный товар на конец дня',
            'rejected_product': 'Отложенный товар',
        }
        for field, expected_value in field_verboses.items():
            with self.subTest(field=field):
                self.assertEqual(
                    task._meta.get_field(field).verbose_name, expected_value)

    def test_object_name_is_title_fild(self):
        """__str__  task - это строчка с содержимым task.title."""
        task = DayilyStatModelTest.task
        expected_object_name = 'Модель статистики по работе с товарами'
        self.assertEqual(expected_object_name, str(task))


class ComparisonSallersModelTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.saller = DealersNames.objects.create(
            dealer_id=1,
            name='Название'
        )
        cls.task = ComparisonSallers.objects.create(
            saller_name=cls.saller.pk,
            verified_product='Проверенный товар компании',
            unverified_product='Непроверенный товар организации',
            all_product='Все продукты компании'
        )

    def test_title_label(self):
        """verbose_name полей ComparisonSallers совпадает с ожидаемым."""
        task = ComparisonSallersModelTest.task
        field_verboses = {
            'saller_name': 'Название организации продавца',
            'verified_product': 'Проверенный товар компании',
            'unverified_product': 'Непроверенный товар организации',
            'all_product': 'Все продукты компании'
        }
        for field, expected_value in field_verboses.items():
            with self.subTest(field=field):
                self.assertEqual(
                    task._meta.get_field(field).verbose_name, expected_value)
