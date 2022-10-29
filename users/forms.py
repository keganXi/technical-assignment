# users/forms.py

from django import forms
from technical_assignment.settings.base import GOOGLE_API_KEY
import requests

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
            NOTE: create a new user and getting longitude and latitude
                  from home_address using google maps geocoding api.
        """
        address = self.cleaned_data.get("home_address") # get user's home addres.
        api_key = GOOGLE_API_KEY # google api key
        api_response = requests.get(
            'https://maps.googleapis.com/maps/api/geocode/json?address={0}&key={1}'.format(address, api_key))
        api_response_dict = api_response.json()

        if api_response_dict['status'] == 'OK':
            location = ",".join(
                [str(api_response_dict['results'][0]['geometry']['location']['lat']),
                str(api_response_dict['results'][0]['geometry']['location']['lng'])])
            self.cleaned_data.update(location=location)
        user = User.objects.create_user(**self.cleaned_data) # create user.
        return user


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, required=True)
    password = forms.CharField(max_length=150, required=True)
