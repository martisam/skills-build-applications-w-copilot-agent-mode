from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    WorkoutViewSet, WorkoutPlanViewSet, WorkoutPlanDayViewSet
)

router = DefaultRouter()
router.register(r'templates', WorkoutViewSet, basename='workout')
router.register(r'plans', WorkoutPlanViewSet, basename='workout-plan')
router.register(r'plan-days', WorkoutPlanDayViewSet, basename='workout-plan-day')

urlpatterns = [
    path('', include(router.urls)),
]
