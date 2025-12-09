from djongo import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(unique=True)
    REQUIRED_FIELDS = ['email']

class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    members = models.ManyToManyField('User', related_name='teams')
    def __str__(self):
        return self.name

class Activity(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='activities')
    def __str__(self):
        return f"{self.name} ({self.user.username})"

class Leaderboard(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='leaderboard_entries')
    score = models.IntegerField()
    def __str__(self):
        return f"{self.user.username}: {self.score}"

class Workout(models.Model):
    name = models.CharField(max_length=100)
    difficulty = models.CharField(max_length=50)
    def __str__(self):
        return self.name
