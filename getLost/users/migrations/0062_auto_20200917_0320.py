# Generated by Django 3.0.6 on 2020-09-17 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0061_auto_20200917_0318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_hostel',
            field=models.BooleanField(default=False),
        ),
    ]
