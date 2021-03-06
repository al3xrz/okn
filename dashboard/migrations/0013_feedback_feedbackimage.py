# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-05-10 17:04
from __future__ import unicode_literals

import dashboard.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0012_auto_20190425_0225'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('o_id', models.IntegerField(verbose_name='ID объекта')),
                ('o_url', models.CharField(blank=True, max_length=200, null=True, verbose_name='Путь к объекту')),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Имя')),
                ('email', models.CharField(blank=True, max_length=100, null=True, verbose_name='Email')),
                ('text', models.TextField(blank=True, null=True, verbose_name='Сообщение')),
            ],
        ),
        migrations.CreateModel(
            name='FeedbackImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(max_length=500, upload_to=dashboard.models.photo_path_2)),
                ('feedback', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='dashboard.Feedback')),
            ],
            options={
                'verbose_name': 'Загруженная фотография',
                'verbose_name_plural': 'Загруженные фотографии',
            },
        ),
    ]
