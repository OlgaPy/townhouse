# Generated by Django 3.2.16 on 2023-04-27 15:08

import core.utils.util
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_document_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='filepath',
        ),
        migrations.AddField(
            model_name='client',
            name='login',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AddField(
            model_name='document',
            name='date_add',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='manager',
            name='login',
            field=models.CharField(blank=True, max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='document',
            name='file',
            field=models.FileField(upload_to=core.utils.util.get_document_file_path),
        ),
    ]
