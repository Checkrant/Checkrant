from django.test import TestCase
from django.utils import timezone
from publication.models import Restaurant 
from publication.models import Review

class RestaurantTest(TestCase):

    def setUp(self):
        self.rest = Restaurant.objects.create(restaurant_name='nomeRestaurante',food_type='testeComida')
        self.rest.save()

    def tearDown(self):
        self.rest.delete()

    def teste_rate(self):
        self.assertEqual(self.rest.restaurant_name, 'nomeRestaurante')
        self.assertEqual(self.rest.food_type, 'testeComida')