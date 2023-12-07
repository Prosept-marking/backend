from api.v1.views import DealerNamesViewSet, DealerProductsViewSet
from django.test import SimpleTestCase
from django.urls import resolve, reverse
from rest_framework import status
from rest_framework.test import APITestCase


class ApiUrlsTests(SimpleTestCase):
    def test_get_dealernames_is_resolved(self):
        url = reverse('api_v1:dealernames')
        self.assertEqual(
            resolve(url).func.view_class, DealerNamesViewSet)

    def test_get_dealerproducts_is_resolved(self):
        url = reverse('api_v1:dealerproducts')
        self.assertEqual(
            resolve(url).func.view_class, DealerProductsViewSet)


class CustomerAPIViewTests(APITestCase):
    url_1 = reverse('api_v1:dealernames')
    url_2 = reverse('api_v1:dealerproducts')

    def test_get_customers(self):
        response_1 = self.client.get(self.url_1)
        response_2 = self.client.get(self.url_2)
        self.assertEqual(response_1.status_code, status.HTTP_200_OK)
        self.assertEqual(response_2.status_code, status.HTTP_200_OK)

    def test_post_dealernames(self):
        data = {
            'name': 'test',
        }
        response = self.client.post(self.url_1, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(len(response.data), 3)
        response = self.client.delete(self.url_1, data, format='json')
        self.assertEqual(
            response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED
        )

    def test_post_dealerproducts(self):
        data = {
            'product_key': '1234',
            'product_url': 'https://example.com',
            'product_name': 'test_product_name',
            'date': '2004-12-12',
        }
        response = self.client.post(self.url_2, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(len(response.data), 13)
