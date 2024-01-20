# Generated by Django 4.2.7 on 2024-01-20 10:07

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0017_alter_category_options_alter_comment_options_and_more'),
        ('orders', '0005_alter_orderitem_product_alter_orderitem_quantity'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ('is_paid', '-updated_at'), 'verbose_name': 'Order', 'verbose_name_plural': 'Orders'},
        ),
        migrations.AlterModelOptions(
            name='orderitem',
            options={'verbose_name': 'OrderItem', 'verbose_name_plural': 'OrderItems'},
        ),
        migrations.AlterField(
            model_name='order',
            name='created_at',
            field=models.DateField(auto_now_add=True, verbose_name='created_at'),
        ),
        migrations.AlterField(
            model_name='order',
            name='delete_at',
            field=models.DateField(blank=True, null=True, verbose_name='delete_at'),
        ),
        migrations.AlterField(
            model_name='order',
            name='discount',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='product.discount', verbose_name='discount'),
        ),
        migrations.AlterField(
            model_name='order',
            name='is_deleted',
            field=models.BooleanField(default=False, verbose_name='is_deleted'),
        ),
        migrations.AlterField(
            model_name='order',
            name='is_paid',
            field=models.BooleanField(default=False, verbose_name='is paid'),
        ),
        migrations.AlterField(
            model_name='order',
            name='total',
            field=models.PositiveIntegerField(default=0, verbose_name='total'),
        ),
        migrations.AlterField(
            model_name='order',
            name='updated_at',
            field=models.DateField(auto_now=True, verbose_name='updated_at'),
        ),
        migrations.AlterField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orderitems', to='orders.order', verbose_name='order'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orderitems', to='product.product', verbose_name='product'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='quantity',
            field=models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1)], verbose_name='quantity'),
        ),
    ]
