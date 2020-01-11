from django.shortcuts import render
from .forms import login
from django.views.generic import CreateView

class user_login(CreateView):
    form_class = login
    template_name = 'sparshkalp/login.html'
    success_url = 'login'
