# Generated by Django 3.0.6 on 2020-07-14 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0037_reservation_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='created_at2',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
