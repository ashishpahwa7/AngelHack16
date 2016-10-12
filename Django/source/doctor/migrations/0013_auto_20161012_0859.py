# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2016-10-12 08:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0012_auto_20161012_0855'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctoral',
            name='timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='doctoral',
            name='updated',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='doctoral',
            name='Doctor_Email_id',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='doctoral',
            name='Doctor_Name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='doctoral',
            name='Doctor_Password',
            field=models.CharField(max_length=30),
        ),
    ]
