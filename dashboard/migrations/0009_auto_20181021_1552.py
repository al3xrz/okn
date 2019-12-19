# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-21 12:52
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0008_auto_20181021_1547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='objectinfo',
            name='locality',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='municipality', chained_model_field='municipality', null=True, on_delete=django.db.models.deletion.SET_NULL, to='dashboard.Locality', verbose_name='Населенный пункт'),
        ),
    ]