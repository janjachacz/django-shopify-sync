# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-06-22 18:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopify_sync', '0014_auto_20160622_1547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variant',
            name='title',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
