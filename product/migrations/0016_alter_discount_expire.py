# Generated by Django 5.0.1 on 2024-01-15 19:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0015_product_price_discount_alter_discount_expire'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discount',
            name='expire',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 16, 19, 35, 1, 33337, tzinfo=datetime.timezone.utc)),
        ),
    ]
