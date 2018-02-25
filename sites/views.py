from django.shortcuts import render, get_object_or_404

from . import models

# Create your views here.

def index(req):
    return render(req, 'sites/list.html', {
        'sites': models.Site.objects.all().iterator()
    })


def site_details(req, site_id):
    site_qs = models.Site.objects.prefetch_related('records')
    site = get_object_or_404(site_qs, pk=site_id)
    return render(req, 'sites/details.html', {'site': site})
