# users/views.py

from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from django.views import View
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin

# forms.
from .forms import RegisterForm, LoginForm, UpdateProfileForm

# models.
from .models import User

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
        return render(request, self.template_name, {'form': form})

register_view = RegisterView.as_view()



class LoginView(View):
    form_class = LoginForm 
    success_url = reverse_lazy("home")
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
                login(request, user)
                return redirect(self.success_url)
            else:
                # Invalid user credentials.
                messages.error(request, "Incorrect username or password!")
        return render(request, self.template_name, {'form': self.form_class})

login_view = LoginView.as_view()



def profile_view(request):
    return render(request, "users/profile.html")


class UpdateProfileView(LoginRequiredMixin ,View):
    form_class = UpdateProfileForm
    success_url = reverse_lazy("profile")
    template_name = "users/update-profile.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            form.update(instance=request.user)
            return redirect(self.success_url)
        return render(request, self.template_name)

update_profile_view = UpdateProfileView.as_view()
