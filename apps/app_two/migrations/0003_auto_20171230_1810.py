# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-31 00:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_two', '0002_auto_20171230_1516'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='rating',
            new_name='add_rating',
        ),
    ]