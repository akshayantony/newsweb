# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-28 13:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0011_auto_20170828_1019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='images',
            field=models.ImageField(blank=True, null=True, upload_to=b'modelimages/'),
        ),
    ]
