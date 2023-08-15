"""
Paper_Creation Views
"""
from rest_framework.viewsets import ModelViewSet

from paper_creation.serializers import PaperSerializer
from core.models import Paper


class PaperViewSet(ModelViewSet):
    """View for manage recipe APIs"""
    serializer_class = PaperSerializer
    queryset = Paper.objects.all()
