from django.urls import path
from .views import UserCreateView, UserRantCreateView, UpdateUser
from . import views

urlpatterns = [


    path('userForm/', UserCreateView.as_view(), name='user.index'),
    path('update/<int:pk>', UpdateUser.as_view(), name='update.index'),
    path('rantForm/', UserRantCreateView.as_view(), name='rant.index'),
    path('favorite/<int:id>', views.add_fav, name='add_fav')
  
]