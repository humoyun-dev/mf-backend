# Generated by Django 5.0.3 on 2024-04-18 11:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loan', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loan',
            name='get_loan_date',
            field=models.DateField(default=datetime.datetime(2024, 4, 18, 16, 59, 30, 723951)),
        ),
    ]
