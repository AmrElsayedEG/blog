# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-19 15:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('details', models.TextField()),
                ('review', models.TextField()),
            ],
        ),
    ]
