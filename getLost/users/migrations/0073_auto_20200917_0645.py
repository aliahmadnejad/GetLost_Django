# Generated by Django 3.0.6 on 2020-09-17 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0072_auto_20200917_0644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='account_type',
            field=models.CharField(choices=[('1', 'None'), ('2', 'Hostel'), ('3', 'Traveler')], default=1, max_length=255),
        ),
    ]
