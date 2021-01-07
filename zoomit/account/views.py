from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.mixins import AccessMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django import forms
from django.views.generic.edit import ModelFormMixin

from blog.urls import *
from .forms import RegistrationForm, SignInForm
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView


# def login_view(request):

#     context = {}
#     if request.user.is_authenticated:
#         return redirect('posts_archive')
#     if request.method == 'GET':
#         form = LoginForm()
#         context = {'form': form}
#     else:
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             user = authenticate(request, username=username, password=password)
#             if user and user.is_active:
#                 login(request, user)
#                 return redirect('posts_archive')
#             else:
#                 context = {'form': form}
#         else:
#             context = {'form': form}
#
#     return render(request, 'blog/form.html', context=context)

class Login(LoginView):
    template_name = 'blog/form.html'
    form_class = SignInForm


# def logout_view(request):
#     logout(request)
#     return redirect('posts_archive')

class Logout(LogoutView):
    pass


class RegisterView(CreateView, ModelFormMixin):
    form_class = RegistrationForm
    template_name = 'blog/register.html'

    def get_success_url(self):
        return reverse('login')

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(user.password)
            user.save()
            return redirect('login')
        return render(request, 'blog/register.html', context={'form': form})

# def register_view(request):
#     if request.method == 'GET':
#         form = RegistrationForm()
#         context = {'form': form}
#     else:
#         form = RegistrationForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.set_password(user.password)
#             user.save()
#             return redirect('login')
#         else:
#             context = {'form': form}
#
#     return render(request, 'blog/register.html', context=context)
