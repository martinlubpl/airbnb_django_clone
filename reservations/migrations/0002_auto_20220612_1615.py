# Generated by Django 2.2.5 on 2022-06-12 14:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reservation',
            old_name='STATUS',
            new_name='status',
        ),
    ]
