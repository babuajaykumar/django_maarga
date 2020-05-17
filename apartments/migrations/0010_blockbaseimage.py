# Generated by Django 3.0.5 on 2020-05-12 08:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apartments', '0009_auto_20200512_1419'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlockBaseImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Number_of_flats', models.IntegerField()),
                ('block_flat_type', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='apartments.FlatTypeDetail')),
                ('block_name', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='apartments.BlockType')),
            ],
        ),
    ]