# Generated by Django 3.0.6 on 2020-06-30 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0019_roomdetail_total_bed_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roomdetail',
            name='price',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]