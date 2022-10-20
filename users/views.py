from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView
from .models import User, UserRant
from .forms import userForm, rantForm

#usuarios


class UserCreateView(CreateView):
    model = User
    form_class = userForm
    success_url = '/#/'

class UserRantCreateView(CreateView):
    model = UserRant
    form_class = rantForm
    success_url = '/#/'


class UpdateUser(UpdateView):
    model = User
    form_class = userForm
    success_url = '/#/'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo"] = "atualizar"

        return context