# Generated by Django 4.1.1 on 2022-11-05 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('celsus', '0022_differentialanalysisdata_peptide_sequence_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='ptm_data',
            field=models.BooleanField(default=False),
        ),
    ]
