from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    TeamViewSet, TeamMembershipViewSet,
    LeaderboardViewSet, LeaderboardEntryViewSet
)

router = DefaultRouter()
router.register(r'teams', TeamViewSet)
router.register(r'memberships', TeamMembershipViewSet)
router.register(r'leaderboards', LeaderboardViewSet)
router.register(r'leaderboard-entries', LeaderboardEntryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
