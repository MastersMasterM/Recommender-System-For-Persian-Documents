"""
Paper_Creation Views
"""
from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from paper_creation.serializers import PaperSerializer
from core.models import Paper
from .tasks import export_paper_table

import redis
import json

r = redis.Redis(db=2, host='redis', port=6379)

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

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)

        # Execute the task after the object has been created
        export_paper_table.delay()

        return response

class RedisDataViewSet(ViewSet):
    """View for Reloading Recommendation List"""
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def list(self, request):
        # Delete old data from Redis
        r.flushdb()

        # Load new data from JSON file
        with open('data/list.json', 'r') as f:
            res = json.load(f)

        # Convert data to bytes and set in Redis
        my_dict_bytes = {k: json.dumps(v).encode('utf-8') for k, v in res.items()}
        r.mset(my_dict_bytes)

        return Response({'message': 'Old data deleted. New data loaded to Redis.'})