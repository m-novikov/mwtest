from django.db import models


class Site(models.Model):
    name = models.CharField(verbose_name='Name', max_length=50)

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
