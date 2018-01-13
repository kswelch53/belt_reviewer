# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-30 01:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app_one', '0002_auto_20171229_1851'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('review', models.TextField()),
                ('rating', models.CharField(max_length=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('adds_book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to='app_one.User')),
                ('adds_review', models.ManyToManyField(related_name='reviews', to='app_one.User')),
            ],
        ),
    ]