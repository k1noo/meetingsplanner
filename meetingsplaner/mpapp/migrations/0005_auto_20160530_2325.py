# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-30 23:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mpapp', '0004_auto_20160530_2324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='FinishTime',
            field=models.TimeField(),
        ),
    ]