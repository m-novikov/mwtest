from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('sites', views.index, name='site-list'),
    path('sites/<int:site_id>', views.site_details, name='site-details'),
    path('summary', views.site_summary, name='site-summary'),
]
