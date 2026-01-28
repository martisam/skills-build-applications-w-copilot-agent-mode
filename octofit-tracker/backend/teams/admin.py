from django.contrib import admin
from .models import Team, TeamMembership, Leaderboard, LeaderboardEntry


class TeamMembershipInline(admin.TabularInline):
    model = TeamMembership
    extra = 1


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'member_count', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'owner__username')
    readonly_fields = ('created_at', 'updated_at')
    inlines = [TeamMembershipInline]


@admin.register(TeamMembership)
class TeamMembershipAdmin(admin.ModelAdmin):
    list_display = ('user', 'team', 'role', 'joined_at')
    list_filter = ('role', 'joined_at')
    search_fields = ('user__username', 'team__name')


@admin.register(Leaderboard)
class LeaderboardAdmin(admin.ModelAdmin):
    list_display = ('team', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')


@admin.register(LeaderboardEntry)
class LeaderboardEntryAdmin(admin.ModelAdmin):
    list_display = ('user', 'leaderboard', 'rank', 'points', 'activities_count')
    list_filter = ('leaderboard', 'rank')
    search_fields = ('user__username',)
    readonly_fields = ('updated_at',)
