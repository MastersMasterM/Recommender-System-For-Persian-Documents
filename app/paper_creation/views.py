"""
Paper_Creation Views
"""
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from paper_creation.serializers import PaperSerializer
from core.models import Paper
from .tasks import recompute_embeddings


class PaperViewSet(ModelViewSet):
    """View for manage recipe APIs"""
    serializer_class = PaperSerializer
    queryset = Paper.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        recompute_embeddings.delay()
        return super().create(request, *args, **kwargs)
