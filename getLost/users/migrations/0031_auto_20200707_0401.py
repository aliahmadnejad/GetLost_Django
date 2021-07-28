# Generated by Django 3.0.6 on 2020-07-07 04:01

from django.db import migrations, models
import django_countries.fields
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0030_auto_20200707_0356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerprofile',
            name='country',
            field=django_countries.fields.CountryField(default='None Selected', max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='customerprofile',
            name='email',
            field=models.EmailField(blank=True, default='example@gmail.com', max_length=255, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='customerprofile',
            name='emergency_contact_name',
            field=models.CharField(blank=True, default='John Smith', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='customerprofile',
            name='emergency_contact_phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, default='John Smith', max_length=20, null=True, region=None),
        ),
        migrations.AlterField(
            model_name='customerprofile',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, default='e.g. +12125552368', max_length=20, null=True, region=None),
        ),
    ]
