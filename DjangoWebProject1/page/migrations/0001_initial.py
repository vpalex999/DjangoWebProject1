# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-09-04 16:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Good',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Краткое описание')),
                ('in_stock', models.BooleanField(db_index=True, default=True, verbose_name='В наличии')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='page.Category')),
            ],
        ),
    ]