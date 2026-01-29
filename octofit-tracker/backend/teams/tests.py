from django.test import TestCase
from django.contrib.auth.models import User
from .models import Team, TeamMembership, Leaderboard


class TeamTestCase(TestCase):
    """Test cases for Team model"""
    
    def setUp(self):
        """Set up test team and members"""
        self.owner = User.objects.create_user(
            username='owner',
            email='owner@example.com',
            password='testpass123'
        )
        self.member = User.objects.create_user(
            username='member',
            email='member@example.com',
            password='testpass123'
        )
        self.team = Team.objects.create(
            name='Test Team',
            owner=self.owner,
            description='A test team'
        )
        self.team.members.add(self.owner)
        self.team.members.add(self.member)
    
    def test_team_creation(self):
        """Test that a team can be created"""
        self.assertEqual(self.team.name, 'Test Team')
        self.assertEqual(self.team.owner, self.owner)
    
    def test_team_member_count(self):
        """Test the member count property"""
        self.assertEqual(self.team.member_count, 2)
    
    def test_team_string_representation(self):
        """Test the string representation of a team"""
        self.assertEqual(str(self.team), 'Test Team')


class LeaderboardTestCase(TestCase):
    """Test cases for Leaderboard model"""
    
    def setUp(self):
        """Set up test team and leaderboard"""
        self.owner = User.objects.create_user(
            username='owner',
            email='owner@example.com',
            password='testpass123'
        )
        self.team = Team.objects.create(
            name='Test Team',
            owner=self.owner
        )
        self.leaderboard = Leaderboard.objects.create(team=self.team)
    
    def test_leaderboard_creation(self):
        """Test that a leaderboard can be created"""
        self.assertEqual(self.leaderboard.team, self.team)
        self.assertIsNotNone(self.leaderboard.created_at)
    
    def test_leaderboard_string_representation(self):
        """Test the string representation of a leaderboard"""
        self.assertIn('Test Team', str(self.leaderboard))
