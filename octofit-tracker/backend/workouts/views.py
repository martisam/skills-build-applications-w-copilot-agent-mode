from rest_framework import viewsets, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Workout, WorkoutPlan, WorkoutPlanDay
from .serializers import WorkoutSerializer, WorkoutPlanSerializer, WorkoutPlanDaySerializer


class WorkoutViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint for workouts.
    View available workout templates.
    """
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['category', 'difficulty']
    search_fields = ['title', 'description']
    ordering_fields = ['created_at', 'estimated_duration_minutes', 'difficulty']
    ordering = ['-created_at']


class WorkoutPlanViewSet(viewsets.ModelViewSet):
    """
    API endpoint for workout plans.
    Users can create and manage their personalized workout plans.
    """
    queryset = WorkoutPlan.objects.all()
    serializer_class = WorkoutPlanSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['difficulty_level', 'is_active', 'user']
    ordering_fields = ['created_at', 'duration_days']
    ordering = ['-created_at']
    
    def get_queryset(self):
        """Return plans, optionally filtered by user"""
        queryset = WorkoutPlan.objects.all()
        user_id = self.request.query_params.get('user_id', None)
        if user_id is not None:
            queryset = queryset.filter(user_id=user_id)
        # Users can only see their own plans unless they're staff
        if not self.request.user.is_staff:
            queryset = queryset.filter(user=self.request.user)
        return queryset
    
    def perform_create(self, serializer):
        """Create plan for the authenticated user"""
        serializer.save(user=self.request.user)


class WorkoutPlanDayViewSet(viewsets.ModelViewSet):
    """
    API endpoint for workout plan days.
    Manage daily workout assignments.
    """
    queryset = WorkoutPlanDay.objects.all()
    serializer_class = WorkoutPlanDaySerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['workout_plan', 'is_rest_day']
    ordering = ['day_number']
