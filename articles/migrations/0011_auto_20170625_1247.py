# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-06-25 12:47
from __future__ import unicode_literals

from django.db import migrations
import tinymce_4.fields


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0010_auto_20170625_1214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='bodytext',
            field=tinymce_4.fields.TinyMCEModelField(blank=True, null=True, verbose_name='TinyMCEModelField'),
        ),
    ]
