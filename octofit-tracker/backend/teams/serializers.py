from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Team, TeamMembership, Leaderboard, LeaderboardEntry


class UserSimpleSerializer(serializers.ModelSerializer):
    """Simplified user serializer for nested data"""
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email']


class TeamMembershipSerializer(serializers.ModelSerializer):
    """Serializer for TeamMembership model"""
    user = UserSimpleSerializer(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        write_only=True,
        source='user'
    )
    
    class Meta:
        model = TeamMembership
        fields = ['id', 'team', 'user', 'user_id', 'role', 'joined_at']
        read_only_fields = ['id', 'joined_at']


class TeamSerializer(serializers.ModelSerializer):
    """Serializer for Team model"""
    owner = UserSimpleSerializer(read_only=True)
    owner_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        write_only=True,
        source='owner'
    )
    members = UserSimpleSerializer(many=True, read_only=True)
    member_count = serializers.SerializerMethodField()
    
    class Meta:
        model = Team
        fields = [
            'id', 'name', 'description', 'owner', 'owner_id', 'members',
            'member_count', 'logo_url', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at', 'members']
    
    def get_member_count(self, obj):
        return obj.members.count()


class LeaderboardEntrySerializer(serializers.ModelSerializer):
    """Serializer for LeaderboardEntry model"""
    user = UserSimpleSerializer(read_only=True)
    
    class Meta:
        model = LeaderboardEntry
        fields = [
            'id', 'leaderboard', 'user', 'rank', 'points',
            'activities_count', 'total_duration_minutes',
            'total_calories_burned', 'updated_at'
        ]
        read_only_fields = ['id', 'updated_at']


class LeaderboardSerializer(serializers.ModelSerializer):
    """Serializer for Leaderboard model"""
    entries = LeaderboardEntrySerializer(many=True, read_only=True, source='entries')
    team_name = serializers.CharField(source='team.name', read_only=True)
    
    class Meta:
        model = Leaderboard
        fields = ['id', 'team', 'team_name', 'entries', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']
