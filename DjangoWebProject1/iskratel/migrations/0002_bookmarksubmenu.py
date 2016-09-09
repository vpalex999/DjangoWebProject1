# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-08 05:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('iskratel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='bookmarksubmenu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('namesub', models.CharField(max_length=30, unique=True)),
                ('nametabsubmenu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iskratel.bookmarks')),
            ],
        ),
    ]
