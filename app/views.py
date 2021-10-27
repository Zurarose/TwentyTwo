"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.views.decorators.clickjacking import xframe_options_exempt
from django.contrib import messages
from .models import *

@xframe_options_exempt
def home(request):
    """Renders the home page."""
    return render(
        request,
        'app/index.html',
        {
            
        }
    )
def news(request):
    instances = News.objects.all()
    return render (request, 'app/news.html', {'instances': instances})

def plans(request):
    return render (request, 'app/plans.html')

def login(request):                  
    """Renders the home page."""
    if request.user.is_authenticated:
       return render(request, 'app/admin.html')

    if request.POST.get('log'):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            log(request, user)
            # Redirect to a success page.
            return HttpResponseRedirect(reverse('admin:index'))
        else:
            # Return an 'invalid login' error message.
            messages.error(request,'username or password not correct')
            return redirect('login')                  
    return render(request, 'app/login.html')
