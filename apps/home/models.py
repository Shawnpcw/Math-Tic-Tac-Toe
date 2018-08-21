from django.db import models
from apps.login_reg.models import *

class Game(models.Model):
    player1 = models.ForeignKey(User, related_name='player1game', on_delete=models.CASCADE)
    player2 = models.ForeignKey(User, related_name='player2game', on_delete= models.CASCADE)
    winner = models.CharField(max_length=255)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

class openMatches(models.Model):
    creator = models.ForeignKey(User, related_name = "user_id", on_delete=models.CASCADE)
    Attendee = models.ManyToManyField(User, related_name = "game_id")
    diffiliculty = models.IntegerField(default = 1)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
