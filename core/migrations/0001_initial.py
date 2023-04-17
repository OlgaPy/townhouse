# Generated by Django 3.2.16 on 2023-04-17 18:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=1024, null=True)),
                ('link_conversation', models.CharField(max_length=4096, null=True)),
                ('name', models.CharField(blank=True, max_length=1024, null=True)),
                ('surname', models.CharField(blank=True, max_length=1024, null=True)),
                ('middle_name', models.CharField(blank=True, max_length=1024, null=True)),
                ('comment', models.CharField(blank=True, max_length=4096, null=True)),
            ],
            options={
                'db_table': 'client',
            },
        ),
        migrations.CreateModel(
            name='Construction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1024, null=True)),
                ('schema_path', models.CharField(max_length=1024, null=True)),
                ('floor', models.IntegerField(null=True)),
                ('rooms', models.IntegerField(null=True)),
                ('square_house', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'construction',
            },
        ),
        migrations.CreateModel(
            name='ConstructionStage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1024, null=True)),
            ],
            options={
                'db_table': 'construction_stage',
            },
        ),
        migrations.CreateModel(
            name='Locality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1024, null=True)),
            ],
            options={
                'db_table': 'locality',
            },
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=1024, null=True)),
                ('surname', models.CharField(blank=True, max_length=1024, null=True)),
                ('middle_name', models.CharField(blank=True, max_length=1024, null=True)),
                ('level', models.CharField(blank=True, max_length=1024, null=True)),
                ('substitute', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.manager')),
            ],
            options={
                'db_table': 'manager',
            },
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1024, null=True)),
                ('is_active', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'source',
            },
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1024, null=True)),
            ],
            options={
                'db_table': 'status',
            },
        ),
        migrations.CreateModel(
            name='TownHouse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=1024, null=True)),
                ('owner', models.CharField(max_length=1024, null=True)),
                ('square_area', models.IntegerField(blank=True, null=True)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('buyer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.client')),
                ('construction', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.construction')),
                ('construction_stage', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.constructionstage')),
                ('location', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.locality')),
                ('manager', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.manager')),
            ],
            options={
                'db_table': 'town_house',
            },
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=1024, null=True)),
                ('filepath', models.CharField(blank=True, max_length=1024, null=True)),
                ('building', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.townhouse')),
                ('client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.client')),
                ('manager', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.manager')),
            ],
            options={
                'db_table': 'document',
            },
        ),
        migrations.AddField(
            model_name='client',
            name='manager',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.manager'),
        ),
        migrations.AddField(
            model_name='client',
            name='object_property',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.townhouse'),
        ),
        migrations.AddField(
            model_name='client',
            name='source',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.source'),
        ),
        migrations.AddField(
            model_name='client',
            name='status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.status'),
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1024, null=True)),
                ('phone', models.CharField(max_length=1024, null=True)),
                ('email', models.CharField(max_length=1024, null=True)),
                ('is_active', models.BooleanField(default=False)),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.source')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.status')),
            ],
            options={
                'db_table': 'card',
            },
        ),
    ]
