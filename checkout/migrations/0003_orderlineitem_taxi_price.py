# Generated by Django 3.2.5 on 2024-08-07 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_order_taxi_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderlineitem',
            name='taxi_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
    ]
