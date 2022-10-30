# home/views.py.

from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from json import dumps

# models.
from users.models import User

# Create your views here.


# user home/dashboard first authenticate if user is logged in or not.
class HomeView(LoginRequiredMixin, View):
    template_name = "home/home.html"

    def get(self, request, *args, **kwargs):
        # get all registered user data.
        users = User.objects.all().values("username", "home_address", "phone_number", "location")
        data = dumps(list(users))
        return render(request, self.template_name, {"data": data})

home_view = HomeView.as_view()
    
