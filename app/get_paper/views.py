"""
Views for the get_paper API
"""
from rest_framework.views import APIView
from rest_framework.response import Response

from django.http import Http404

from core.models import Paper
from paper_creation.serializers import PaperSerializer
from .serializers import GetPaperSerializer

import redis

r = redis.Redis(db=2,host='redis', port=6379)

class GetPaperView(APIView):
    def get_object(self, pk):
        if pk is not None:
            try:
                return Paper.objects.get(pk=pk)
            except Paper.DoesNotExist:
                raise Http404

    def get(self, request=None, pk=None, format=None):
        if pk is not None:
            instance = self.get_object(pk)
            id_list = r.get(str(pk))
            id_list = id_list.decode('utf-8')
            id_list = id_list.strip('][').split(', ')
            recommended_papers = [self.get_object(i) for i in id_list]
            serializer = GetPaperSerializer(instance, context={'recommended_papers': recommended_papers})
            return Response(serializer.data)
        else:
            queryset = Paper.objects.all()[:10]
            serializer = PaperSerializer(queryset, many=True)
            return Response(serializer.data)