"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from django.views.decorators.clickjacking import xframe_options_exempt

@xframe_options_exempt
def home(request):
    """Renders the home page."""
    return render(
        request,
        'app/index.html',
        {
            
        }
    )