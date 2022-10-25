from django.contrib.auth import get_user_model
from django.test import TestCase
from django.utils import timezone

from comment.forms import CommentForm
from comment.models import Comment


class teste_comentario(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(username='teste_usuario', password='teste123',
                                                         email='teste@exemplo.com')
        self.user.save()
        self.date = timezone.now()
        self.comment = Comment(user=self.user,
                               content='teste do conteudo do comentario',
                               data=self.date)
        self.comment.save()

    def tearDown(self):
        self.user.delete()

    def test_ler_comentario(self):
        self.assertEqual(self.comment.user, self.user)
        self.assertEqual(self.comment.content, 'teste do conteudo do comentario')
        self.assertEqual(self.comment.data, self.date)

    def test_atualizar_comentario(self):
        self.comment.description = 'novo comentario'
        self.comment.save()
        self.assertEqual(self.comment.description, 'novo comentario')

    def test_valid_form(self):
        comment = Comment.objects.create(content='content', user=self.user, data=self.date)
        data = {'content': comment.content, 'user': comment.user, 'data': comment.data}
        form = CommentForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        comment = Comment.objects.create(content='content', user=self.user, data=self.date)
        data = {'content': comment.content, 'user': comment.user}
        form = CommentForm(data=data)
        self.assertFalse(form.is_valid())
