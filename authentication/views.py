from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


class Signup(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('signin')
    template_name = 'signup.html'

class Signin(LoginView):
    template_name = 'signin.html'
    success_url = reverse_lazy('profile')

@login_required
def Profile(request):
    return render(request, 'profile.html')