"""
Definition of urls for TwentyTwo.
"""

from datetime import datetime
from django.urls import include, path
from django.contrib import admin
from app import forms, views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),       
    path('news/', views.news, name='news'), 
    path('plans/', views.plans, name='plans'), 
    path('i18n/', include('django.conf.urls.i18n')),
]

#if settings.DEBUG:
#   urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)



