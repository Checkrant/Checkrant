from django.shortcuts import render
from django.views.generic import CreateView
from .models import  UserRant
from .forms import  rantForm
from publication.models import Restaurant

#usuarios

class UserRantCreateView(CreateView):
    model = UserRant
    form_class = rantForm
    success_url = '/#/'


