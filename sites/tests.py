from django.test import TestCase, Client

from . import models


class TestMainSitesList(TestCase):
    fixtures = ['sites.json']

    def setUp(self):
        self.client = Client()
        self.resp = self.client.get('/sites')

    def test_sites_path_exists(self):
        self.assertEqual(self.resp.status_code, 200)

    def test_sites_list_uses_base_template(self):
        self.assertTemplateUsed(self.resp, 'sites/list.html')

    def test_sites_is_alias_for_root(self):
        resp = self.client.get('/')
        self.assertEqual(resp.content, self.resp.content)

    def test_sites_count(self):
        self.assertEqual(3, models.Site.objects.count())

    def test_sites_displayed_on_the_page(self):
        for site in models.Site.objects.all():
            self.assertContains(self.resp, site.name)
