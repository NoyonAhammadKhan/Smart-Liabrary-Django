from django.shortcuts import render, redirect
from .forms import UserSignupForm
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import FormView, View
from django.urls import reverse_lazy
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView, LogoutView
# Create your views here.


class UserSignupView(FormView):
    template_name = 'users/signup.html'
    form_class = UserSignupForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)


class UserLoginView(LoginView):

    template_name = 'users/login.html'

    def get_success_url(self):
        return reverse_lazy('home')


def user_logout(request):
    logout(request)
    return redirect('login')
