# users/forms.py

from django import forms

# models.
from .models import User

# api.
from api.google_geocode_api import GeocodeClient

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
        client = GeocodeClient(address)
        if client.status == "OK":
            self.cleaned_data.update(location=client.get_location())
        user = User.objects.create_user(**self.cleaned_data) # create user.
        return user


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, required=True)
    password = forms.CharField(max_length=150, required=True)



class UpdateProfileForm(forms.Form):
    username = forms.CharField(max_length=150)
    home_address = forms.CharField(max_length=150)
    phone_number = forms.CharField(max_length=15)


    def update(self, instance):
        """
            NOTE: update user profile.
        """
        home_address = self.cleaned_data.get("home_address", instance.home_address)

        # if home address did not change don't call geocode api.
        if home_address != instance.home_address:
            client = GeocodeClient(home_address)
            if client.status == "OK":
                # update location.
                instance.location = client.get_location() # set new location coordinates.

        instance.username = self.cleaned_data.get(
            "username", instance.username
        )
        instance.phone_number = self.cleaned_data.get(
            "phone_number", instance.phone_number
        )
        instance.save()

