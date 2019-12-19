# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-19 08:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_locality_municipality'),
    ]

    operations = [
        migrations.AlterField(
            model_name='locality',
            name='municipality',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='dashboard.Municipality', verbose_name='Муниципальное образование'),
        ),
        migrations.AlterField(
            model_name='objectinfo',
            name='category_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='dashboard.CategoryType', verbose_name='Категория объекта'),
        ),
        migrations.AlterField(
            model_name='objectinfo',
            name='gen_species_appearance',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='dashboard.Species', verbose_name='Общая видовая принадлежность'),
        ),
        migrations.AlterField(
            model_name='objectinfo',
            name='locality',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='municipality', chained_model_field='municipality', null=True, on_delete=django.db.models.deletion.SET_NULL, to='dashboard.Locality', verbose_name='Населенный пункт'),
        ),
        migrations.AlterField(
            model_name='objectinfo',
            name='municipality',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='dashboard.Municipality', verbose_name='Муниципальное образование'),
        ),
        migrations.AlterField(
            model_name='objectinfo',
            name='object_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='dashboard.ObjectType', verbose_name='Тип объекта'),
        ),
    ]
