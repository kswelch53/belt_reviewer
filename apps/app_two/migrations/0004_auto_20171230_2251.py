# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-31 04:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_two', '0003_auto_20171230_1810'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='add_rating',
            new_name='rating',
        ),
        migrations.RenameField(
            model_name='review',
            old_name='add_review',
            new_name='review',
        ),
        migrations.RemoveField(
            model_name='book',
            name='rating',
        ),
        migrations.RemoveField(
            model_name='book',
            name='review',
        ),
    ]
