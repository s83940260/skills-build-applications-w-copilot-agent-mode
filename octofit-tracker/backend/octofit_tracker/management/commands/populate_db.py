from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models

class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    class Meta:
        app_label = 'octofit_tracker'

class Activity(models.Model):
    user = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    duration = models.IntegerField()
    class Meta:
        app_label = 'octofit_tracker'

class Leaderboard(models.Model):
    user = models.CharField(max_length=100)
    points = models.IntegerField()
    class Meta:
        app_label = 'octofit_tracker'

class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    class Meta:
        app_label = 'octofit_tracker'

User = get_user_model()

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create users
        users = [
            {'username': 'ironman', 'email': 'ironman@marvel.com', 'team': marvel},
            {'username': 'spiderman', 'email': 'spiderman@marvel.com', 'team': marvel},
            {'username': 'batman', 'email': 'batman@dc.com', 'team': dc},
            {'username': 'superman', 'email': 'superman@dc.com', 'team': dc},
        ]
        user_objs = []
        for u in users:
            user = User.objects.create_user(username=u['username'], email=u['email'], password='password')
            user_objs.append(user)

        # Create activities
        Activity.objects.create(user='ironman', type='run', duration=30)
        Activity.objects.create(user='spiderman', type='cycle', duration=45)
        Activity.objects.create(user='batman', type='swim', duration=60)
        Activity.objects.create(user='superman', type='run', duration=50)

        # Create leaderboard
        Leaderboard.objects.create(user='ironman', points=100)
        Leaderboard.objects.create(user='spiderman', points=80)
        Leaderboard.objects.create(user='batman', points=90)
        Leaderboard.objects.create(user='superman', points=110)

        # Create workouts
        Workout.objects.create(name='Morning Cardio', description='A quick morning run and stretch.')
        Workout.objects.create(name='Strength Training', description='Pushups, squats, and weights.')

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
