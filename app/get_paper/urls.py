from django.urls import path
from .views import GetPaperView

urlpatterns = [
    path('get_paper/<int:pk>', GetPaperView.as_view(), name='get_paper'),
    path('get_paper/', GetPaperView.as_view(), name='all_papers')
]