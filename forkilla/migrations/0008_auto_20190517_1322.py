# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-05-17 11:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forkilla', '0007_auto_20190517_1204'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='user',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='review',
            name='user',
            field=models.TextField(default=''),
        ),
    ]
