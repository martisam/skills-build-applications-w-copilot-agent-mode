from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from users.models import UserProfile
from activities.models import Activity
from teams.models import Team, TeamMembership, Leaderboard, LeaderboardEntry
from workouts.models import Workout, WorkoutPlan, WorkoutPlanDay
from datetime import datetime, timedelta
from django.utils import timezone
import random


class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear existing data
        self.stdout.write('Clearing existing data...')
        User.objects.all().delete()
        UserProfile.objects.all().delete()
        Activity.objects.all().delete()
        Team.objects.all().delete()
        TeamMembership.objects.all().delete()
        Leaderboard.objects.all().delete()
        LeaderboardEntry.objects.all().delete()
        Workout.objects.all().delete()
        WorkoutPlan.objects.all().delete()
        WorkoutPlanDay.objects.all().delete()
        
        self.stdout.write('Starting database population...')
        
        # Create sample users (Superheroes)
        users = self.create_superhero_users()
        self.stdout.write(self.style.SUCCESS(f'✓ Created {len(users)} superhero users'))
        
        # Create user profiles
        profiles = self.create_user_profiles(users)
        self.stdout.write(self.style.SUCCESS(f'✓ Created {len(profiles)} user profiles'))
        
        # Create sample activities
        activities = self.create_activities(users)
        self.stdout.write(self.style.SUCCESS(f'✓ Created {len(activities)} activities'))
        
        # Create sample workouts
        workouts = self.create_workouts()
        self.stdout.write(self.style.SUCCESS(f'✓ Created {len(workouts)} workout templates'))
        
        # Create teams (Marvel and DC)
        teams = self.create_superhero_teams(users)
        self.stdout.write(self.style.SUCCESS(f'✓ Created {len(teams)} teams'))
        
        # Create leaderboards
        leaderboards = self.create_leaderboards(teams, users, activities)
        self.stdout.write(self.style.SUCCESS(f'✓ Created {len(leaderboards)} leaderboards'))
        
        # Create workout plans
        plans = self.create_workout_plans(users, workouts)
        self.stdout.write(self.style.SUCCESS(f'✓ Created {len(plans)} workout plans'))
        
        self.stdout.write(self.style.SUCCESS('\n✓ Database population completed successfully!'))

    def create_superhero_users(self):
        """Create sample superhero users"""
        superhero_data = [
            # Marvel Heroes
            {'username': 'iron_man', 'email': 'tony@marvel.com', 'first_name': 'Tony', 'last_name': 'Stark'},
            {'username': 'captain_america', 'email': 'steve@marvel.com', 'first_name': 'Steve', 'last_name': 'Rogers'},
            {'username': 'spider_man', 'email': 'peter@marvel.com', 'first_name': 'Peter', 'last_name': 'Parker'},
            {'username': 'black_widow', 'email': 'natasha@marvel.com', 'first_name': 'Natasha', 'last_name': 'Romanoff'},
            # DC Heroes
            {'username': 'batman', 'email': 'bruce@dc.com', 'first_name': 'Bruce', 'last_name': 'Wayne'},
            {'username': 'superman', 'email': 'clark@dc.com', 'first_name': 'Clark', 'last_name': 'Kent'},
            {'username': 'wonder_woman', 'email': 'diana@dc.com', 'first_name': 'Diana', 'last_name': 'Prince'},
            {'username': 'the_flash', 'email': 'barry@dc.com', 'first_name': 'Barry', 'last_name': 'Allen'},
        ]
        
        users = []
        for user_data in superhero_data:
            user, created = User.objects.get_or_create(
                username=user_data['username'],
                defaults={
                    'email': user_data['email'],
                    'first_name': user_data['first_name'],
                    'last_name': user_data['last_name'],
                }
            )
            if created:
                user.set_password('testpass123')
                user.save()
            users.append(user)
        
        return users

    def create_user_profiles(self, users):
        """Create user profiles"""
        profiles = []
        fitness_levels = ['beginner', 'intermediate', 'advanced']
        genders = ['M', 'F', 'O']
        
        for user in users:
            profile, created = UserProfile.objects.get_or_create(
                user=user,
                defaults={
                    'bio': f'Fitness enthusiast - {user.first_name}',
                    'gender': random.choice(genders),
                    'age': random.randint(18, 65),
                    'height_cm': random.randint(150, 200),
                    'weight_kg': random.randint(50, 100),
                    'fitness_level': random.choice(fitness_levels),
                    'total_workouts': random.randint(0, 50),
                    'total_activities': random.randint(0, 100),
                }
            )
            profiles.append(profile)
        
        return profiles

    def create_activities(self, users):
        """Create sample activities"""
        activities = []
        activity_types = ['running', 'cycling', 'swimming', 'walking', 'gym', 'yoga', 'sports', 'hiking']
        
        for user in users:
            for i in range(random.randint(5, 15)):
                activity_date = timezone.now() - timedelta(days=random.randint(0, 30))
                activity = Activity.objects.create(
                    user=user,
                    activity_type=random.choice(activity_types),
                    title=f'{user.first_name} - Activity {i+1}',
                    description=f'A great workout session',
                    duration_minutes=random.randint(15, 120),
                    calories_burned=random.randint(100, 800),
                    distance_km=round(random.uniform(1, 20), 2),
                    intensity=random.choice(['low', 'moderate', 'high']),
                    location=random.choice(['Park', 'Gym', 'Home', 'Beach', 'Trail']),
                    activity_date=activity_date,
                )
                activities.append(activity)
        
        return activities

    def create_workouts(self):
        """Create sample workout templates"""
        workouts_data = [
            {
                'title': 'Morning Run',
                'description': 'A refreshing morning run to start the day',
                'category': 'cardio',
                'difficulty': 'beginner',
                'estimated_duration_minutes': 30,
                'estimated_calories': 300,
                'instructions': 'Warm up for 5 minutes, then run at a steady pace for 25 minutes.',
                'equipment_needed': 'Running shoes',
            },
            {
                'title': 'Strength Training Session',
                'description': 'Full body strength workout',
                'category': 'strength',
                'difficulty': 'intermediate',
                'estimated_duration_minutes': 60,
                'estimated_calories': 400,
                'instructions': 'Perform 3 sets of various exercises targeting all major muscle groups.',
                'equipment_needed': 'Dumbbells, Barbell, Bench',
            },
            {
                'title': 'Yoga Flow',
                'description': 'Relaxing yoga session for flexibility',
                'category': 'flexibility',
                'difficulty': 'beginner',
                'estimated_duration_minutes': 45,
                'estimated_calories': 150,
                'instructions': 'Follow a guided yoga sequence focusing on flexibility and mindfulness.',
                'equipment_needed': 'Yoga Mat',
            },
            {
                'title': 'HIIT Workout',
                'description': 'High Intensity Interval Training',
                'category': 'hiit',
                'difficulty': 'advanced',
                'estimated_duration_minutes': 30,
                'estimated_calories': 500,
                'instructions': 'Perform 30 seconds of high intensity exercise followed by 30 seconds rest.',
                'equipment_needed': 'None',
            },
            {
                'title': 'Cycling Adventure',
                'description': 'Outdoor cycling session',
                'category': 'cardio',
                'difficulty': 'intermediate',
                'estimated_duration_minutes': 90,
                'estimated_calories': 600,
                'instructions': 'Ride on varying terrain at a comfortable pace.',
                'equipment_needed': 'Bicycle',
            },
            {
                'title': 'Swimming Session',
                'description': 'Pool workout combining different strokes',
                'category': 'cardio',
                'difficulty': 'intermediate',
                'estimated_duration_minutes': 45,
                'estimated_calories': 350,
                'instructions': 'Practice different swimming strokes for full body conditioning.',
                'equipment_needed': 'Swimming Pool, Swimsuit',
            },
        ]
        
        workouts = []
        for workout_data in workouts_data:
            workout, created = Workout.objects.get_or_create(
                title=workout_data['title'],
                defaults=workout_data
            )
            workouts.append(workout)
        
        return workouts

    def create_superhero_teams(self, users):
        """Create Marvel and DC teams"""
        teams_data = [
            {'name': 'marvel', 'owner': users[0], 'description': 'Marvel Universe Superheroes'},
            {'name': 'dc', 'owner': users[4], 'description': 'DC Universe Superheroes'},
        ]
        
        teams = []
        for team_data in teams_data:
            team, created = Team.objects.get_or_create(
                name=team_data['name'],
                defaults={
                    'owner': team_data['owner'],
                    'description': team_data['description'],
                }
            )
            
            # Add team members based on universe
            if created:
                if team.name == 'marvel':
                    team_members = users[0:4]  # Iron Man, Captain America, Spider-Man, Black Widow
                else:  # dc
                    team_members = users[4:8]  # Batman, Superman, Wonder Woman, The Flash
                
                for member in team_members:
                    role = 'owner' if member == team.owner else 'member'
                    TeamMembership.objects.get_or_create(
                        team=team,
                        user=member,
                        defaults={'role': role}
                    )
            
            teams.append(team)
        
        return teams

    def create_leaderboards(self, teams, users, activities):
        """Create leaderboards for teams"""
        leaderboards = []
        
        for team in teams:
            leaderboard, created = Leaderboard.objects.get_or_create(team=team)
            
            # Create leaderboard entries
            if created:
                members = team.members.all()
                for rank, member in enumerate(members, 1):
                    member_activities = activities.filter(user=member)
                    total_duration = sum(a.duration_minutes for a in member_activities)
                    total_calories = sum(a.calories_burned or 0 for a in member_activities)
                    
                    LeaderboardEntry.objects.create(
                        leaderboard=leaderboard,
                        user=member,
                        rank=rank,
                        points=rank * 100,
                        activities_count=member_activities.count(),
                        total_duration_minutes=total_duration,
                        total_calories_burned=total_calories,
                    )
            
            leaderboards.append(leaderboard)
        
        return leaderboards

    def create_workout_plans(self, users, workouts):
        """Create personalized workout plans"""
        plans = []
        
        for user in users:
            plan = WorkoutPlan.objects.create(
                user=user,
                name=f'{user.first_name}\'s Weekly Plan',
                description=f'Custom workout plan for {user.first_name}',
                duration_days=7,
                difficulty_level=random.choice(['beginner', 'intermediate', 'advanced']),
                is_active=True,
            )
            
            # Add workouts to plan
            selected_workouts = random.sample(list(workouts), k=min(5, len(workouts)))
            for day, workout in enumerate(selected_workouts, 1):
                WorkoutPlanDay.objects.create(
                    workout_plan=plan,
                    workout=workout,
                    day_number=day,
                    is_rest_day=False,
                )
            
            # Add rest days
            for day in range(len(selected_workouts) + 1, 8):
                WorkoutPlanDay.objects.create(
                    workout_plan=plan,
                    workout=workouts[0],
                    day_number=day,
                    is_rest_day=True,
                )
            
            plans.append(plan)
        
        return plans
