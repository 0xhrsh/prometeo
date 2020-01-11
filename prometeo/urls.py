from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from sparshkalp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^logout/',views.logout_request,name='logout'),
    path('register', views.registerView.as_view(), name='register'),
    path('upload', views.uploadView.as_view(), name='upload'),
    path('', views.loginView.as_view(), name='index'),
]
