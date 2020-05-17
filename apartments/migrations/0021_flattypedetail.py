# Generated by Django 3.0.5 on 2020-05-16 11:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apartments', '0020_delete_flattypedetail'),
    ]

    operations = [
        migrations.CreateModel(
            name='FlatTypeDetail',
            fields=[
                ('flat_type', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='apartments.FlatType')),
                ('sqft', models.IntegerField()),
                ('bedrooms', models.IntegerField()),
                ('bathrooms', models.DecimalField(decimal_places=1, max_digits=2)),
                ('price', models.IntegerField(default=0)),
                ('dining_hall', models.BooleanField(default=False)),
                ('description', models.TextField(blank=True)),
                ('photo_main', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('isometric_view', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('floor_plan', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('photo_3', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_4', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_5', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_6', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('is_published', models.BooleanField(default=True)),
            ],
            options={
                'unique_together': {('flat_type', 'sqft')},
                'index_together': {('flat_type', 'sqft')},
            },
        ),
    ]
