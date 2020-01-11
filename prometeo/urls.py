from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from sparshkalp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^accounts/', include('allauth.urls')),
    path('login', views.user_login.as_view(), name='login')
]
