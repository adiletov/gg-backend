# Generated by Django 4.2.21 on 2025-06-01 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0006_car_vin'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='year',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
