# users/views.py

from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from django.views import View
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login

# forms.
from .forms import RegisterForm, LoginForm

# Create your views here.


class RegisterView(View):
    form_class = RegisterForm 
    success_url = reverse_lazy("login")
    template_name = "users/register.html"

    def get(self, request, *args, **kwargs):
        # render register page.
        return render(request, self.template_name, {'form': self.form_class})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect(self.success_url)

register_view = RegisterView.as_view()



class LoginView(View):
    form_class = LoginForm 
    success_url = "login"
    template_name = "users/login.html"

    def get(self, request, *args, **kwargs):
        # render register page.
        return render(request, self.template_name, {'form': self.form_class})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # authenticate user credentials.
            user = authenticate(request, **form.cleaned_data)
            if user is not None:
                login(user)
                return redirect(self.success_url)
            else:
                # Invalid user credentials.
                messages.error(request, "Incorrect username or password!")
                return render(request, self.template_name, {'form': self.form_class})

login_view = LoginView.as_view()

