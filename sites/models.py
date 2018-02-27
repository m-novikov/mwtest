from django.db import models


class SiteQueryset(models.QuerySet):
    def with_sums(self):
        return self.annotate(
            a_value=models.Sum('records__a_value'),
            b_value=models.Sum('records__b_value'),
        )

    def with_avgs(self):
        return self.raw(
            'SELECT * '
            ',AVG(rec.a_value) as a_value '
            ',AVG(rec.b_value) as b_value '
            'FROM sites_site as site, sites_record as rec '
            'WHERE rec.site_id = site.id '
            'GROUP BY site.id '
        )


class Site(models.Model):
    name = models.CharField(verbose_name='Name', max_length=50)

    objects = SiteQueryset.as_manager()

    def __str__(self):
        return self.name


class Record(models.Model):
    site = models.ForeignKey(
        Site, verbose_name='Site', related_name='records',
        on_delete=models.CASCADE
    )
    date = models.DateField(verbose_name='Date')
    a_value = models.FloatField(verbose_name='A Value')
    b_value = models.FloatField(verbose_name='B Value')

    def __str__(self):
        return '%s %s' % (self.site, self.date)

    class Meta:
        index_together = ('site', 'a_value', 'b_value')
