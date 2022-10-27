# users/forms.py
from django import forms

from django.contrib.auth.forms import UserCreationForm

# models.
from .models import User

# create forms below.


class RegistrationForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ["username", "password", "home_address", "phone_number"]
    
    def save(self):
        """
            NOTE: create a new user
        """
        user = User.objects.create_user(**self.data)
        return user
        