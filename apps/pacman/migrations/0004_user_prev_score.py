# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-08-30 19:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pacman', '0003_auto_20180829_1727'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='prev_score',
            field=models.IntegerField(default=0),
        ),
    ]
