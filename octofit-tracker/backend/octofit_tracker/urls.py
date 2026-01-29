"""
URL configuration for octofit_tracker project.
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.reverse import reverse
import os


class APIRootView(APIView):
    """
    API root endpoint that lists all available endpoints
    """
    def get(self, request, format=None):
        # Get CODESPACE_NAME environment variable
        codespace_name = os.getenv('CODESPACE_NAME', '')
        
        # Construct the base URL for codespace or localhost
        if codespace_name:
            # Use HTTPS for GitHub Codespace URL
            base_url = f"https://{codespace_name}-8000.app.github.dev"
        elif request.is_secure():
            base_url = f"https://{request.get_host()}"
        else:
            base_url = f"http://{request.get_host()}"
        
        return Response({
            'message': 'Welcome to OctoFit Tracker API',
            'version': '1.0.0',
            'base_url': base_url,
            'codespace_name': codespace_name if codespace_name else 'localhost',
            'endpoints': {
                'admin': f"{base_url}/admin/",
                'auth': f"{base_url}/api/auth/",
                'users': f"{base_url}/api/users/",
                'activities': f"{base_url}/api/activities/",
                'teams': f"{base_url}/api/teams/",
                'workouts': f"{base_url}/api/workouts/",
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
