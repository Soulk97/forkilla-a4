# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2019-05-15 18:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forkilla', '0004_auto_20190514_0108'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('ratio', models.CharField(choices=[('one_star', '1'), ('two_stars', '2'), ('three_stars', '3'), ('four_stars', '4'), ('five_stars', '5')], max_length=5)),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forkilla.Restaurant')),
            ],
        ),
    ]
