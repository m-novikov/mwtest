from django.shortcuts import render, get_object_or_404

from . import models

# Create your views here.

def index(req):
    return render(req, 'sites/list.html', {
        'sites': models.Site.objects.all().iterator()
    })


def site_details(req, site_id):
    site = get_object_or_404(models.Site, pk=site_id)
    return render(req, 'sites/details.html', {'site': site})
