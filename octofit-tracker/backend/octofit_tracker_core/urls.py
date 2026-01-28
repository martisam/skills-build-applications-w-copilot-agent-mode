"""
URL configuration for octofit_tracker_core project.
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.reverse import reverse


class APIRootView(APIView):
    """
    API root endpoint that lists all available endpoints
    """
    def get(self, request, format=None):
        return Response({
            'message': 'Welcome to OctoFit Tracker API',
            'version': '1.0.0',
            'endpoints': {
                'admin': reverse('admin:index', request=request),
                'auth': reverse('rest_framework:api-root', request=request),
                'users': reverse('users-list', request=request),
                'activities': reverse('activity-list', request=request),
                'teams': reverse('team-list', request=request),
                'workouts': reverse('workout-list', request=request),
                'documentation': 'See endpoints below for full API documentation',
            },
            'available_endpoints': {
                'api/users/': 'User management and profiles',
                'api/activities/': 'Activity logging and tracking',
                'api/teams/': 'Team management and leaderboards',
                'api/workouts/': 'Workout templates and plans',
                'api/auth/': 'Authentication endpoints',
            }
        })


urlpatterns = [
    path('', APIRootView.as_view(), name='api-root'),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/auth/', include('dj_rest_auth.urls')),
    path('api/auth/registration/', include('dj_rest_auth.registration.urls')),
    path('api/users/', include('users.urls')),
    path('api/activities/', include('activities.urls')),
    path('api/teams/', include('teams.urls')),
    path('api/workouts/', include('workouts.urls')),
]
