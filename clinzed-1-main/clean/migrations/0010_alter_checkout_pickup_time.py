# Generated by Django 5.0 on 2023-12-21 03:24

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clean', '0009_alter_checkout_pickup_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkout',
            name='pickup_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
