# Generated by Django 3.0.6 on 2020-07-14 03:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0042_auto_20200714_0337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False, null=True),
        ),
    ]