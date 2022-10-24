
from django.views.generic import UpdateView






    
# Create your views here.



from django.urls import reverse_lazy
from django.shortcuts import render, redirect,  get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


from .forms import UserForm





def home(request):
    template_name = 'main/index.html'
    context = {}
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            f = form.save()
            f.set_password(f.password)
            f.save()
            messages.success(request, 'Usuário cadastrado com sucesso.')
            return redirect('main:home')
    form = UserForm()
    context['form'] = form
    return render(request, template_name, context)



class UpdateUser(UpdateView):
    template_name = 'main/editar_user.html'
    model = User
    fields = ['first_name', 'username', 'email']
    success_url = reverse_lazy('main:user_profile')


    def saveUpdate(request, template_name):
        context = {}
        if request.method == 'POST':
            form = UserForm(request.POST)
            if form.is_valid():
                f = form.save()
                f.set_password(f.password)
                f.save()
                messages.success(request, 'Usuário cadastrado com sucesso.')
                return redirect('main:home')
        form = UserForm()
        context['form'] = form
        return render(request, template_name, context)

    def get_object(self, queryset=None):
        self.object = get_object_or_404(User, username=self.request.user)
        return self.object



def user_login(request):
    template_name = 'main/user_login.html'
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main:user_profile')
        else:
            print('deu caca')

    return render(request, template_name, {})


@login_required(login_url='/login/')
def user_profile(request):
    template_name = 'main/user_profile.html'
    return render(request, template_name, {})


@login_required(login_url='/login/')
def user_logout(request):
    logout(request)
    messages.success(request, 'Você saiu do sistema.')
    return redirect('main:home')
