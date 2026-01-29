from django.test import TestCase
from django.contrib.auth.models import User
from .models import UserProfile


class UserProfileTestCase(TestCase):
    """Test cases for UserProfile model"""
    
    def setUp(self):
        """Set up test user and profile"""
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        self.profile = UserProfile.objects.create(
            user=self.user,
            age=30,
            height_cm=180,
            weight_kg=75,
            fitness_level='intermediate'
        )
    
    def test_profile_creation(self):
        """Test that a profile can be created"""
        self.assertEqual(self.profile.user.username, 'testuser')
        self.assertEqual(self.profile.age, 30)
    
    def test_profile_string_representation(self):
        """Test the string representation of a profile"""
        expected = "testuser's Profile"
        self.assertEqual(str(self.profile), expected)
    
    def test_profile_defaults(self):
        """Test default values for a new profile"""
        self.assertEqual(self.profile.total_workouts, 0)
        self.assertEqual(self.profile.total_activities, 0)
