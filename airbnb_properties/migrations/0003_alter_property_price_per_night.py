# Generated by Django 3.2.5 on 2024-08-07 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airbnb_properties', '0002_alter_property_price_per_night'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='price_per_night',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
