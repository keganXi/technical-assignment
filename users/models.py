# users/models.py

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

# 3rd party packages.
from location_field.models.plain import PlainLocationField

# Create your models here.


class User(AbstractUser):
    home_address = models.CharField(
        _("home address"),
        max_length=150)
    phone_number = models.CharField(
        _("phone number"),
        max_length=15)
    location = PlainLocationField(based_fields=["home_address"], zoom=7, blank=True)

    REQUIRED_FIELDS = ["home_address", "phone_number"]

    def __str__(self):
        return self.username
