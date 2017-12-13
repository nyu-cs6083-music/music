# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0004_auto_20171212_0946'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='play_count',
            field=models.IntegerField(default=0),
        ),
    ]
