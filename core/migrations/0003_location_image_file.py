# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-22 10:07
from __future__ import unicode_literals

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20170111_0812'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='image_file',
            field=models.ImageField(blank=True, null=True, upload_to=core.models.upload_to_location),
        ),
    ]
