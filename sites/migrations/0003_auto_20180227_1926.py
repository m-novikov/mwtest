# Generated by Django 2.0.2 on 2018-02-27 19:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0002_record_date'),
    ]

    operations = [
        migrations.AlterIndexTogether(
            name='record',
            index_together={('site', 'a_value', 'b_value')},
        ),
    ]
