# Generated by Django 3.0.6 on 2020-06-11 03:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_remove_user_is_hostel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='roomdetail',
            old_name='total_coed_rooms',
            new_name='total_beds',
        ),
        migrations.RenameField(
            model_name='roomdetail',
            old_name='total_rooms',
            new_name='total_coed_beds',
        ),
    ]