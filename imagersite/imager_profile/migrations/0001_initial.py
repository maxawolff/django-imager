# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ImagerProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('website', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=50)),
                ('bio', models.CharField(max_length=500)),
                ('phone', models.CharField(max_length=10)),
                ('fee', models.FloatField()),
                ('services', models.CharField(choices=[['WD', 'Weddings'], ['SCH', 'School Photos'], ['CEL', 'Celebrations']], max_length=30)),
                ('photo_styles', models.CharField(choices=[['BW', 'black and white'], ['PT', 'portrait'], ['FAM', 'family']], max_length=30)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
            managers=[
                ('active', django.db.models.manager.Manager()),
            ],
        ),
    ]
