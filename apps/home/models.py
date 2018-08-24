from django.db import models
from apps.login_reg.models import *


class openMatches(models.Model):
    creator = models.ForeignKey(User, related_name = "creator_game_id", on_delete=models.CASCADE)
    attendee = models.ForeignKey(User, related_name = "attendee_game_id", on_delete=models.CASCADE)
    difficulty = models.IntegerField(default = 1)
    board = models.CharField(max_length = 2000, default ="")
    scoreboard = models.CharField(max_length = 2000, default = "0,0,0,0,0,0,0,0,0")
    playersTurn = models.IntegerField(default=1, max_length=2)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
