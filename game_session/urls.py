from django.urls import path
from . import views

urlpatterns = [
    path('', views.slot_machine, name='slot_machine'),
    path('pull_lever/', views.pull_lever, name='pull_lever'),
    path('cash_out/', views.cash_out, name='cash_out'),
    path('game_over/', views.game_over, name='game_over'),
]
