# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-24 23:56
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('callisto_core.wizard_builder', '0034d_move_choice_question'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='new_question',
            new_name='question',
        ),
    ]
