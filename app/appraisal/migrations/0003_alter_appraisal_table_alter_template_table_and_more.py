# Generated by Django 4.0.6 on 2023-01-02 08:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appraisal', '0002_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='appraisal',
            table='ftb_epa_appraisal',
        ),
        migrations.AlterModelTable(
            name='template',
            table='ftb_epa_template',
        ),
        migrations.AlterModelTable(
            name='type',
            table='ftb_epa_type',
        ),
    ]
