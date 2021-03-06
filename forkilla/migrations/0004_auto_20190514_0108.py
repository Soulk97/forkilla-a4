# Generated by Django 2.1.2 on 2019-05-13 23:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forkilla', '0003_reservation'),
    ]

    operations = [
        migrations.CreateModel(
            name='RestaurantInsertDate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forkilla.Restaurant')),
            ],
            options={
                'ordering': ['-date_added'],
            },
        ),
        migrations.CreateModel(
            name='ViewedRestaurants',
            fields=[
                ('id_vr', models.AutoField(primary_key=True, serialize=False)),
                ('restaurant', models.ManyToManyField(through='forkilla.RestaurantInsertDate', to='forkilla.Restaurant')),
            ],
        ),
        migrations.AddField(
            model_name='restaurantinsertdate',
            name='viewedrestaurants',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forkilla.ViewedRestaurants'),
        ),
    ]
