# users/tests/test_views.py

from django.test import TestCase
from django.urls import reverse

# tests.
from .test_forms import TestRegsterForm

# models.
from users.models import User


# Write tests below.


class TestRegisterView(TestRegsterForm):

    def setUp(self):
        self.url = reverse("register")

    def test_register_user_successful(self):
        # send post request with user registration data.
        response = self.client.post(self.url, data=self.users[0])
        self.assertEquals(response.status_code, 302) # post request was successful and redirect to login.
        username = self.users[0]["username"] # get username.
        self.assertTrue(User.objects.filter(username=username).exists()) # check if user was created.
        