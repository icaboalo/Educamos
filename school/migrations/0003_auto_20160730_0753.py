# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-30 07:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0002_auto_20160730_0733'),
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.IntegerField(choices=[(1, 'Lunes'), (2, 'Martes'), (3, 'Miercoles'), (4, 'Jueves'), (5, 'Viernes')])),
                ('start_hour', models.TimeField()),
                ('end_hour', models.TimeField()),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.Subject')),
            ],
            options={
                'verbose_name': 'Schedule',
                'verbose_name_plural': 'Schedules',
            },
        ),
        migrations.AlterField(
            model_name='school',
            name='state',
            field=models.IntegerField(choices=[(1, ''), (2, ''), (3, ''), (4, ''), (5, ''), (6, ''), (7, ''), (8, ''), (9, ''), (10, ''), (11, ''), (12, ''), (13, ''), (14, ''), (15, ''), (16, ''), (17, ''), (18, ''), (19, ''), (20, ''), (21, ''), (22, ''), (23, ''), (24, ''), (25, ''), (26, ''), (27, ''), (28, ''), (29, ''), (30, ''), (31, ''), (32, '')]),
        ),
    ]