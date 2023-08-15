"""
Paper_Creation Views
"""
from rest_framework.viewsets import ModelViewSet

from paper_creation.serializers import PaperSerializer
from core.models import Paper
from .tasks import recompute_embeddings


class PaperViewSet(ModelViewSet):
    """View for manage recipe APIs"""
    serializer_class = PaperSerializer
    queryset = Paper.objects.all()

    def create(self, request, *args, **kwargs):
        recompute_embeddings.delay()
        return super().create(request, *args, **kwargs)
