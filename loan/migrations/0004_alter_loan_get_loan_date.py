# Generated by Django 5.0.4 on 2024-04-28 07:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loan', '0003_alter_loan_get_loan_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loan',
            name='get_loan_date',
            field=models.DateField(default=datetime.datetime(2024, 4, 28, 7, 6, 55, 582898)),
        ),
    ]
