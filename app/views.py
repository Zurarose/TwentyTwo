"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.views.decorators.clickjacking import xframe_options_exempt
from django.contrib import messages
from .models import *
from django.views.decorators.gzip import gzip_page
import logging
from django.core.mail import send_mail
from django.conf import settings


loggerMS = logging.getLogger(__name__)
#loggerMS.error('Something went wrong')

@xframe_options_exempt
@gzip_page

    
def home(request):
    """Renders the home page."""
    request.session['toShow'] = "false"

    if request.POST.get("submit_contact"):
        email(request)

    if 'toShow' in request.session:
        toShow = request.session['toShow']
    else:
        toShow = "false"

    return render(
        request,
        'app/index.html',
        {
            "toShow": toShow
        }    
    )

def email(request):
    try:
        if (request.POST.get('name') != "" and request.POST.get('name') != None):
            name = request.POST.get('name')  #пристройки
        else:
            name = "error"

        if (request.POST.get('phone') != "" and request.POST.get('phone') != None):
            phone = request.POST.get('phone')  #пристройки
        else:
            phone = "error"

        subject = 'message'
        message = name + ";" + phone
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['gs2.22.info@gmail.com',]
        send_mail( subject, message, email_from, recipient_list )
        request.session['toShow'] = "true"
    except:
        request.session['toShow'] = "false"

def news(request):
    instances = News.objects.all()
    return render (request, 'app/news.html', {'instances': instances})

def plans(request):
    return render (request, 'app/plans.html')

def contacts(request):
    return render (request, 'app/contacts.html')

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
