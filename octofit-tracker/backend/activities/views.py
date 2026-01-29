from rest_framework import viewsets, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Activity
from .serializers import ActivitySerializer


class ActivityViewSet(viewsets.ModelViewSet):
    """
    API endpoint for activities.
    Users can log and view their activities.
    """
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['activity_type', 'user', 'intensity']
    ordering_fields = ['activity_date', 'created_at', 'duration_minutes', 'calories_burned']
    ordering = ['-activity_date']
    
    def get_queryset(self):
        """Return activities, optionally filtered by user"""
        queryset = Activity.objects.all()
        user_id = self.request.query_params.get('user_id', None)
        if user_id is not None:
            queryset = queryset.filter(user_id=user_id)
        # Users can only see their own activities unless they're staff
        if not self.request.user.is_staff:
            queryset = queryset.filter(user=self.request.user)
        return queryset
    
    def perform_create(self, serializer):
        """Create activity for the authenticated user"""
        serializer.save(user=self.request.user)
