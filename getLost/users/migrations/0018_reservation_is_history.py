# Generated by Django 3.0.6 on 2020-06-24 01:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0017_auto_20200613_2220'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='is_history',
            field=models.BooleanField(default=False),
        ),
    ]