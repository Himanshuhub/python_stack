# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-20 21:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='cost',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='weight',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
