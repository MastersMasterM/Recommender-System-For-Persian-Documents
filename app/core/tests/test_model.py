from django.test import TestCase
from core.models import Paper


class ModelTest(TestCase):
    """Test Models"""

    def test_create_new_object(self):
        """Test creating a paper object"""
        sample_paper = Paper.objects.create(
            uid="663026",
            title="بررسی و تحلیل عناصر رنگ و بو در مثنوی مولانا",
            abstract="تست چکیده",
            fl_subject="هنر و ادبيات",
            sl_subject="ادبیات فارسی"
        )
        self.assertEqual(str(sample_paper), sample_paper.title)
