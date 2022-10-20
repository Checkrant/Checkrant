from django.urls import path
from . import views

urlpatterns = [
    path('', views.pub, name='pub.index'),
    path('success',views.success, name="success"),
    path('rate/<int:id>',views.rate,name="rate"),
    path('rate/<int:id>',views.like_rate, name="like_rate"),
    path('reviews',views.viewReview, name="viewReview.index"),
]