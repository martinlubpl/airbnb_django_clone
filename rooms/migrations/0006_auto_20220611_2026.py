# Generated by Django 2.2.5 on 2022-06-11 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0005_auto_20220611_2005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='amenities',
            field=models.ManyToManyField(blank=True, related_name='rooms', to='rooms.Amenity'),
        ),
        migrations.AlterField(
            model_name='room',
            name='facilities',
            field=models.ManyToManyField(blank=True, related_name='rooms', to='rooms.Facility'),
        ),
        migrations.AlterField(
            model_name='room',
            name='house_rules',
            field=models.ManyToManyField(blank=True, related_name='rooms', to='rooms.HouseRule'),
        ),
    ]
