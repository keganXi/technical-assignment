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


class TestUpdateProfileForm(TestCase):
    data = {
        "username": "john",
        "home_address": "Namibia",
        "phone_number": "0845503982"
    }
    location = "-22.95764,18.49041"

    def setUp(self):
        self.user = User.objects.create(**users[0])

    def test_form_valid(self):
        """
            NOTE: test if form is valid.
        """
        self.form = UpdateProfileForm(data=self.data)
        self.assertTrue(self.form.is_valid())

    def test_update_location(self):
        """
            NOTE: test updated location based on home address.
        """
        self.test_form_valid()
        self.form.update(instance=self.user)
        self.assertEquals(self.user.location, self.location)
