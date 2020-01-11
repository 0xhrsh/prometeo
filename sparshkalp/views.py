from django.shortcuts import render
from .forms import loginForm, registerForm, uploadForm
from django.views.generic import CreateView
from django.contrib.auth.models import User
from .models import upload, userlog
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, login


class loginView(CreateView):
    form_class = loginForm
    template_name = 'sparshkalp/login.html'
    success_url = 'upload'

    def form_valid(self, form):        
        user=form.save()
        user = authenticate(username=user.username, password=user.password)
        if user:
            if user.is_active:
                login(self.request,user)
                return super(loginView, self).form_valid(form)
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            return HttpResponse("Invalid login details given")
        # user = self.request.user
        # if user is not None:
        #     team = form.save()
        #     team.captian = get_object_or_404(UserProfile, user=user)
        #     # TeamFormationView.create_team(team, **form.cleaned_data)
        #     return super(TeamFormationView, self).form_valid(form)
        # return HttpResponse("404")



class registerView(CreateView):
    form_class = registerForm
    template_name = 'sparshkalp/register.html'
    success_url = 'login'


class uploadView(CreateView):
    form_class = uploadForm
    template_name = 'sparshkalp/upload.html'
    success_url = 'upload'
