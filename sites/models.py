from django.db import models


class Site(models.Model):
    name = models.CharField(verbose_name='Name', max_length=50)


class Record(models.Model):
    site = models.ForeignKey(
        Site, verbose_name='Site', related_name='records',
        on_delete=models.CASCADE
    )
    a_value = models.FloatField(verbose_name='A Value')
    b_value = models.FloatField(verbose_name='B Value')
