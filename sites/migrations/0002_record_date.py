# Generated by Django 2.0.2 on 2018-02-25 20:01

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='date',
            field=models.DateField(default=datetime.datetime(2018, 2, 25, 20, 1, 46, 33618, tzinfo=utc), verbose_name='Date'),
            preserve_default=False,
        ),
    ]
