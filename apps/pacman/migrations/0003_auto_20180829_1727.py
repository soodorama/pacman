# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-08-29 17:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pacman', '0002_auto_20180827_0754'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.CharField(default='email', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='top_score',
            field=models.IntegerField(default=0),
        ),
    ]
