# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-11 15:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_auto_20180922_1348'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Категория объекта')),
            ],
            options={
                'verbose_name': 'Категория объектов',
                'verbose_name_plural': 'Категории объектов',
            },
        ),
        migrations.CreateModel(
            name='ObjectType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Тип объекта')),
            ],
            options={
                'verbose_name': 'Тип объектов',
                'verbose_name_plural': 'Типы объектов',
            },
        ),
        migrations.AddField(
            model_name='objectinfo',
            name='addr_NPA',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='Адрес в соответствии с НПА'),
        ),
        migrations.AddField(
            model_name='objectinfo',
            name='con_number',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='con_number?'),
        ),
        migrations.AddField(
            model_name='objectinfo',
            name='coordinates',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Координаты'),
        ),
        migrations.AddField(
            model_name='objectinfo',
            name='create_date',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Дата создания'),
        ),
        migrations.AddField(
            model_name='objectinfo',
            name='documents',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='Документы'),
        ),
        migrations.AddField(
            model_name='objectinfo',
            name='photo_url',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='URL фото'),
        ),
        migrations.AddField(
            model_name='objectinfo',
            name='reg_number',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Регистрационный номер'),
        ),
        migrations.AddField(
            model_name='objectinfo',
            name='category_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.CategoryType', verbose_name='Категория объекта'),
        ),
        migrations.AddField(
            model_name='objectinfo',
            name='object_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.ObjectType', verbose_name='Тип объекта'),
        ),
    ]
