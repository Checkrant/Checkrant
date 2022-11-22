from django.test import TestCase
from django.utils import timezone
from django.contrib.auth import authenticate, get_user_model
from publication.models import Restaurant 
from publication.models import Review
from users.models import UserRant

class RestaurantTest(TestCase):

    def setUp(self):
        self.rest = Restaurant.objects.create(restaurant_name='nomeRestaurante',food_type='testeComida')
        self.rest.save()

    def tearDown(self):
        self.rest.delete()

    def teste_rate(self):
        self.assertEqual(self.rest.restaurant_name, 'nomeRestaurante')
        self.assertEqual(self.rest.food_type, 'testeComida')

class ReviewTest(TestCase):

    def setUp(self):
        UserRant.objects.create(username='testeUser', password='teste123', email='test@teste.com', nomeRant='testeRant', endereco='enderecoRant', horarioInicio='10:00', horarioFinal='11:00',
                                tipo='tipoRant')
        self.rev = Review.objects.create(writer='nomeAvaliador', pub_date='2022-11-21 18:30', stars=5, detail='Muito Bom', restaurant=UserRant.objects.get(nomeRant = 'testeRant'))
        self.rev.save()
        self.user = get_user_model().objects.create_user(username='usuario2', password='teste1234', email='test@test.com')
        self.user.save()

    def tearDown(self):
        self.rev.delete()
        self.user.delete()

    def teste_review(self):
        self.assertEqual(self.rev.writer, 'nomeAvaliador')
        self.assertEqual(self.rev.stars, 5)
        self.assertEqual(self.rev.detail, 'Muito Bom')
        self.assertEqual(self.rev.restaurant, UserRant.objects.get(nomeRant = 'testeRant'))

    def like_test(self):
        self.rev.users_likes.add('usuario2')
        self.assertEqual(Review.users_likes.count(), 1)
        self.rev.users_likes.remove('usuario2')
        self.assertEqual(Review.users_likes.count(), 0)