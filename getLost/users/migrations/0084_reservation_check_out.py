# Generated by Django 3.0.6 on 2021-06-11 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0083_customerprofile_stripe_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='check_out',
            field=models.DateField(blank=True, null=True),
        ),
    ]
