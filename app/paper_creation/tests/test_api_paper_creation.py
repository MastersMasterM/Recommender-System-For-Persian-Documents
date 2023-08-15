"""
Testing Create Papers Functionality
"""
from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient

from core.models import Paper


PAPER_URL = reverse('paper_creation:paper_creation-list')


class Paper_Creation_API_Test(TestCase):
    """Testing API Functionality"""

    def setUp(self):
        self.client = APIClient()

    def test_Paper_Creation(self):
        """Test Changing a Paper Details"""
        sample_paper = {
            'uid': "663026",
            'title': "بررسی و تحلیل عناصر رنگ و بو در مثنوی مولانا",
            'abstract': "تست چکیده شسیشسیشسیشیشسییییشسیشسسشیشستیشسهیتشسیتشسیشخهسیتشخسهیتشسیتشخهسیتشخهسیتشخهیشیسخهتشخیهتشخیتشخیتشخیهتشسیخهتشسیخهشتیخهتش",
            'fl_subject': "هنر و ادبيات",
            'sl_subject': "ادبیات فارسی"
        }

        response = self.client.post(PAPER_URL, sample_paper)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        created_paper = Paper.objects.get(id=response.data['id'])

        for k, v in sample_paper.items():
            self.assertEqual(getattr(created_paper, k), v)

    def test_paper_data_changing(self):
        """Test Changing a Paper Details"""
        sample_paper = {
            'uid': "663026",
            'title': "بررسی و تحلیل عناصر رنگ و بو در مثنوی مولانا",
            'abstract': "تست چکیده شسیشسیشسیشیشسییییشسیشسسشیشستیشسهیتشسیتشسیشخهسیتشخسهیتشسیتشخهسیتشخهسیتشخهیشیسخهتشخیهتشخیتشخیتشخیهتشسیخهتشسیخهشتیخهتش",
            'fl_subject': "هنر و ادبيات",
            'sl_subject': "ادبیات فارسی"
        }

        response = self.client.post(PAPER_URL, sample_paper)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        this_paper_url = reverse('paper_creation:paper_creation-detail', args=[response.data['id']])

        new_data = {
            'title': 'عنوان جدید'
        }
        response2 = self.client.patch(this_paper_url, new_data)
        self.assertEqual(response2.status_code, status.HTTP_200_OK)
        modified_paper = Paper.objects.get(id=response.data['id'])

        self.assertEqual(getattr(modified_paper, 'title'), new_data['title'])
