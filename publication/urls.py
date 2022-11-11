from django.urls import path
from . import views

urlpatterns = [
    path('', views.pub, name='pub.index'),
    path('success', views.success, name="success"),
    path('rate/<int:id>', views.rate, name="rate"),
    path('like/rate/<int:id>', views.like_rate, name="like_rate"),
    path('reviews', views.viewReview, name="viewReview.index"),
    path('favorites', views.favorite, name='favorite.index'),
    path('favorites/''/<int:id>', views.add_fav, name="add_fav"),
]
