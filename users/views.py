from django.shortcuts import render
from django.views.generic import CreateView, ListView
from .models import  UserRant
from .forms import  rantForm
from publication.models import Restaurant

#usuarios

class UserRantCreateView(CreateView):
    model = UserRant
    form_class = rantForm
    success_url = '/profile/'


class listrant(ListView):
     model = UserRant
     template_name = 'userrant_form.html'
     fields = ('nomeRant')
     success_url = '/profile/'

     def get_queryset(self):

         txt_nome = self.request.GET.get('nomeRant')

         if txt_nome:
            rants = UserRant.objects.filter(nomeRant__icontains=txt_nome)
         else:
            rants = UserRant.objects.all()

         return rants


