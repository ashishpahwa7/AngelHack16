# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-10-12 06:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0007_auto_20161011_1858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctoral',
            name='Doctor_Email_id',
            field=models.CharField(blank=True, default=None, max_length=30, null=True),
        ),
    ]