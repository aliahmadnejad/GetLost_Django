# Generated by Django 3.0.6 on 2020-09-17 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0064_auto_20200917_0345'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='account_type',
            field=models.CharField(default=False, max_length=255),
        ),
    ]
