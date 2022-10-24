from django.test import TestCase
from django.utils import timezone
from users.models import UserRant


class RantTest(TestCase):

    def setUp(self):
        self.horarioInicio = timezone.now()
        self.horarioFinal = timezone.now()
        self.user_rant = UserRant.objects.create(username='testeUser', password='teste123',
            email='test@teste.com', nomeRant='testeRant', endereco='enderecoRant',
                                                 horarioInicio=self.horarioInicio, horarioFinal=self.horarioFinal,
                                                 tipo='tipoRant')
        self.user_rant.save()

    def tearDown(self):
        self.user_rant.delete()

    def test_rant(self):
        self.assertEqual(self.user_rant.username, 'testeUser')
        self.assertEqual(self.user_rant.tipo, 'tipoRant')
        self.assertEqual(self.user_rant.endereco, 'enderecoRant')
        self.assertEqual(self.user_rant.nomeRant, 'testeRant')
        self.assertEqual(self.user_rant.password, 'teste123')
        self.assertEqual(self.user_rant.email, 'test@teste.com')