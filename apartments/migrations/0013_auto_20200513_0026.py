# Generated by Django 3.0.5 on 2020-05-12 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apartments', '0012_auto_20200512_1553'),
    ]

    operations = [
        migrations.RenameField(
            model_name='flattypedetail',
            old_name='flat_type',
            new_name='flat_type_desc',
        ),
        migrations.AlterField(
            model_name='flattypedetail',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
