from unittest import TestCase

from django.contrib.auth import authenticate, get_user_model
from django.db import IntegrityError


class AccountsTesting(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(username='test_user_1', password='testing',
                                                         email='test@example.com')
        self.user.save()

    def tearDown(self):
        self.user.delete()

    def test_correct_credentials(self):
        user = authenticate(username='test_user_1', password='testing')
        self.assertTrue((user is not None) and user.is_authenticated)

    def test_wrong_username(self):
        user = authenticate(username='test_user123', password='testing')
        self.assertFalse(user is not None and user.is_authenticated)

    def test_wrong_password(self):
        user = authenticate(username='test_user_1', password='wrong')
        self.assertFalse(user is not None and user.is_authenticated)

    def test_no_username_provided(self):
        self.assertRaises(ValueError, get_user_model().objects.create_user, username='', email='testing@gmail.com',
                          password='password')

    def test_duplicate_username(self):
        self.assertRaises(IntegrityError, get_user_model().objects.create_user,
                          username='test_user_1', email='testing@gmail.com', password='password')
