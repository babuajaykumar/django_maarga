# Generated by Django 3.0.5 on 2020-05-12 08:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apartments', '0003_auto_20200506_0055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flattypedetails',
            name='list_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 5, 12, 14, 6, 15, 164511)),
        ),
    ]
