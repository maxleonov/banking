# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('cashmachine', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigIntegerField(serialize=False, primary_key=True, validators=[django.core.validators.RegexValidator(regex=b'[0-9]{16}')])),
                ('pin', models.CharField(max_length=32, verbose_name='PIN', validators=[django.core.validators.RegexValidator(regex=b'[0-9]{4}')])),
                ('balance', models.BigIntegerField(default=0)),
                ('blocked', models.BooleanField(default=False)),
                ('pin_attempts_made', models.SmallIntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='operationlog',
            name='card',
            field=models.ForeignKey(to='cashmachine.Card'),
            preserve_default=True,
        ),
        migrations.DeleteModel(
            name='Cards',
        ),
    ]
