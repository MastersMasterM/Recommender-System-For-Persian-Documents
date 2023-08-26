"""
URL mapping for the PaperCreationAPI
"""
from django.urls import (
    path,
    include,
)

from rest_framework.routers import DefaultRouter

from paper_creation import views


router = DefaultRouter()
router.register('paper_creation', views.PaperViewSet, 'paper_creation')

app_name = 'paper_creation'

urlpatterns = [
    path('', include(router.urls)),
    path('updatelist/', views.RedisDataViewSet.as_view({'get': 'list'}), name='updatelist'),
]
