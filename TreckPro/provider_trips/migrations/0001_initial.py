# Generated by Django 4.0.3 on 2022-07-13 11:10

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TripModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trip_id', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('trip_name', models.CharField(max_length=30)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('starting_destination', models.CharField(max_length=30)),
                ('ending_destination', models.CharField(max_length=30)),
                ('pickup_point', models.CharField(max_length=30)),
                ('droping_point', models.CharField(max_length=30)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('days', models.IntegerField()),
                ('budget', models.FloatField()),
                ('no_of_seats', models.IntegerField()),
                ('booked_seats', models.IntegerField()),
                ('pending_seats', models.IntegerField()),
                ('description', models.CharField(max_length=30)),
                ('is_active', models.BooleanField()),
            ],
        ),
    ]
