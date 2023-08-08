from django.db import models

# Create your models here.
class GameSession(models.Model):
    player_name = models.CharField(max_length=100)
    credits = models.IntegerField(default=10)
    game_state = models.CharField(max_length=100, default="")

    def __str__(self):
        return f"{self.player_name}'s Game Session"
