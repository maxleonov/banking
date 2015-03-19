# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cashmachine', '0002_auto_20150317_2234'),
    ]

    operations = [
        migrations.AddField(
            model_name='operationlog',
            name='amount',
            field=models.BigIntegerField(default=None),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='operationlog',
            name='balance_afer_operation',
            field=models.BigIntegerField(default=None),
            preserve_default=True,
        ),
    ]
