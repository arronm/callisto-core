# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-22 18:08
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('callisto_core.wizard_builder', '0044_auto_20171101_1412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formquestion',
            name='page',
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to='wizard_builder.Page'),
        ),
    ]
