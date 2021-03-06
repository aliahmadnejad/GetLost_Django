# Generated by Django 3.0.6 on 2020-07-07 04:03

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0031_auto_20200707_0401'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerprofile',
            name='country',
            field=django_countries.fields.CountryField(max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='customerprofile',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='pictures'),
        ),
    ]
