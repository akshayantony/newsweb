# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-04 20:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0019_auto_20170830_0913'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='slug',
            field=models.SlugField(blank=True, max_length=60),
        ),
    ]
