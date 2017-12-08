# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-24 16:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('callisto_core.wizard_builder', '0027_textarea'),
    ]

    operations = [
        migrations.AddField(
            model_name='formquestion',
            name='type',
            field=models.TextField(
                choices=[
                    ('checkbox',
                     'checkbox'),
                    ('radiobutton',
                     'radiobutton'),
                    ('singlelinetext',
                     'singlelinetext'),
                    ('textarea',
                     'textarea')],
                null=True),
        ),
    ]
