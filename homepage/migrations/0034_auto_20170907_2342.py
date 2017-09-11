# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-07 18:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0033_auto_20170907_2331'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='modelimages/')),
            ],
        ),
        migrations.RemoveField(
            model_name='news',
            name='file',
        ),
    ]