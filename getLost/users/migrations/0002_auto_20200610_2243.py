# Generated by Django 3.0.6 on 2020-06-10 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_hostel',
            field=models.BooleanField(default=True),
        ),
    ]
