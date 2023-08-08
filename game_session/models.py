from django.db import models
from django.conf import settings

# Create your models here.
class GameSession(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.CASCADE)
    is_guest = models.BooleanField(default=False)
    player_name = models.CharField(max_length=100)
    credits = models.IntegerField(default=10)
    game_state = models.CharField(max_length=100, default="")

    def __str__(self):
        if self.is_guest:
            return f"Guest game session"
        return f"{self.user}'s Game Session"

