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
import os, shutil, time
from django.contrib.auth.decorators import login_required


class loginView(CreateView):
    form_class = loginForm
    template_name = 'sparshkalp/login.html'
    success_url = "index"

    def form_valid(self, form):
        user=form.save()
        print(user.username,user.password)
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


def logout_request(request):
    if request.user.username != "":
        print("logged in",request.user.username)
        logout(request)
        messages.info(request, "Logged out successfully!")
    return redirect("index")

# class registerView(CreateView):
#     form_class = registerForm
#     template_name = 'sparshkalp/register.html'
#     success_url = 'login'



def registerView(request):
    registered = False
    if request.method == 'POST':
        user_form = registerForm(data=request.POST)
        user_form.email = request.POST.get('email')
        user_form.username = request.POST.get('username')
        user_form.password = request.POST.get('password')
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
            return redirect("login")
        else:
            return HttpResponse(user_form.errors)

    else:
        user_form = registerForm()
        # return HttpResponse("hey")
        #profile_form = UserProfileInfoForm()
    return render(request,'sparshkalp/register.html',
                          {'user_form':user_form,
                           'registered':registered})





class uploadView(CreateView):
    form_class = uploadForm
    template_name = 'sparshkalp/upload.html'
    success_url = 'upload'
    def form_valid(self, form):
        if self.request.user.username == "":
            return redirect("login")
        file=form.save()
        file = file.document
        os.chdir('media')
        os.chdir('documents')
        ls_fd = os.popen("mkdir {}".format(self.request.user))#,file,self.request.user))
        shutil.move(str(file)[10:],"{}/".format(self.request.user)+str(file)[10:])
        output = ls_fd.read()
        print(output)
        os.chdir('..')
        os.chdir('..')
        ls_fd.close()
        return redirect("index")

class giveAccess(CreateView):
    form_class = giveAccessForm
    template_name = 'sparshkalp/doctor.html'
    success_url = 'end'
    #@login_required
    def form_valid(self, form):
        if self.request.user.username == "":
            return redirect("login")
        print(self.request.user)
        doctor=form.save()
        doctorId=doctor.doctorId
        os.chdir('media')
        os.chdir('documents')
        ls=os.popen('mkdir ' + str(self.request.user))
        ls.close()
        os.chdir(str(self.request.user))
        source = os.getcwd()
        os.chdir('..')
        ls=os.popen('mkdir ' + str(doctorId))
        ls.close()
        os.chdir(str(doctorId))
        destination = os.getcwd()
        file_url = shutil.move(source, destination, copy_function = shutil.copytree)
        os.chdir('..')
        os.chdir('..')
        os.chdir('..')
        os.chdir('..')
        return render(self.request,'sparshkalp/end.html',{'file_url' : file_url})

def takeAccess(request):
    if request.method == 'POST':
        os.chdir('media')
        os.chdir('documents')
        os.chdir(str(request.doctorId))
        os.remove(str(request.user))
        os.chdir('..')
        os.chdir('..')
        os.chdir('..')
        return redirect("index")
    else:
        os.chdir('media')
        os.chdir('documents')

        os.chdir(str(request.user))
        file_url =str(os.getcwd())
        os.chdir('..')
        os.chdir('..')
        os.chdir('..')
        #module_dir = os.path.dirname(__file__)  # get current directory
        #file_url = os.path.join(file_url, 'changelog.txt')
        return render(request,'sparshkalp/end.html',{'file_url' : file_url})


def viewRecords(request):
    fs = FileSystemStorage()
    os.chdir('media')
    os.chdir('documents')
    os.chdir(str(request.user))
    file_url =os.getcwd()
    os.chdir('..')
    os.chdir('..')
    os.chdir('..')
    return render(request,'sparshkalp/end.html',{'file_url' : file_url})
    #return render(request,str(os.getcwd())
