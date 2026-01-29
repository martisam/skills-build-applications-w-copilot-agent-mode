from rest_framework import serializers
from .models import Workout, WorkoutPlan, WorkoutPlanDay


class WorkoutSerializer(serializers.ModelSerializer):
    """Serializer for Workout model"""
    class Meta:
        model = Workout
        fields = [
            'id', 'title', 'description', 'category', 'difficulty',
            'estimated_duration_minutes', 'estimated_calories',
            'instructions', 'equipment_needed', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']


class WorkoutPlanDaySerializer(serializers.ModelSerializer):
    """Serializer for WorkoutPlanDay model"""
    workout = WorkoutSerializer(read_only=True)
    workout_id = serializers.PrimaryKeyRelatedField(
        queryset=Workout.objects.all(),
        write_only=True,
        source='workout'
    )
    
    class Meta:
        model = WorkoutPlanDay
        fields = [
            'id', 'workout_plan', 'workout', 'workout_id', 'day_number',
            'is_rest_day', 'notes'
        ]
        read_only_fields = ['id']


class WorkoutPlanSerializer(serializers.ModelSerializer):
    """Serializer for WorkoutPlan model"""
    days = WorkoutPlanDaySerializer(many=True, read_only=True)
    username = serializers.CharField(source='user.username', read_only=True)
    
    class Meta:
        model = WorkoutPlan
        fields = [
            'id', 'user', 'username', 'name', 'description', 'workouts',
            'duration_days', 'difficulty_level', 'is_active', 'days',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'workouts', 'created_at', 'updated_at']
