# users/tests/test_forms.py

from django.test import TestCase

# forms.
from users.forms import RegisterForm

# models.
from users.models import User

# create tests below.


class TestRegsterForm(TestCase):
    users = [
        {
            "username": "john",
            "password": "1234567",
            "home_address": "21 test st, western cape",
            "phone_number": "0845503982"
        }
    ]

    def test_form_valid(self):
        """
            NOTE: test if form is valid.
        """
        form = RegisterForm(data=self.users[0])
        self.assertTrue(form.is_valid())

