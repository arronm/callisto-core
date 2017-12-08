# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-02 22:46
from __future__ import unicode_literals

from django.db import migrations, models


def copy_questionpage_to_page(apps, schema_editor):
    current_database = schema_editor.connection.alias
    QuestionPage = apps.get_model('callisto_core.wizard_builder.QuestionPage')
    for question_page in QuestionPage.objects.using(current_database):
        with schema_editor.connection.cursor() as cursor:
            cursor.execute(
                'INSERT INTO "wizard_builder_page" ("id", "position", "section", "infobox") VALUES (%s, %s, %s, %s)', [
                    question_page.id, question_page.position, question_page.section, question_page.infobox], )
            for site in question_page.sites.all():
                cursor.execute(
                    'INSERT INTO "wizard_builder_page_sites" ("page_id", "site_id") VALUES (%s, %s)', [
                        question_page.id, site.id], )


def delete_page_rows(apps, schema_editor):
    current_database = schema_editor.connection.alias
    Page = apps.get_model('callisto_core.wizard_builder.Page')
    Page.objects.using(current_database).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('callisto_core.wizard_builder', '0012_questionpage_to_page'),
    ]

    operations = [
        migrations.RunPython(
            copy_questionpage_to_page,
            delete_page_rows,
        ),
    ]
