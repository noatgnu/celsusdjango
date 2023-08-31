# Generated by Django 4.1.1 on 2022-10-20 09:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('celsus', '0010_alter_rawdata_value'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='first_author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='first_authors', to='celsus.project'),
        ),
        migrations.DeleteModel(
            name='FirstAuthor',
        ),
    ]