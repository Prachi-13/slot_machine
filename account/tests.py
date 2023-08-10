from django.test import TestCase
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from django.test import Client
from django.urls import reverse
from account.models import UserProfile
# Create your tests here.
User = get_user_model()


class UserProfileModelTestCase(TestCase):
    TEST_USER_USERNAME = "testuser"
    TEST_USER_PASSWORD = "testpassword"

    @classmethod
    def setUpTestData(self):
        self.user = User.objects.create_user(
            username=self.TEST_USER_USERNAME,
            password=self.TEST_USER_PASSWORD
        )  # will create UserProfile as well using signals

    def create_user(self, username, password):
        return User.objects.create_user(username=username, password=password)

    def get_user(self, username=None):
        try:
            return User.objects.get(username=username)
        except User.DoesNotExist:
            return None

    def test_get_user(self):
        user_not_exists = self.get_user("test")
        test_user = self.get_user(self.TEST_USER_USERNAME)
        self.assertEqual(user_not_exists, None)
        self.assertEqual(test_user, self.user)
        self.assertEqual(test_user.username, self.TEST_USER_USERNAME)

    def test_get_profile(self):
        user_profile = UserProfile.objects.get(user=self.user)
        self.assertEqual(user_profile.user, self.user)
        self.assertEqual(str(user_profile), f"{self.user.username}'s profile")

    def test_default_credits(self):
        test_user_profile_credits = self.user.userprofile.credits
        self.assertEqual(test_user_profile_credits, 0)

