from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from djongo import models

# Define models for demonstration (replace with your actual models if they exist)
class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    class Meta:
        app_label = 'octofit_tracker'

class Activity(models.Model):
    name = models.CharField(max_length=100)
    user = models.CharField(max_length=100)
    class Meta:
        app_label = 'octofit_tracker'

class Leaderboard(models.Model):
    user = models.CharField(max_length=100)
    score = models.IntegerField()
    class Meta:
        app_label = 'octofit_tracker'

class Workout(models.Model):
    name = models.CharField(max_length=100)
    difficulty = models.CharField(max_length=50)
    class Meta:
        app_label = 'octofit_tracker'

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create users (super heroes)
        users = [
            User.objects.create_user(username='ironman', email='ironman@marvel.com', password='password'),
            User.objects.create_user(username='spiderman', email='spiderman@marvel.com', password='password'),
            User.objects.create_user(username='batman', email='batman@dc.com', password='password'),
            User.objects.create_user(username='superman', email='superman@dc.com', password='password'),
        ]

        # Create activities
        Activity.objects.create(name='Flight', user='superman')
        Activity.objects.create(name='Martial Arts', user='batman')
        Activity.objects.create(name='Web Swinging', user='spiderman')
        Activity.objects.create(name='Engineering', user='ironman')

        # Create leaderboard
        Leaderboard.objects.create(user='superman', score=100)
        Leaderboard.objects.create(user='batman', score=90)
        Leaderboard.objects.create(user='spiderman', score=80)
        Leaderboard.objects.create(user='ironman', score=70)

        # Create workouts
        Workout.objects.create(name='Strength Training', difficulty='Hard')
        Workout.objects.create(name='Cardio', difficulty='Medium')
        Workout.objects.create(name='Agility', difficulty='Easy')

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
