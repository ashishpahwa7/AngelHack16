# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2016-10-12 08:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0010_auto_20161012_0850'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctoral',
            name='updated',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
