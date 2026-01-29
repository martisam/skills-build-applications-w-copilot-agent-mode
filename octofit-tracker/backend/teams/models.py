from django.db import models
from django.contrib.auth.models import User


class Team(models.Model):
    """Team model for competitive fitness challenges"""
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField(blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owned_teams')
    members = models.ManyToManyField(User, related_name='teams', through='TeamMembership')
    logo_url = models.URLField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return self.name
    
    @property
    def member_count(self):
        return self.members.count()


class TeamMembership(models.Model):
    """Through model for Team members with roles"""
    ROLE_CHOICES = [
        ('owner', 'Owner'),
        ('admin', 'Admin'),
        ('member', 'Member'),
    ]
    
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='member')
    joined_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('team', 'user')
        ordering = ['-joined_at']
    
    def __str__(self):
        return f"{self.user.username} - {self.team.name} ({self.role})"


class Leaderboard(models.Model):
    """Leaderboard for team competitions"""
    team = models.OneToOneField(Team, on_delete=models.CASCADE, related_name='leaderboard')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Leaderboard for {self.team.name}"


class LeaderboardEntry(models.Model):
    """Individual leaderboard entries for team members"""
    leaderboard = models.ForeignKey(Leaderboard, on_delete=models.CASCADE, related_name='entries')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rank = models.IntegerField()
    points = models.IntegerField(default=0)
    activities_count = models.IntegerField(default=0)
    total_duration_minutes = models.IntegerField(default=0)
    total_calories_burned = models.FloatField(default=0)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        unique_together = ('leaderboard', 'user')
        ordering = ['rank']
    
    def __str__(self):
        return f"{self.user.username} - Rank {self.rank}"
