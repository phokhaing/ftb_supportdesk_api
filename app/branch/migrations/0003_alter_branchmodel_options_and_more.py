# Generated by Django 4.0.6 on 2023-01-11 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('branch', '0002_branchmodel_address_en_branchmodel_address_kh_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='branchmodel',
            options={'managed': True, 'verbose_name': 'Branch', 'verbose_name_plural': 'Branches'},
        ),
        migrations.AlterField(
            model_name='branchmodel',
            name='address_en',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='branchmodel',
            name='address_kh',
            field=models.TextField(max_length=500),
        ),
    ]
