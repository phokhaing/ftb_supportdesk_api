# Generated by Django 4.0.6 on 2023-01-11 04:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_management', '0041_alter_user_date_joined'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 11, 11, 22, 36, 347447)),
        ),
    ]