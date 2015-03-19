# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cashmachine', '0004_auto_20150318_0904'),
    ]

    operations = [
        migrations.CreateModel(
            name='LogRecord',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField()),
                ('amount', models.BigIntegerField(default=None)),
                ('balance_after_operation', models.BigIntegerField(default=None)),
                ('card', models.ForeignKey(to='cashmachine.Card')),
                ('operation', models.ForeignKey(to='cashmachine.Operation')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='operationlog',
            name='card',
        ),
        migrations.RemoveField(
            model_name='operationlog',
            name='operation',
        ),
        migrations.DeleteModel(
            name='OperationLog',
        ),
        migrations.AlterField(
            model_name='operation',
            name='name',
            field=models.CharField(unique=True, max_length=50, verbose_name='Name', choices=[(b'Get cash', b'Get cash'), (b'View balance', b'View balance')]),
            preserve_default=True,
        ),
    ]
