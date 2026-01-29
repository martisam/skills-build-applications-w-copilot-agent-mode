from django.contrib import admin
from .models import Workout, WorkoutPlan, WorkoutPlanDay


class WorkoutPlanDayInline(admin.TabularInline):
    model = WorkoutPlanDay
    extra = 1


@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'difficulty', 'estimated_duration_minutes')
    list_filter = ('category', 'difficulty', 'created_at')
    search_fields = ('title', 'description')
    readonly_fields = ('created_at', 'updated_at')


@admin.register(WorkoutPlan)
class WorkoutPlanAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'difficulty_level', 'duration_days', 'is_active')
    list_filter = ('difficulty_level', 'is_active', 'created_at')
    search_fields = ('user__username', 'name')
    readonly_fields = ('created_at', 'updated_at')
    inlines = [WorkoutPlanDayInline]


@admin.register(WorkoutPlanDay)
class WorkoutPlanDayAdmin(admin.ModelAdmin):
    list_display = ('workout_plan', 'day_number', 'workout', 'is_rest_day')
    list_filter = ('is_rest_day',)
    search_fields = ('workout_plan__name', 'workout__title')
