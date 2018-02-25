from django.shortcuts import render

from . import models

# Create your views here.

def index(req):
    return render(req, 'sites/list.html', {
        'sites': models.Site.objects.all().iterator()
    })
