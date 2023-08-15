"""
Defining Serializers
"""
from rest_framework.serializers import ModelSerializer
from core.models import Paper


class PaperSerializer(ModelSerializer):
    """Serializer for Paper"""
    
    class Meta:
        model = Paper
        fields = '__all__'