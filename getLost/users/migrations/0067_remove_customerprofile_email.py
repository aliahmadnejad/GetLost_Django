# Generated by Django 3.0.6 on 2020-09-17 05:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0066_auto_20200917_0423'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customerprofile',
            name='email',
        ),
    ]
