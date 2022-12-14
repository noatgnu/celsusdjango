# Generated by Django 4.1.1 on 2022-11-29 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('celsus', '0034_file_file_parameters'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='genenamemap',
            name='uniprot_record',
        ),
        migrations.AddField(
            model_name='genenamemap',
            name='uniprot_record',
            field=models.ManyToManyField(related_name='gene_map', to='celsus.uniprotrecord'),
        ),
    ]
