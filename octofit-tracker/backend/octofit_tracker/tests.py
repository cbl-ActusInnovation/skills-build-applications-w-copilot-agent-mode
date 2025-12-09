from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from .models import User, Team, Activity, Leaderboard, Workout

class ModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='testpass')
        self.team = Team.objects.create(name='Test Team')
        self.team.members.add(self.user)
        self.activity = Activity.objects.create(name='Test Activity', user=self.user)
        self.leaderboard = Leaderboard.objects.create(user=self.user, score=42)
        self.workout = Workout.objects.create(name='Test Workout', difficulty='Easy')

    def test_user_str(self):
        self.assertEqual(str(self.user), 'testuser')

    def test_team_str(self):
        self.assertEqual(str(self.team), 'Test Team')

    def test_activity_str(self):
        self.assertIn('Test Activity', str(self.activity))

    def test_leaderboard_str(self):
        self.assertIn('testuser', str(self.leaderboard))

    def test_workout_str(self):
        self.assertEqual(str(self.workout), 'Test Workout')

class APITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='apitest', email='api@example.com', password='apipass')
        self.team = Team.objects.create(name='API Team')
        self.team.members.add(self.user)
        self.activity = Activity.objects.create(name='API Activity', user=self.user)
        self.leaderboard = Leaderboard.objects.create(user=self.user, score=99)
        self.workout = Workout.objects.create(name='API Workout', difficulty='Medium')

    def test_api_root(self):
        response = self.client.get(reverse('api-root'))
        self.assertEqual(response.status_code, 200)

    def test_users_endpoint(self):
        response = self.client.get('/users/')
        self.assertEqual(response.status_code, 200)

    def test_teams_endpoint(self):
        response = self.client.get('/teams/')
        self.assertEqual(response.status_code, 200)

    def test_activities_endpoint(self):
        response = self.client.get('/activities/')
        self.assertEqual(response.status_code, 200)

    def test_leaderboard_endpoint(self):
        response = self.client.get('/leaderboard/')
        self.assertEqual(response.status_code, 200)

    def test_workouts_endpoint(self):
        response = self.client.get('/workouts/')
        self.assertEqual(response.status_code, 200)
