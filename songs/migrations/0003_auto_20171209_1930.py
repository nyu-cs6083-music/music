# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-10 00:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0002_auto_20171209_1247'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='year_released',
            field=models.DateField(auto_now=True, max_length=8),
        ),
        migrations.AlterField(
            model_name='song',
            name='artists',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='song', to='artists.Artist'),
        ),
    ]