from django.db import models
from django.contrib.auth.models import User


class Workout(models.Model):
    """Personalized workout suggestions model"""
    DIFFICULTY_LEVELS = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    ]
    
    WORKOUT_CATEGORIES = [
        ('cardio', 'Cardio'),
        ('strength', 'Strength Training'),
        ('flexibility', 'Flexibility/Yoga'),
        ('hiit', 'HIIT'),
        ('sports', 'Sports'),
        ('mixed', 'Mixed Training'),
    ]
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=WORKOUT_CATEGORIES)
    difficulty = models.CharField(max_length=20, choices=DIFFICULTY_LEVELS, default='beginner')
    estimated_duration_minutes = models.IntegerField()
    estimated_calories = models.FloatField(null=True, blank=True)
    instructions = models.TextField()
    equipment_needed = models.CharField(max_length=500, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['difficulty', 'category']),
        ]
    
    def __str__(self):
        return self.title


class WorkoutPlan(models.Model):
    """Personalized workout plans for users"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='workout_plans')
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    workouts = models.ManyToManyField(Workout, related_name='plans', through='WorkoutPlanDay')
    duration_days = models.IntegerField()
    difficulty_level = models.CharField(
        max_length=20,
        choices=[('beginner', 'Beginner'), ('intermediate', 'Intermediate'), ('advanced', 'Advanced')],
        default='beginner'
    )
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.user.username}'s {self.name}"


class WorkoutPlanDay(models.Model):
    """Daily workout assignments in a plan"""
    workout_plan = models.ForeignKey(WorkoutPlan, on_delete=models.CASCADE, related_name='days')
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE)
    day_number = models.IntegerField()
    is_rest_day = models.BooleanField(default=False)
    notes = models.TextField(blank=True)
    
    class Meta:
        unique_together = ('workout_plan', 'day_number')
        ordering = ['day_number']
    
    def __str__(self):
        return f"{self.workout_plan.name} - Day {self.day_number}"
