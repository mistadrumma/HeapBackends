# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-25 10:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0007_auto_20170625_1027'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='username',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
