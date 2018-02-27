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
        self.assertTemplateUsed(self.resp, 'sites/base.html')
        self.assertTemplateUsed(self.resp, 'sites/list.html')

    def test_sites_is_alias_for_root(self):
        resp = self.client.get('/')
        self.assertEqual(resp.content, self.resp.content)

    def test_sites_count(self):
        self.assertEqual(3, models.Site.objects.count())

    def test_sites_displayed_on_the_page(self):
        template = '<a href="/sites/%s">%s</a>'

        for site in models.Site.objects.all():
            site_link = template % (site.id, site.name)
            self.assertContains(self.resp, site_link)


class TestSiteDetails(TestCase):
    fixtures = ['sites.json']

    def setUp(self):
        self.client = Client()
        self.resp = self.client.get('/sites/1')

    def test_details_path_exists(self):
        self.assertEqual(self.resp.status_code, 200)

    def test_sites_details_uses_correct_templates(self):
        self.assertTemplateUsed(self.resp, 'sites/base.html')
        self.assertTemplateUsed(self.resp, 'sites/table.html')
        self.assertTemplateUsed(self.resp, 'sites/details.html')

    def test_details_page_contains_header(self):
        self.assertContains(self.resp, 'Site Details - Demo Site')


class TestSummaryPage(TestCase):
    fixtures = ['sites.json']

    def setUp(self):
        self.client = Client()
        self.resp = self.client.get('/summary')

    def test_details_path_exists(self):
        self.assertEqual(self.resp.status_code, 200)

    def test_sites_list_uses_base_template(self):
        self.assertTemplateUsed(self.resp, 'sites/base.html')
        self.assertTemplateUsed(self.resp, 'sites/table.html')
        self.assertTemplateUsed(self.resp, 'sites/summary.html')

    def test_details_page_contains_header(self):
        self.assertContains(self.resp, 'Summary')


class TestAggregationMethods(TestCase):
    fixtures = ['sites.json']

    def test_sum_aggregation(self):
        sites = models.Site.objects.with_sums()
        expected_by_id = {
            1: {'a_value': 52.0, 'b_value': 196.0},
            2: {'a_value': 5.0, 'b_value': 15.0},
            3: {'a_value': 10.0, 'b_value': 30.0},
        }

        for site in sites:
            expected = expected_by_id[site.id]
            self.assertAlmostEqual(expected['a_value'], site.a_value)
            self.assertAlmostEqual(expected['b_value'], site.b_value)

    def test_avg_aggregation(self):
        sites = models.Site.objects.with_avgs()
        expected_by_id = {
            1: {'a_value': 17.33, 'b_value': 65.33},
            2: {'a_value': 5.0, 'b_value': 15.0},
            3: {'a_value': 5.0, 'b_value': 15.0},
        }

        for site in sites:
            expected = expected_by_id[site.id]
            self.assertAlmostEqual(expected['a_value'], site.a_value, places=2)
            self.assertAlmostEqual(expected['b_value'], site.b_value, places=2)
