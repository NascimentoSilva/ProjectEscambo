# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-19 05:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escambo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='height_field',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='post',
            name='width_field',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, height_field='height_field', null=True, upload_to='', verbose_name='Upload da Imagem:', width_field='width_field'),
        ),
        migrations.AlterField(
            model_name='post',
            name='published_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Data de Publicação:'),
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.TextField(max_length=1000, verbose_name='Descrição:'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Nome do Livro:'),
        ),
        migrations.AlterField(
            model_name='post',
            name='user',
            field=models.CharField(max_length=15, verbose_name='Usuário:'),
        ),
    ]
