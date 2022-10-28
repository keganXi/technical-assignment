# users/tests/test_views.py

from django.test import TestCase
from django.urls import reverse

# tests.
from .test_forms import TestRegsterForm

# models.
from users.models import User


# Write tests below.


class TestAuthViews(TestRegsterForm):
    login_credentials = {
        "username": "jack",
        "password": "12345678"
    }
    fail_login_credentials = {
        "username": "john",
        "password": "12345678"
    }


    def setUp(self):
        self.url_register = reverse("register")
        self.url_login = reverse("login")

        # create user.
        User.objects.create_user(**self.login_credentials)


    def test_register_user_successful(self):
        """
            NOTE: user should register successfully and should redirect to login.
        """
        # send post request with user registration data.
        response = self.client.post(self.url_register, data=self.users[0], follow=True)
        self.assertEquals(response.status_code, 200) # redirect to login.
        self.assertContains(response, "Don't have an account?") # redirect was successful.
        username = self.users[0]["username"] # get username.
        self.assertTrue(User.objects.filter(username=username).exists()) # check if user was created.


    def test_login_user_successful(self):
        """
            NOTE: user should login successfully and should redirect to home.
        """
        # send post request with user login data.
        response = self.client.post(
            self.url_login, data=self.login_credentials, follow=True)
        self.assertEquals(response.status_code, 200) # redirect to home.
        self.assertContains(response, f"Welcome {self.login_credentials['username']}") # redirect was successful.

    
    def test_login_user_failed(self):
        """
            NOTE: authentication should fail because of incorrect login credentials.
        """
        # send post request with user login data.
        response = self.client.post(
            self.url_login, data=self.fail_login_credentials)
        self.assertContains(response, "Incorrect username or password!") # html contains error message.
        
        