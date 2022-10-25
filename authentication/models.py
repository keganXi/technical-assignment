from django.db import models
from django.contrib.gis.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

# Create your models here.

class User(AbstractUser):
    home_address = models.CharField(
        _("home address"),
        max_length=150)
    phone_number = models.CharField(
        _("phone number"),
        max_length=15
    )
    location = models.PointField(
        _("location"),
        null=True)
    REQUIRED_FIELDS = ["home_address", "phone_number", "location"]

    def __str__(self): return f"{self.username}"