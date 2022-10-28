# users/views.py

from django.shortcuts import render
from django.shortcuts import redirect
from django.views import View
from django.urls import reverse_lazy

# forms.
from .forms import RegisterForm

# Create your views here.


class RegisterView(View):
    form_class = RegisterForm 
    success_url = reverse_lazy("login")
    template_name = "users/register.html"

    def get(self, request, *args, **kwargs):
        # render register page.
        return render(request, self.template_name, {'form': self.form_class})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect(self.success_url)

register_view = RegisterView.as_view()

