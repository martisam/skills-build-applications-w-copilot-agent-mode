from django.test import TestCase
from django.contrib.auth.models import User
from django.utils import timezone
from .models import Activity


class ActivityTestCase(TestCase):
    """Test cases for Activity model"""
    
    def setUp(self):
        """Set up test user and activity"""
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        self.activity = Activity.objects.create(
            user=self.user,
            activity_type='running',
            title='Morning Run',
            duration_minutes=30,
            calories_burned=300,
            activity_date=timezone.now()
        )
    
    def test_activity_creation(self):
        """Test that an activity can be created"""
        self.assertEqual(self.activity.user.username, 'testuser')
        self.assertEqual(self.activity.activity_type, 'running')
        self.assertEqual(self.activity.duration_minutes, 30)
    
    def test_activity_string_representation(self):
        """Test the string representation of an activity"""
        self.assertIn('testuser', str(self.activity))
        self.assertIn('running', str(self.activity))
    
    def test_activity_ordering(self):
        """Test that activities are ordered by date"""
        recent_activity = Activity.objects.create(
            user=self.user,
            activity_type='cycling',
            title='Evening Ride',
            duration_minutes=60,
            activity_date=timezone.now()
        )
        activities = Activity.objects.all()
        self.assertEqual(activities[0].id, recent_activity.id)
