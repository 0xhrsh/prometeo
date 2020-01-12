from django import forms
from django.contrib.auth.models import User
from .models import upload, userlog
class registerForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class loginForm(forms.ModelForm):
    class Meta:
        model = userlog
        fields = ['username', 'password']


class uploadForm(forms.ModelForm):
    class Meta:
        model = upload
        fields = ['description','document',]

class giveAccessForm(forms.ModelForm):
    class Meta:
        model = userlog
        fields = ['doctorId']
