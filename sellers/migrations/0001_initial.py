# Generated by Django 5.0.3 on 2024-03-23 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=12)),
                ('password', models.CharField(max_length=255)),
                ('profile_picture', models.ImageField(upload_to='sellers-profiles/')),
            ],
        ),
    ]
