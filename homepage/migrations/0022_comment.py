# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-06 06:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0021_remove_news_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('news', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homepage.News')),
            ],
        ),
    ]
