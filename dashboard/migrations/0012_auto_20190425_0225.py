# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-04-24 23:25
from __future__ import unicode_literals

import dashboard.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0011_auto_20190407_2233'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'verbose_name': 'Фотография объекта', 'verbose_name_plural': 'Фотографии объекта'},
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(max_length=500, upload_to=dashboard.models.photo_path),
        ),
        migrations.AlterField(
            model_name='image',
            name='objectinfo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='dashboard.ObjectInfo'),
        ),
    ]
