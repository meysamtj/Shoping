# Generated by Django 4.2.7 on 2024-01-12 13:39

from django.db import migrations, models
import product.models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_alter_discount_amount_alter_discount_discount_code_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discount',
            name='amount',
            field=models.PositiveIntegerField(validators=[product.models.Discount.amount_check]),
        ),
    ]
