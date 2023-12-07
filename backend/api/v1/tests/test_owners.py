from api.v1.views import OwnerProductsViewSet, ProductRelationViewSet
from django.test import SimpleTestCase
from django.urls import resolve, reverse
from rest_framework import status
from rest_framework.test import APITestCase


class ApiUrlsTests(SimpleTestCase):
    def test_get_ownerproducts_is_resolved(self):
        url = reverse('api_v1:ownerproducts')
        self.assertEqual(
            resolve(url).func.view_class, OwnerProductsViewSet)

    def test_get_productrelation_is_resolved(self):
        url = reverse('api_v1:productrelation')
        self.assertEqual(
            resolve(url).func.view_class, ProductRelationViewSet)


class CustomerAPIViewTests(APITestCase):
    url_1 = reverse('api_v1:ownerproducts')
    url_2 = reverse('api_v1:productrelation')

    def test_get_customers(self):
        response_1 = self.client.get(self.url_1)
        response_2 = self.client.get(self.url_2)
        self.assertEqual(response_1.status_code, status.HTTP_200_OK)
        self.assertEqual(response_2.status_code, status.HTTP_200_OK)

    def test_post_ownerproducts(self):
        data = {
            'article': 'test_article',
            'ean_13': 'test_ean',
            'name': 'test_name',
            'name_1c': 'test_name',
            'cost': 3,
            'recommended_price': 10,
            'category_id': 'test_category',
            'ozon_name': 'test_ozon_name',
            'wb_name': 'test_wb_name',
            'ozon_article': 'test_ozon_art',
            'wb_article': 'test_wb_art',
        }
        response = self.client.post(self.url_1, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(len(response.data), 14)

    def test_post_productrelation(self):
        data = {
            'dealer_product': '',
            'owner_product': '',
        }
        response = self.client.post(self.url_2, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(len(response.data), 3)
