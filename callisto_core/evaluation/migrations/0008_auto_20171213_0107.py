# Generated by Django 2.0 on 2017-12-13 01:07

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0039_auto_20171208_0039'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('evaluation', '0007_auto_20171212_1756'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='evalrow',
            name='record_identifier',
        ),
        migrations.RemoveField(
            model_name='evalrow',
            name='user_identifier',
        ),
        migrations.AddField(
            model_name='evalrow',
            name='record',
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to='delivery.Report'),
        ),
        migrations.AddField(
            model_name='evalrow',
            name='user',
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL),
        ),
    ]
