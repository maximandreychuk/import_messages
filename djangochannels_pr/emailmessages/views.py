from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.urls import reverse_lazy, reverse
from .models import Message


class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'register.html'

    def get_success_url(self):
        return reverse('messages_list')


class LoginView(LoginView):
    form_class = AuthenticationForm
    template_name = 'login.html'

    def get_success_url(self):
        return reverse('messages_list')


def logout_user(request):
    logout(request)
    return redirect('login')


def messages_list(request):
    messages = Message.objects.all()
    return render(request, 'messages_list.html', {'messages': messages})
