# Generated by Django 3.0.6 on 2020-06-10 23:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_user_is_hostel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_hostel',
        ),
    ]
