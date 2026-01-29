from rest_framework import viewsets, permissions, status, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import Team, TeamMembership, Leaderboard, LeaderboardEntry
from .serializers import (
    TeamSerializer, TeamMembershipSerializer,
    LeaderboardSerializer, LeaderboardEntrySerializer
)


class TeamViewSet(viewsets.ModelViewSet):
    """
    API endpoint for teams.
    Users can create, join, and manage teams.
    """
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'description']
    ordering_fields = ['created_at', 'name']
    ordering = ['-created_at']
    
    @action(detail=True, methods=['post'])
    def add_member(self, request, pk=None):
        """Add a member to the team"""
        team = self.get_object()
        user_id = request.data.get('user_id')
        role = request.data.get('role', 'member')
        
        if not user_id:
            return Response(
                {'error': 'user_id is required'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        try:
            membership, created = TeamMembership.objects.get_or_create(
                team=team,
                user_id=user_id,
                defaults={'role': role}
            )
            if created:
                return Response(
                    {'message': 'Member added successfully'},
                    status=status.HTTP_201_CREATED
                )
            return Response({'message': 'Member already in team'})
        except Exception as e:
            return Response(
                {'error': str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )
    
    @action(detail=True, methods=['post'])
    def remove_member(self, request, pk=None):
        """Remove a member from the team"""
        team = self.get_object()
        user_id = request.data.get('user_id')
        
        if not user_id:
            return Response(
                {'error': 'user_id is required'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        try:
            membership = TeamMembership.objects.get(team=team, user_id=user_id)
            membership.delete()
            return Response({'message': 'Member removed successfully'})
        except TeamMembership.DoesNotExist:
            return Response(
                {'error': 'Member not in team'},
                status=status.HTTP_404_NOT_FOUND
            )
    
    @action(detail=False, methods=['get'])
    def my_teams(self, request):
        """Get teams of the current user"""
        teams = Team.objects.filter(members=request.user)
        serializer = self.get_serializer(teams, many=True)
        return Response(serializer.data)
    
    def perform_create(self, serializer):
        """Create team with current user as owner"""
        serializer.save(owner=self.request.user)


class TeamMembershipViewSet(viewsets.ModelViewSet):
    """
    API endpoint for team memberships.
    Manage user roles within teams.
    """
    queryset = TeamMembership.objects.all()
    serializer_class = TeamMembershipSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['team', 'user', 'role']


class LeaderboardViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint for leaderboards.
    View team competition leaderboards.
    """
    queryset = Leaderboard.objects.all()
    serializer_class = LeaderboardSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    @action(detail=True, methods=['get'])
    def entries(self, request, pk=None):
        """Get leaderboard entries for a team"""
        leaderboard = self.get_object()
        entries = leaderboard.entries.all()
        serializer = LeaderboardEntrySerializer(entries, many=True)
        return Response(serializer.data)


class LeaderboardEntryViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint for leaderboard entries.
    View individual leaderboard standings.
    """
    queryset = LeaderboardEntry.objects.all()
    serializer_class = LeaderboardEntrySerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['leaderboard', 'user']
    ordering_fields = ['rank', 'points', 'activities_count']
    ordering = ['rank']
