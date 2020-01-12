from django import forms
from django.contrib.auth.models import User
from .models import upload, userlog, doc
# class registerForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password']

class registerForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())
	class Meta():
		model = User
		fields = ('email','username','password')


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
        model = doc
        fields = ['doctorId']
