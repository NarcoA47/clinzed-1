# Generated by Django 5.0 on 2023-12-21 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clean', '0008_checkout_pickup_time_pickup_pickup_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkout',
            name='pickup_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
