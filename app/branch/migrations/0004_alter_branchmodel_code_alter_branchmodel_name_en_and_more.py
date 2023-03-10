# Generated by Django 4.0.6 on 2023-01-11 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('branch', '0003_alter_branchmodel_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branchmodel',
            name='code',
            field=models.CharField(max_length=9, unique=True),
        ),
        migrations.AlterField(
            model_name='branchmodel',
            name='name_en',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='branchmodel',
            name='name_kh',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
