# Generated by Django 3.0.6 on 2020-09-17 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0071_auto_20200917_0642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='account_type',
            field=models.CharField(choices=[('1', 'Hostel'), ('2', 'Traveler'), ('3', 'None')], default=None, max_length=255),
        ),
    ]
