# users/views.py

from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm

# Create your views here.


class RegisterView(generic.CreateView):
    form_class = UserCreationForm 
    success_url = reverse_lazy("login")
    template_name = "users/register.html"

register_view = RegisterView.as_view()

