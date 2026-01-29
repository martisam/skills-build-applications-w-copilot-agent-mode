from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


class UserProfile(models.Model):
    """Extended user profile for fitness tracking"""
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    
    FITNESS_LEVEL_CHOICES = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
        ('professional', 'Professional'),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(blank=True, null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(1), MaxValueValidator(150)])
    height_cm = models.FloatField(null=True, blank=True, help_text="Height in centimeters")
    weight_kg = models.FloatField(null=True, blank=True, help_text="Weight in kilograms")
    fitness_level = models.CharField(
        max_length=20,
        choices=FITNESS_LEVEL_CHOICES,
        default='beginner',
        help_text="Current fitness level"
    )
    total_workouts = models.IntegerField(default=0)
    total_activities = models.IntegerField(default=0)
    profile_picture = models.URLField(null=True, blank=True)
    bio_link = models.URLField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.user.username}'s Profile"
