# Generated by Django 3.0.6 on 2020-07-04 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0028_customerprofile_country'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customerprofile',
            old_name='emergency_contact',
            new_name='emergency_contact_phone',
        ),
        migrations.AddField(
            model_name='customerprofile',
            name='emergency_contact_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]