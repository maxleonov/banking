# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cards',
            fields=[
                ('id', models.BigIntegerField(serialize=False, primary_key=True)),
                ('balance', models.BigIntegerField(default=0)),
                ('pin', models.CharField(max_length=32, verbose_name='PIN')),
                ('blocked', models.BooleanField(default=False)),
                ('pin_attempts_made', models.SmallIntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Operation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=50, verbose_name='Name', choices=[(b'Get cache', b'Get cache'), (b'View balance', b'View balance')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='OperationLog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField()),
                ('card', models.ForeignKey(to='cashmachine.Cards')),
                ('operation', models.ForeignKey(to='cashmachine.Operation')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
