from api.v1.views import ComparisonSallersViewSet, DailyStatisticsViewSet
from django.test import SimpleTestCase
from django.urls import resolve, reverse
from rest_framework import status
from rest_framework.test import APITestCase


class ApiUrlsTests(SimpleTestCase):
    def test_get_dailystatistic_is_resolved(self):
        url = reverse('api_v1:dailystatistic')
        self.assertEqual(
            resolve(url).func.view_class, DailyStatisticsViewSet)

    def test_get_dealersstatistic_is_resolved(self):
        url = reverse('api_v1:dealersstatistic')
        self.assertEqual(
            resolve(url).func.view_class, ComparisonSallersViewSet)


class CustomerAPIViewTests(APITestCase):
    url_1 = reverse('api_v1:dailystatistic')
    url_2 = reverse('api_v1:dealersstatistic')

    def test_get_customers(self):
        response_1 = self.client.get(self.url_1)
        response_2 = self.client.get(self.url_2)
        self.assertEqual(response_1.status_code, status.HTTP_200_OK)
        self.assertEqual(response_2.status_code, status.HTTP_200_OK)

    def test_post_dailystatistic(self):
        data = {
            'date': '',
            'daily_unverified_product': '',
            'unverified_product': '',
            'verified_product': '',
            'rejected_product': ''
        }
        response = self.client.post(self.url_1, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(len(response.data), 5)

    def test_post_dealersstatistic(self):
        data = {
            'saller_name': '',
            'verified_product': '',
            'unverified_product': '',
            'rejected_product': '',
            'all_product': ''
        }
        response = self.client.post(self.url_2, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(len(response.data), 5)
