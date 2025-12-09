from rest_framework import serializers
from .models import User, Team, Activity, Leaderboard, Workout

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'teams', 'activities', 'leaderboard_entries']

class TeamSerializer(serializers.ModelSerializer):
    members = UserSerializer(many=True, read_only=True)
    class Meta:
        model = Team
        fields = ['id', 'name', 'members']

class ActivitySerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    class Meta:
        model = Activity
        fields = ['id', 'name', 'user']

class LeaderboardSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    class Meta:
        model = Leaderboard
        fields = ['id', 'user', 'score']

class WorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workout
        fields = ['id', 'name', 'difficulty']
