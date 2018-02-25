from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='site-list'),
    path('sites', views.index, name='site-list'),
]
