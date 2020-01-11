from django import forms
from django.contrib.auth.models import User

class login(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
