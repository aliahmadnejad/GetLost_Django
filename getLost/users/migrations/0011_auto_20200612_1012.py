# Generated by Django 3.0.6 on 2020-06-12 10:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_auto_20200612_0955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roomdetail',
            name='hostel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Profile'),
        ),
    ]