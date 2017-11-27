# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-27 22:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('imager_images', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='cover',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='imager_images.Photo'),
        ),
        migrations.AlterField(
            model_name='album',
            name='date_modified',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='album',
            name='date_published',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='album',
            name='date_uploaded',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='album',
            name='description',
            field=models.CharField(blank=True, max_length=120),
        ),
        migrations.AlterField(
            model_name='album',
            name='photo',
            field=models.ManyToManyField(blank=True, to='imager_images.Photo'),
        ),
        migrations.AlterField(
            model_name='album',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='imager_profile.ImagerProfile'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='date_modified',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='photo',
            name='date_published',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='photo',
            name='date_uploaded',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='photo',
            name='description',
            field=models.CharField(blank=True, max_length=120),
        ),
        migrations.AlterField(
            model_name='photo',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='imager_profile.ImagerProfile'),
        ),
    ]
