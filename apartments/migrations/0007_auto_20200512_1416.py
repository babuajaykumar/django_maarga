# Generated by Django 3.0.5 on 2020-05-12 08:46

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apartments', '0006_auto_20200512_1411'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flattypedetail',
            name='list_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 5, 12, 14, 16, 50, 331761)),
        ),
        migrations.CreateModel(
            name='UnitFlats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('is_available', models.BooleanField(default=True)),
                ('Facing', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('car_parking', models.BooleanField(default=True)),
                ('block_name', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='apartments.BlockType')),
                ('floor_number', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='apartments.FloorRangeAllocation')),
                ('unit_flat_type', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='apartments.FlatTypeDetail')),
            ],
        ),
    ]
