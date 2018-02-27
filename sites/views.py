from django import urls
from django.views import generic as generic_views

from . import models


class Navigation:
    def __init__(self, name, paths):
        if not paths:
            raise ValueError('At least one path should be provided')

        self.name = name
        self.paths = paths

    @property
    def path(self):
        return self.paths[0]

    def __repr__(self):
        return '%s<name:%s, path:%s>' % (
            type(self).__name__,
            self.name,
            self.path
        )


MAIN_NAV = [
    Navigation('Sites', [
        urls.reverse_lazy('site-list'), urls.reverse_lazy('home')
    ]),
    Navigation('Summary', [
        urls.reverse_lazy('site-summary'),
        urls.reverse_lazy('site-summary-average'),
    ])
]


SUMMARY_NAV = [
    Navigation('Sum', [
        urls.reverse_lazy('site-summary')
    ]),
    Navigation('Average', [
        urls.reverse_lazy('site-summary-average')
    ])
]


class ViewMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['main_nav'] = MAIN_NAV
        context['summary_nav'] = SUMMARY_NAV
        return context


class SiteListView(ViewMixin, generic_views.ListView):
    model = models.Site
    context_object_name = 'sites'
    template_name = 'sites/list.html'


class SiteDetailsView(ViewMixin, generic_views.DetailView):
    queryset = models.Site.objects.prefetch_related('records')
    template_name = 'sites/details.html'
    context_object_name = 'site'


class SiteSummaryView(ViewMixin, generic_views.ListView):
    queryset = models.Site.objects.all().with_sums()
    template_name = 'sites/summary.html'
    context_object_name = 'sites'


class SiteSummaryAvgView(SiteSummaryView):
    queryset = models.Site.objects.all().with_avgs()
