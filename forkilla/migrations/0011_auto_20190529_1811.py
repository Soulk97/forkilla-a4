# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2019-05-29 16:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forkilla', '0010_auto_20190522_1610'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='featured_photo',
            field=models.CharField(max_length=300),
        ),
    ]