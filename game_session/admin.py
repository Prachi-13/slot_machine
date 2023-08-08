from django.contrib import admin
from .models import GameSession
# Register your models here.

@admin.register(GameSession)
class GameSessionAdmin(admin.ModelAdmin):
    pass