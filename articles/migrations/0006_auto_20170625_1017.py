# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-25 10:17
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_auto_20170625_1014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, to_field='username'),
        ),
    ]
