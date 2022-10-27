# users/views.py

from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy

# forms.
from .forms import RegistrationForm

# Create your views here.


class RegisterView(generic.CreateView):
    form_class = RegistrationForm 
    success_url = reverse_lazy("login")
    template_name = "users/register.html"

register_view = RegisterView.as_view()

