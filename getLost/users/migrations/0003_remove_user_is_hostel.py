# Generated by Django 3.0.6 on 2020-06-10 22:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200610_2243'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_hostel',
        ),
    ]
