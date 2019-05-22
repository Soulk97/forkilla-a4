# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2019-04-03 17:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('restaurant_number', models.CharField(max_length=8, unique=True)),
                ('name', models.CharField(max_length=50)),
                ('menu_description', models.TextField()),
                ('price_average', models.DecimalField(decimal_places=2, max_digits=5)),
                ('is_promot', models.BooleanField()),
                ('rate', models.DecimalField(decimal_places=1, max_digits=3)),
                ('address', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('featured_photo', models.ImageField(upload_to='')),
                ('category', models.CharField(choices=[('Rice', 'Rice'), ('Fusi', 'Fusion'), ('BBQ', 'Barbecue'), ('Chin', 'Chinese'), ('Medi', 'Mediterranean'), ('Crep', 'Creperie'), ('Hind', 'Hindu'), ('Japa', 'Japanese'), ('Ital', 'Italian'), ('Mexi', 'Mexican'), ('Peru', 'Peruvian'), ('Russ', 'Russian'), ('Turk', 'Turkish'), ('Basq', 'Basque'), ('Vegy', 'Vegetarian'), ('Afri', 'African'), ('Egyp', 'Egyptian'), ('Grek', 'Greek')], max_length=5)),
                ('restaurant_capacity', models.PositiveIntegerField(max_length=3)),
            ],
        ),
    ]
