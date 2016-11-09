# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-30 23:24
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mpapp', '0003_meetings_members'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='BusyTime',
            field=models.CharField(default=datetime.datetime(2016, 5, 30, 23, 23, 59, 494816, tzinfo=utc), max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='FinishTime',
            field=models.TimeField(auto_now=True, default=datetime.datetime(2016, 5, 30, 23, 24, 19, 713480, tzinfo=utc)),
            preserve_default=False,
        ),
    ]