from django.test import TestCase

# Create your tests here.
from django.utils import timezone
from users.models import UserRant


class RantTest(TestCase):

    def setUp(self):
        self.horarioInicio = timezone.now()
        self.horarioFinal = timezone.now()
        # creating user rant
        self.user_rant = UserRant.objects.create(username='test_user', password='testing',
                                                 email='test@example.com', nomeRant='testing', endereco='testing',
                                                 horarioInicio=self.horarioInicio, horarioFinal=self.horarioFinal,
                                                 tipo='testing')
        self.user_rant.save()

    def tearDown(self):
        self.user_rant.delete()

    def test_read_rant(self):
        self.assertEqual(self.user_rant.username, 'test_user')
        self.assertEqual(self.user_rant.tipo, 'testing')
