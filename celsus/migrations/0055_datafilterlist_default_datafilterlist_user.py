# Generated by Django 4.1.5 on 2023-02-17 12:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('celsus', '0054_datafilterlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='datafilterlist',
            name='default',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='datafilterlist',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='users', to=settings.AUTH_USER_MODEL),
        ),
    ]
