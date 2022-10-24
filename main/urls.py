from django.urls import path

app_name = 'main'


from . import views
from .views import UpdateUser

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
    path('profile/', views.user_profile, name='user_profile'),
    path('editarUsuario/', views.UpdateUser.as_view(), name='editar_user'),

]