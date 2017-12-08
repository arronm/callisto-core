# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-24 23:56
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('callisto_core.wizard_builder', '0033_add_temps'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='new_question',
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name='example2',
                to='wizard_builder.FormQuestion'),
        ),
    ]
