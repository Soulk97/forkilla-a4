# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-05-21 12:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forkilla', '0008_auto_20190517_1322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='featured_photo',
            field=models.ImageField(upload_to='static/photos'),
        ),
    ]
