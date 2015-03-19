# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cashmachine', '0003_auto_20150318_0903'),
    ]

    operations = [
        migrations.RenameField(
            model_name='operationlog',
            old_name='balance_afer_operation',
            new_name='balance_after_operation',
        ),
    ]
