# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-07 18:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('callisto_core.wizard_builder', '0018_remove_multilinetext'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='extra_info_placeholder',
        ),
    ]
