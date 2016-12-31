# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lights', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='light',
            name='motion_trigger_state',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='light',
            name='currentState',
            field=models.BooleanField(default=False),
        ),
    ]
