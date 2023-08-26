"""
Paper_Creation Views
"""
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from paper_creation.serializers import PaperSerializer
from core.models import Paper
from .tasks import export_paper_table


class PaperViewSet(ModelViewSet):
    """View for managing paper APIs"""
    serializer_class = PaperSerializer
    queryset = Paper.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        last_paper = Paper.objects.order_by('-id').first()  # Get the last paper object

        if last_paper is not None:
            new_id = last_paper.id + 1  # Increment the last primary key value by one
            serializer.save(id=new_id)  # Save the new object with the updated primary key
        else:
            serializer.save()  # Save the new object using the default primary key generation

        # Execute the task after the object has been saved
        export_paper_table.delay()

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)

        # Execute the task after the object has been created
        export_paper_table.delay()

        return response