# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-19 06:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escambo', '0002_auto_20161219_0505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='height_field',
            field=models.IntegerField(default=100),
        ),
        migrations.AlterField(
            model_name='post',
            name='width_field',
            field=models.IntegerField(default=50),
        ),
    ]
