# Generated by Django 3.0.6 on 2020-09-09 05:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0056_auto_20200827_2313'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='roomdetail',
            name='balance',
        ),
        migrations.RemoveField(
            model_name='roomdetail',
            name='balance_currency',
        ),
    ]
