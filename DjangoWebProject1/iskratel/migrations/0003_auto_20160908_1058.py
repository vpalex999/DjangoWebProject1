# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-08 05:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('iskratel', '0002_bookmarksubmenu'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookmarksubmenu',
            name='nametabsubmenu',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='iskratel.bookmarks'),
        ),
    ]
