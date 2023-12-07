from api.v1.views import OwnerProductsViewSet, ProductRelationViewSet
from django.test import SimpleTestCase
from django.urls import resolve, reverse
from rest_framework import status
from rest_framework.test import APITestCase


class ApiUrlsTests(SimpleTestCase):
    def test_get_ownerproducts_is_resolved(self):
        url = reverse('api.v1:ownerproducts')
        self.assertEqual(
            resolve(url).func.view_class, OwnerProductsViewSet)

    def test_get_productrelation_is_resolved(self):
        url = reverse('api.v1:productrelation')
        self.assertEqual(
            resolve(url).func.view_class, ProductRelationViewSet)


class CustomerAPIViewTests(APITestCase):
    url_1 = reverse('api.v1:ownerproducts')
    url_2 = reverse('api.v1:productrelation')

    def test_get_customers(self):
        response_1 = self.client.get(self.url_1)
        response_2 = self.client.get(self.url_2)
        self.assertEqual(response_1.status_code, status.HTTP_200_OK)
        self.assertEqual(response_2.status_code, status.HTTP_200_OK)

    def test_post_dealernames(self):
        data = {
            'title': 'Mr',
            'name': 'Peter',
            'last_name': 'Parkerz',
            'gender': 'M',
            'status': 'published'
        }
        response = self.client.post(self.url_1, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(len(response.data), 8)

    def test_post_dealerproducts(self):
        data = {
            'title': 'Mr',
            'name': 'Peter',
            'last_name': 'Parkerz',
            'gender': 'M',
            'status': 'published'
        }
        response = self.client.post(self.url_2, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(len(response.data), 8)
