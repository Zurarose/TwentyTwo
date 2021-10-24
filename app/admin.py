from django.contrib import admin
from .models import *
from django.contrib.auth.models import Group

admin.site.unregister(Group)
admin.site.register(News)
admin.site.site_header = "Панель администратора серверной части приложения"


