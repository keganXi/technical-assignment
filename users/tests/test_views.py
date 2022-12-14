# users/tests/test_views.py

from django.test import TestCase
from django.urls import reverse

# tests.
from .test_forms import users

# models.
from users.models import User


# Write tests below.


class TestAuthViews(TestCase):
    registration_credentials = {
        "username": "jack",
        "home_addres": "5 Lydenberg Street, Portland, Cape Town",
        "phone_number": "0845503982",
        "password": "12345678"
    }
    login_credentials = {
        "username": "jack",
        "password": "12345678"
    }
    fail_login_credentials = {
        "username": "john",
        "password": "12345678"
    }
    location = "-34.0552652,18.6145938"


    def setUp(self):
        self.url_register = reverse("register")
        self.url_login = reverse("login")
        self.url_home = reverse("home")
        self.url_logout = reverse("logout")

        # create user.
        self.user = User.objects.create_user(**self.login_credentials)


    def test_register_user_successful(self):
        """
            NOTE: user should register successfully and should redirect to login.
        """
        # send post request with user registration data.
        response = self.client.post(self.url_register, data=users[0], follow=True)
        self.assertEquals(response.status_code, 200) # redirect to login.
        self.assertContains(response, "Don't have an account?") # redirect was successful.
        username = users[0]["username"] # get username.
        self.assertTrue(User.objects.filter(username=username).exists()) # check if user was created.

    
    def test_correct_location_coordinates_after_registration(self):
        """
            NOTE: test if google geocode api got correct location
                  coordinates when registering.
        """
        # send post request with user registration data.
        response = self.client.post(self.url_register, data=users[0], follow=True)
        self.assertEquals(response.status_code, 200) # redirect to login.
        username = users[0]["username"] # get username.
        self.assertEquals(User.objects.get(username=username).location, self.location) # test location coordinates.

    
    def test_register_user_failed(self):
        """
            NOTE: registration should fail because of incorrect credentials.
        """
        # send post request with user registration data.
        response = self.client.post(self.url_register, data=self.registration_credentials)
        self.assertContains(response, "A user with that username already exists.") # html contains error message.


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

    
    def test_logout(self):
        """
            NOTE: testing logout functionality.
        """
        # login user and navigate to home page.
        self.client.force_login(self.user, backend=None)
        response = self.client.get(self.url_home, follow=True)
        self.assertContains(response, f"Welcome {self.login_credentials['username']}")

        # logout user.
        response = self.client.get(self.url_logout, follow=True) # logout
        self.assertEquals(response.status_code, 200) # successful redirect
        self.assertContains(response, f"Don't have an account?") # landed on login page.



        
        