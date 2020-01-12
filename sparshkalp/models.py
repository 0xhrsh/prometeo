from django.db import models
from django.contrib.auth.models import User
from prometeo import settings
class userlog(models.Model):
    username = models.CharField(max_length=8, blank=False)
    password = models.CharField(max_length=16, blank=False)

class doc(models.Model):
    doctorId =models.CharField(max_length=8, blank=False)

    
class upload(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
