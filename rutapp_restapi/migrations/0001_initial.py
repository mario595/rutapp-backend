# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Walk',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('difficulty', models.IntegerField()),
                ('region', models.CharField(max_length=100)),
                ('length', models.DecimalField(max_digits=5, decimal_places=2)),
                ('travel_info', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
