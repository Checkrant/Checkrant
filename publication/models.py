from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from users.models import UserRant


class Restaurant(models.Model):
    restaurant_name = models.CharField(max_length=30)
    food_type = models.TextField(max_length=3000)
    rest_pic = models.FileField(upload_to='')
    favorites = models.ManyToManyField(User, related_name='favorite', default=None, blank=True)

    def __str__(self):
        return self.restaurant_name


class Review(models.Model):
    writer = models.CharField(max_length=40, default="anonymous")
    pub_date = models.DateTimeField(default=timezone.now)
    stars_nums = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5)
    )
    stars = models.IntegerField(choices=stars_nums)
    detail = models.TextField(max_length=4000, default="Type here your review.")
    users_likes = models.ManyToManyField(User, related_name="likes")
    restaurant = models.ForeignKey(UserRant, on_delete=models.CASCADE)
    def total_likes(self):
        return self.users_likes.count()

    def __str__(self):
        return self.restaurant.nomeRant
