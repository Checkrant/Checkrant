from django.contrib.auth import get_user_model
from django.test import TestCase

# Create your tests here.
from django.utils import timezone

from comment.forms import CommentForm
from comment.models import Comment


class CommentTest(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(username='test_user', password='testing',
                                                         email='test@example.com')
        self.user.save()
        self.date = timezone.now()
        self.comment = Comment(user=self.user, content='description of the comment',
                               data=self.date)
        self.comment.save()

    def tearDown(self):
        self.user.delete()

    def test_read_comment(self):
        self.assertEqual(self.comment.user, self.user)
        self.assertEqual(self.comment.content, 'description of the comment')
        self.assertEqual(self.comment.data, self.date)

    def test_update_comment_content(self):
        self.comment.description = 'new description'
        self.comment.save()
        self.assertEqual(self.comment.description, 'new description')

    def test_valid_form(self):
        comment = Comment.objects.create(content='content', user=self.user, data=self.date)
        data = {'content': comment.content, 'user': comment.user, 'data': comment.data}
        form = CommentForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        # trying to save data without date
        comment = Comment.objects.create(content='content', user=self.user, data=self.date)
        data = {'content': comment.content, 'user': comment.user}
        form = CommentForm(data=data)
        self.assertFalse(form.is_valid())