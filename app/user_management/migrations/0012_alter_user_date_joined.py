# Generated by Django 4.0.6 on 2022-11-25 10:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_management', '0011_alter_user_date_joined'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 25, 10, 6, 4, 322962)),
        ),
    ]
