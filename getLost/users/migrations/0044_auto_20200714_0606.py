# Generated by Django 3.0.6 on 2020-07-14 06:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0043_auto_20200714_0340'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='expected_arrival',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='expected_departure',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='reservation_date_time',
        ),
    ]