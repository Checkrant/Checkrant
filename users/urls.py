from django.urls import path
from .views import  UserRantCreateView, listrant
from . import views

urlpatterns = [


    path('rantForm/', UserRantCreateView.as_view(), name='rant.index'),
    path('rantlist/', listrant.as_view(), name='rantlist.index'),

    #path('favorite/<int:id>', views.add_fav, name='add_fav')
  
]