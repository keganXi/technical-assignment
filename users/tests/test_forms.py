# users/tests/test_forms.py

from django.test import TestCase

# forms.
from users.forms import RegisterForm, UpdateProfileForm

# models.
from users.models import User

# create tests below.

users = [
    {
        "username": "john",
        "password": "1234567",
        "home_address": "5 Lydenberg Street, Portland, Cape Town",
        "phone_number": "0845503982"
    }
]


class TestRegsterForm(TestCase):
    
    def test_form_valid(self):
        """
            NOTE: test if form is valid.
        """
        form = RegisterForm(data=users[0])
        self.assertTrue(form.is_valid())


class TestUpdateForm(TestCase):
    data = {
        "username": "john",
        "home_address": "Namibia",
        "phone_number": "0845503982"
    }

    def setUp(self):
        self.user = User.objects.create(**users[0])

    def test_form_valid(self):
        """
            NOTE: test if form is valid.
        """
        form = UpdateProfileForm(data=self.data, instance=self.user)
        self.assertTrue(form.is_valid())
