# users/tests/test_models.py

from django.test import TestCase

# models.
from users.models import User


# create tests below.


class TestUsersModels(TestCase):
    users = [
        {
            "username": "john_doe",
            "password": "1234567",
            "email": "johndoe@test.com",
            "home_address": "5 Lydenberg Street, Portland, Cape Town",
            "phone_number": "0845503982"
        }
    ]
    location = "-34.0552652,18.6145938"


    def setUp(self):
        # create test user.
        self.user = User.objects.create_user(**self.users[0])


    def test_total_users(self):
        """
            NOTE: test total number of users created.
        """
        total_users = 1
        self.assertEquals(total_users, User.objects.all().count())

    
    def test_location_not_empty(self):
        """
            NOTE: check if user location is not empty.
        """
        self.assertGreater(len(self.user.location), 0)


    def test_correct_location(self):
        """
            NOTE: test if google maps api returned the correct coordinates.
        """
        self.assertEquals(self.user.location, self.location) 


    def test_which_user(self):
        """
             NOTE: test which user was created.
        """
        username = self.users[0]["username"]
        self.assertTrue(User.objects.filter(username=username).exists())
