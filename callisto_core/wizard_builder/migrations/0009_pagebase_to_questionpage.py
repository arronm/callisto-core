# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-02 21:54
from __future__ import unicode_literals

from django.db import migrations, models


def copy_to_question_page(apps, schema_editor):
    current_database = schema_editor.connection.alias
    QuestionPage = apps.get_model('callisto_core.wizard_builder.QuestionPage')
    for page in QuestionPage.objects.using(current_database):
        page.new_position = page.position
        page.new_section = page.section
        for site in page.sites.all():
            page.new_sites.add(site)
        page.save()


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0002_alter_domain_unique'),
        ('callisto_core.wizard_builder', '0008_remove_textpage'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionpage',
            name='new_position',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='position'),
        ),
        migrations.AddField(
            model_name='questionpage',
            name='new_section',
            field=models.IntegerField(choices=[(1, 'When'), (2, 'Where'), (3, 'What'), (4, 'Who')], default=1),
        ),
        migrations.AddField(
            model_name='questionpage',
            name='new_sites',
            field=models.ManyToManyField(to='sites.Site'),
        ),
        migrations.RunPython(
            copy_to_question_page,
            reverse_code=migrations.RunPython.noop,
        ),
    ]
