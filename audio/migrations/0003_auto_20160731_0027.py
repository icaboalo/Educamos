# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-31 00:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audio', '0002_auto_20160730_1759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audio',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='audios/'),
        ),
    ]
