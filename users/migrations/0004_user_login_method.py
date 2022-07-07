# Generated by Django 2.2.5 on 2022-07-06 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20220705_2113'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='login_method',
            field=models.CharField(choices=[('email', 'Email'), ('github', 'Github'), ('facebook', 'Facebook')], default='email', max_length=10),
        ),
    ]
