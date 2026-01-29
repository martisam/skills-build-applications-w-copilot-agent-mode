from django.contrib import admin
from .models import Activity


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('user', 'activity_type', 'activity_date', 'duration_minutes', 'calories_burned')
    list_filter = ('activity_type', 'intensity', 'activity_date')
    search_fields = ('user__username', 'title', 'location')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('User', {
            'fields': ('user',)
        }),
        ('Activity Info', {
            'fields': ('activity_type', 'title', 'description')
        }),
        ('Metrics', {
            'fields': ('duration_minutes', 'calories_burned', 'distance_km', 'intensity')
        }),
        ('Location & Date', {
            'fields': ('location', 'activity_date')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
