# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lights', '0002_auto_20161231_0307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='light',
            name='lastBeaconTime',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='light',
            name='name',
            field=models.CharField(default=b'unknown', max_length=64),
        ),
    ]
