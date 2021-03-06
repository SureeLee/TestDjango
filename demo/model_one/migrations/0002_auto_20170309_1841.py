# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-09 10:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('model_one', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='publisher',
            options={'verbose_name': '出版商', 'verbose_name_plural': '出版商'},
        ),
        migrations.AddField(
            model_name='book',
            name='price',
            field=models.DecimalField(decimal_places=2, default=10, max_digits=5),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='name',
            field=models.CharField(max_length=30, verbose_name='名称'),
        ),
    ]
