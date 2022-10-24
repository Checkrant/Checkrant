from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import HomeView

from  . import views 

urlpatterns = [
    path('', login_required(HomeView.as_view()), name='index')
]