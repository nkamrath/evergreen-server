# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lights', '0003_auto_20161231_0535'),
    ]

    operations = [
        migrations.RenameField(
            model_name='light',
            old_name='autoOffTimeSeconds',
            new_name='auto_off_time_seconds',
        ),
        migrations.RenameField(
            model_name='light',
            old_name='currentState',
            new_name='current_state',
        ),
        migrations.RenameField(
            model_name='light',
            old_name='ipAddress',
            new_name='ip_address',
        ),
        migrations.RenameField(
            model_name='light',
            old_name='lastBeaconTime',
            new_name='last_beacon_time',
        ),
    ]
