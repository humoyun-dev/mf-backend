# Generated by Django 5.0.4 on 2024-05-05 00:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_alter_product_category_alter_productimage_image'),
        ('shop', '0003_shop_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='shop',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='shop', to='shop.shop'),
        ),
    ]
