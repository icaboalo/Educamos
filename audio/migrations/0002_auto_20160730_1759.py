# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-30 17:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audio',
            name='file',
            field=models.FileField(upload_to='audios/'),
        ),
    ]
