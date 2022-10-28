# users/tests/test_views.py

from django.test import TestCase
from django.urls import reverse_lazy

# tests.
from .test_forms import TestRegsterForm

# models.
from users.models import User


# Write tests below.


class TestRegisterView(TestRegsterForm):

    def setUp(self):
        self.url = reverse_lazy("register")

    def test_create_user(self):
        response = self.client.post(self.url, data=self.users[0], follow=False)
        self.assertEquals(User.objects.first().count(), 1)
        

        

