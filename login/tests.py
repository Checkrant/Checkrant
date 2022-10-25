from django.test import TestCase

from django.contrib.auth import authenticate, get_user_model
from django.db import IntegrityError


class testeConta(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(username='usuario1', password='teste123',
                                                         email='test@exemplo.com')
        self.user.save()

    def tearDown(self):
        self.user.delete()

    def teste_login_sucesso(self):
        user = authenticate(username='usuario1', password='teste123')
        self.assertTrue((user is not None) and user.is_authenticated)

    def teste_usuario_errado(self):
        user = authenticate(username='test_user123', password='teste123')
        self.assertFalse(user is not None and user.is_authenticated)

    def teste_senha_errada(self):
        user = authenticate(username='usuario1', password='wrong')
        self.assertFalse(user is not None and user.is_authenticated)

    def teste_usuario_nao_existe(self):
        self.assertRaises(ValueError, get_user_model().objects.create_user, username='', email='teste123@gmail.com',
                          password='password')
    def teste_usuario_ja_existe(self):
        user = authenticate(username='usuario1')
        self.assertFalse((user is not None) and user.is_authenticated)

