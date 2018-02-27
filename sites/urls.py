from django.urls import path

from . import views

urlpatterns = [
    path('', views.SiteListView.as_view(), name='home'),
    path('sites', views.SiteListView.as_view(), name='site-list'),
    path('sites/<int:pk>', views.SiteDetailsView.as_view(), name='site-details'),
    path('summary', views.SiteSummaryView.as_view(), name='site-summary'),
    path('summary-average', views.SiteSummaryAvgView.as_view(), name='site-summary-average'),
]
