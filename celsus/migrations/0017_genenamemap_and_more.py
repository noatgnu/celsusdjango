# Generated by Django 4.1.1 on 2022-10-28 10:57

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('celsus', '0016_remove_rawdata_project_rawdata_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='GeneNameMap',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('accession_id', models.TextField()),
                ('gene_names', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='differentialanalysisdata',
            name='gene_names',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='celsus.genenamemap'),
        ),
        migrations.AlterField(
            model_name='rawdata',
            name='gene_names',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='celsus.genenamemap'),
        ),
    ]
