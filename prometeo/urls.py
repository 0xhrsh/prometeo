from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.conf.urls.static import static
from sparshkalp import views
from . import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^logout/',views.logout_request,name='logout'),
    # path('register', views.registerView.as_view(), name='register'),
    url(r'^register/$',views.registerView,name='register'),
    path('upload', views.uploadView.as_view(), name='upload'),
    path('login', views.loginView.as_view(), name='login'),
    path('', views.giveAccess.as_view(), name='index'),
    path('index', views.giveAccess.as_view(), name='index'),
    url(r'^end/$',views.takeAccess,name='end'),
    # path('end', views.takeAccess.as_view(), name='end'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
