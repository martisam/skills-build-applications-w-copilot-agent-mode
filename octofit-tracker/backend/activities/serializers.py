from rest_framework import serializers
from .models import Activity


class ActivitySerializer(serializers.ModelSerializer):
    """Serializer for Activity model"""
    username = serializers.CharField(source='user.username', read_only=True)
    
    class Meta:
        model = Activity
        fields = [
            'id', 'user', 'username', 'activity_type', 'title', 'description',
            'duration_minutes', 'calories_burned', 'distance_km', 'intensity',
            'location', 'activity_date', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']
