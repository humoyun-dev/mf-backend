# Generated by Django 5.0.3 on 2024-03-23 09:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='status_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='users.status'),
        ),
    ]