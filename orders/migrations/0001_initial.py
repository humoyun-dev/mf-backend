# Generated by Django 5.0.3 on 2024-03-24 11:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0003_productimage'),
        ('sellers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=600)),
                ('phone_number', models.CharField(max_length=12)),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sellers.seller')),
                ('products', models.ManyToManyField(to='product.product')),
            ],
        ),
    ]