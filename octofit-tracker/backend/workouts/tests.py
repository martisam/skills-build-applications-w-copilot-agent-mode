from django.test import TestCase
from django.contrib.auth.models import User
from .models import Workout, WorkoutPlan, WorkoutPlanDay


class WorkoutTestCase(TestCase):
    """Test cases for Workout model"""
    
    def setUp(self):
        """Set up test workout"""
        self.workout = Workout.objects.create(
            title='Morning Run',
            description='A refreshing morning run',
            category='cardio',
            difficulty='beginner',
            estimated_duration_minutes=30,
            estimated_calories=300,
            instructions='Warm up and run at steady pace'
        )
    
    def test_workout_creation(self):
        """Test that a workout can be created"""
        self.assertEqual(self.workout.title, 'Morning Run')
        self.assertEqual(self.workout.category, 'cardio')
        self.assertEqual(self.workout.difficulty, 'beginner')
    
    def test_workout_string_representation(self):
        """Test the string representation of a workout"""
        self.assertEqual(str(self.workout), 'Morning Run')


class WorkoutPlanTestCase(TestCase):
    """Test cases for WorkoutPlan model"""
    
    def setUp(self):
        """Set up test user and workout plan"""
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        self.workout = Workout.objects.create(
            title='Test Workout',
            description='A test workout',
            category='cardio',
            difficulty='beginner',
            estimated_duration_minutes=30,
            instructions='Test instructions'
        )
        self.plan = WorkoutPlan.objects.create(
            user=self.user,
            name='Weekly Plan',
            duration_days=7,
            difficulty_level='beginner'
        )
    
    def test_workout_plan_creation(self):
        """Test that a workout plan can be created"""
        self.assertEqual(self.plan.user, self.user)
        self.assertEqual(self.plan.name, 'Weekly Plan')
        self.assertEqual(self.plan.duration_days, 7)
    
    def test_workout_plan_string_representation(self):
        """Test the string representation of a workout plan"""
        self.assertIn('Weekly Plan', str(self.plan))
        self.assertIn('testuser', str(self.plan))


class WorkoutPlanDayTestCase(TestCase):
    """Test cases for WorkoutPlanDay model"""
    
    def setUp(self):
        """Set up test plan day"""
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        self.workout = Workout.objects.create(
            title='Test Workout',
            description='A test workout',
            category='cardio',
            difficulty='beginner',
            estimated_duration_minutes=30,
            instructions='Test instructions'
        )
        self.plan = WorkoutPlan.objects.create(
            user=self.user,
            name='Weekly Plan',
            duration_days=7
        )
        self.plan_day = WorkoutPlanDay.objects.create(
            workout_plan=self.plan,
            workout=self.workout,
            day_number=1
        )
    
    def test_plan_day_creation(self):
        """Test that a plan day can be created"""
        self.assertEqual(self.plan_day.workout_plan, self.plan)
        self.assertEqual(self.plan_day.day_number, 1)
        self.assertFalse(self.plan_day.is_rest_day)
    
    def test_plan_day_string_representation(self):
        """Test the string representation of a plan day"""
        self.assertIn('Weekly Plan', str(self.plan_day))
        self.assertIn('Day 1', str(self.plan_day))
