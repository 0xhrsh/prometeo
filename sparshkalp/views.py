from django.shortcuts import render
from .forms import loginForm, registerForm, uploadForm, giveAccessForm
from django.views.generic import CreateView
from django.contrib.auth.models import User
from .models import upload, userlog
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import redirect
from apiclient.http import MediaFileUpload
from django.core.files.storage import FileSystemStorage
from datetime import datetime
import os
import shutil
from django.contrib.auth.decorators import login_required



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

@login_required
def logout_request(request):
    if request.user.username != "":
        print("logged in",request.user.username)
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("index")

class registerView(CreateView):
    form_class = registerForm
    template_name = 'sparshkalp/register.html'
    success_url = 'login'


class uploadView(CreateView):
    form_class = uploadForm
    template_name = 'sparshkalp/upload.html'
    success_url = 'upload'
    @login_required
    def form_valid(self, form):
        file=form.save()
        file = file.document
        os.chdir('media')
        os.chdir('documents')
        ls_fd = os.popen("mkdir {}".format(self.request.user))#,file,self.request.user))
        shutil.move(str(file)[10:],"{}/".format(self.request.user))#+str(file)[10:])
        output = ls_fd.read()
        print(output)
        os.chdir('..')
        os.chdir('..')
        ls_fd.close()
        return redirect("index")

class giveAccess(CreateView):
    form_class = giveAccessForm
    template_name = 'sparshkalp/doctor.html'
    success_url = 'index'
    #@login_required
    def form_valid(self, form):
        if self.request.user != "":
            print("here")
            return redirect("login")
        else:
            print("not")
        doctor=form.save()
        doctorId=doctor.doctorId
        print(doctorId)
        return redirect("index")
