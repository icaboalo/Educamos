# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-30 07:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='state',
            field=models.IntegerField(choices=[(1, ''), (2, ''), (3, ''), (4, ''), (5, ''), (6, ''), (7, ''), (8, ''), (9, ''), (10, ''), (11, ''), (12, ''), (13, ''), (14, ''), (15, ''), (16, ''), (17, ''), (18, ''), (19, ''), (20, ''), (21, ''), (22, ''), (23, ''), (24, ''), (25, ''), (26, ''), (27, ''), (28, ''), (29, ''), (30, ''), (31, ''), (32, '')], max_length=15),
        ),
    ]
