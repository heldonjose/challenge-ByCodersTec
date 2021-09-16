from django.shortcuts import render, redirect

# Create your views here.
from django.views import View
from django.views.generic import TemplateView


class RedirecAuthenticationView(View):
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('core:login')
        return '....'

class LoginView(TemplateView):
    template_name = 'core/pages/login.html'

