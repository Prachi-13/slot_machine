from django.test import TestCase
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from django.test import Client
from django.urls import reverse
from account.models import UserProfile
from game_session.models import GameSession

# Create your tests here.
User = get_user_model()


class GameSessionModelTestCase(TestCase):
    TEST_GAME_PLAYER = "Test game Player"
    TEST_GUEST_PLAYER = "Test Guest Player12345"

    def create_game_session(self, player_name, is_guest=True, credits=None, user=None):
        if credits is None:
            credits = 10
        if user is not None:
            is_guest = False
        return GameSession(
            user=user, player_name=player_name, is_guest=is_guest, credits=credits
        )

    def test_game_session_creation(self):
        user = User.objects.create(username=self.TEST_GAME_PLAYER)
        session = self.create_game_session(user=user, player_name=self.TEST_GAME_PLAYER)
        self.assertEqual(session.__str__(), f"{self.TEST_GAME_PLAYER}'s Game Session")
        self.assertEqual(session.user, user)
        self.assertEqual(session.credits, 10)
        self.assertEqual(session.is_guest, False)

    def test_guest_games_session_creation(self):
        user = User.objects.create(username=self.TEST_GUEST_PLAYER)
        session = self.create_game_session(player_name=self.TEST_GUEST_PLAYER)
        self.assertEqual(session.__str__(), f"Guest game session")
        self.assertEqual(session.user, None)
        self.assertEqual(session.credits, 10)
        self.assertEqual(session.is_guest, True)