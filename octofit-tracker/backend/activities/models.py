from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator


class Activity(models.Model):
    """User activity/exercise logging model"""
    ACTIVITY_TYPES = [
        ('running', 'Running'),
        ('cycling', 'Cycling'),
        ('swimming', 'Swimming'),
        ('walking', 'Walking'),
        ('gym', 'Gym/Strength'),
        ('yoga', 'Yoga'),
        ('sports', 'Sports'),
        ('hiking', 'Hiking'),
        ('other', 'Other'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='activities')
    activity_type = models.CharField(max_length=20, choices=ACTIVITY_TYPES)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    duration_minutes = models.IntegerField(validators=[MinValueValidator(1)])
    calories_burned = models.FloatField(null=True, blank=True, validators=[MinValueValidator(0)])
    distance_km = models.FloatField(null=True, blank=True, help_text="Distance covered in kilometers")
    intensity = models.CharField(
        max_length=20,
        choices=[('low', 'Low'), ('moderate', 'Moderate'), ('high', 'High')],
        default='moderate'
    )
    location = models.CharField(max_length=200, blank=True)
    activity_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-activity_date']
        indexes = [
            models.Index(fields=['user', '-activity_date']),
            models.Index(fields=['activity_type']),
        ]
    
    def __str__(self):
        return f"{self.user.username} - {self.activity_type} on {self.activity_date.date()}"
