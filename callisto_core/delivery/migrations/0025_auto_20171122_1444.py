# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-22 14:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0024a_copy_attrs'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sentfullreport',
            name='report',
        ),
    ]
