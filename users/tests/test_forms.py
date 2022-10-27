# users/tests/test_forms.py

from django.test import TestCase

# forms.
from users.forms import RegistrationForm

# models.
from users.models import User

# create tests below.


class TestRegstrationForm(TestCase):
    users = [
        {
            "username": "john",
            "password": "1234567",
            "home_address": "21 test st, western cape",
            "phone_number": "0845503982"
        }
    ]

    def test_form(self):
        """
            NOTE: create user with registration form.
        """
        form = RegistrationForm(self.users[0])
        form.save()
        self.assertTrue(User.objects.filter(username=self.users[0]["username"]).exists())
        
        

