from django.contrib import admin
from .models import UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'age', 'fitness_level', 'total_workouts', 'created_at')
    list_filter = ('fitness_level', 'created_at')
    search_fields = ('user__username', 'user__email')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('User', {
            'fields': ('user',)
        }),
        ('Personal Info', {
            'fields': ('bio', 'gender', 'age', 'height_cm', 'weight_kg')
        }),
        ('Fitness Info', {
            'fields': ('fitness_level', 'total_workouts', 'total_activities')
        }),
        ('Social', {
            'fields': ('profile_picture', 'bio_link')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
