from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from .models import User, Team, Activity, Workout, Leaderboard

class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create_user(username='testuser', password='testpass')
        self.assertEqual(user.username, 'testuser')

class TeamModelTest(TestCase):
    def test_create_team(self):
        user = User.objects.create_user(username='member', password='pass')
        team = Team.objects.create(name='Team A')
        team.members.add(user)
        self.assertEqual(team.name, 'Team A')

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        user = User.objects.create_user(username='activityuser', password='pass')
        activity = Activity.objects.create(user=user, activity_type='Run', duration=30, calories_burned=200, date='2023-01-01')
        self.assertEqual(activity.activity_type, 'Run')

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        user = User.objects.create_user(username='workoutuser', password='pass')
        workout = Workout.objects.create(user=user, name='Morning Routine', description='Pushups and situps', date='2023-01-01')
        self.assertEqual(workout.name, 'Morning Routine')

class LeaderboardModelTest(TestCase):
    def test_create_leaderboard(self):
        user = User.objects.create_user(username='leader', password='pass')
        leaderboard = Leaderboard.objects.create(user=user, score=100, rank=1)
        self.assertEqual(leaderboard.rank, 1)

class APIRootTest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_api_root(self):
        response = self.client.get(reverse('api-root'))
        self.assertEqual(response.status_code, 200)
