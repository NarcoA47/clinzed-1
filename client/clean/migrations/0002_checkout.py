# Generated by Django 5.0 on 2023-12-12 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clean', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Checkout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('area', models.CharField(max_length=255)),
                ('pickup_choice', models.CharField(choices=[('one-time', 'One-time Pickup'), ('subscription', 'Subscription')], max_length=20)),
            ],
        ),
    ]
