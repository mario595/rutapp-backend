# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rutapp_restapi', '0002_auto_20160203_0801'),
    ]

    operations = [
        migrations.AddField(
            model_name='walk',
            name='source',
            field=models.URLField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='walk',
            name='source_text',
            field=models.CharField(max_length=100, null=True),
            preserve_default=True,
        ),
    ]
