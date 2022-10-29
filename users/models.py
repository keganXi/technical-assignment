# users/models.py

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from technical_assignment.settings.base import GOOGLE_API_KEY
import requests


# Create your models here.


class User(AbstractUser):
    home_address = models.CharField(
        _("home address"),
        max_length=150)
    phone_number = models.CharField(
        _("phone number"),
        max_length=15)
    location = models.CharField(max_length=63)

    REQUIRED_FIELDS = ["home_address", "phone_number"]

    def save(self, *args, **kwargs):
        """
            NOTE:
                - get longitude and latitude from home_address using google
                  maps api.
        """
        address = self.home_address # get user's home addres.
        api_key = GOOGLE_API_KEY # google api key
        api_response = requests.get(
            'https://maps.googleapis.com/maps/api/geocode/json?address={0}&key={1}'.format(address, api_key))
        api_response_dict = api_response.json()

        if api_response_dict['status'] == 'OK':
            self.location = ",".join(
                [str(api_response_dict['results'][0]['geometry']['location']['lat']),
                str(api_response_dict['results'][0]['geometry']['location']['lng'])])
            self.save()
        super(User, self).save(*args, **kwargs)

    def __str__(self):
        return self.username
