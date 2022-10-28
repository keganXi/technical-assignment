# home/views.py.

from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


# user home/dashboard first authenticate if user is logged in or not.
class HomeView(LoginRequiredMixin, View):
    template_name = "home/home.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

home_view = HomeView.as_view()
    
