"""
Serializer for get paper api
"""
from rest_framework import serializers

from paper_creation.serializers import PaperSerializer


class GetPaperSerializer(serializers.Serializer):
    uid = serializers.CharField(max_length=12)
    title = serializers.CharField()
    abstract = serializers.CharField()
    fl_subject = serializers.CharField()
    sl_subject = serializers.CharField()
    recommended_papers = serializers.SerializerMethodField()

    def get_recommended_papers(self, instance):
        recommended_papers = self.context.get('recommended_papers', [])
        serialized_recommended_papers = PaperSerializer(recommended_papers, many=True).data
        return serialized_recommended_papers
