# Generated by Django 3.2.16 on 2023-04-27 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20230427_1514'),
    ]

    operations = [
        migrations.AlterField(
            model_name='construction',
            name='name',
            field=models.CharField(max_length=1024, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='constructionstage',
            name='name',
            field=models.CharField(max_length=1024, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='locality',
            name='name',
            field=models.CharField(max_length=1024, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='manager',
            name='name',
            field=models.CharField(max_length=1024),
        ),
        migrations.AlterField(
            model_name='manager',
            name='surname',
            field=models.CharField(max_length=1024),
        ),
        migrations.AlterField(
            model_name='source',
            name='name',
            field=models.CharField(max_length=1024, unique=True),
        ),
        migrations.AlterField(
            model_name='status',
            name='name',
            field=models.CharField(max_length=1024, unique=True),
        ),
    ]
