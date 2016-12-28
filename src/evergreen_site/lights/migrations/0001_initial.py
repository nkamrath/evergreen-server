# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Light',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ipAddress', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=64)),
                ('currentState', models.CharField(max_length=10)),
                ('autoOffTimeSeconds', models.IntegerField(default=0)),
                ('lastBeaconTime', models.DateField(auto_now=True)),
            ],
        ),
    ]
