# users/forms.py

from django import forms

# models.
from .models import User

# create forms below.


class RegisterForm(forms.ModelForm):
    username = forms.CharField(error_messages={'required': 'This username is already taken!'})
    
    class Meta:
        model = User
        fields = ["username", "password", "home_address", "phone_number"]
    
    def save(self):
        """
            NOTE: create a new user.
        """
        user = User.objects.create_user(**self.cleaned_data)
        return user


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, required=True)
    password = forms.CharField(max_length=150, required=True)
