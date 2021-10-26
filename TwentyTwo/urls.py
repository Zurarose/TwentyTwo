"""
Definition of urls for TwentyTwo.
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.urls import path, reverse_lazy
from django.views.generic.base import RedirectView
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve

urlpatterns = [
    path('', views.home, name='home'),   
    path('admin/', admin.site.urls),
    path('news/', views.news, name='news'), 
    path('plans/', views.plans, name='plans'), 
]
if settings.DEBUG:
   urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)



