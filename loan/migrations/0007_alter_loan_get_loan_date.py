# Generated by Django 5.0.4 on 2024-05-05 00:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loan', '0006_alter_loan_get_loan_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loan',
            name='get_loan_date',
            field=models.DateField(default=datetime.datetime(2024, 5, 5, 0, 17, 17, 266382)),
        ),
    ]