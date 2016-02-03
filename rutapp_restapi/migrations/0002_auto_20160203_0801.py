# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rutapp_restapi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='walk',
            name='duration',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='walk',
            name='features',
            field=models.TextField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='walk',
            name='history',
            field=models.TextField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='walk',
            name='lunch_tea',
            field=models.TextField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='walk',
            name='walk_options',
            field=models.TextField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='walk',
            name='travel_info',
            field=models.TextField(null=True),
            preserve_default=True,
        ),
    ]
