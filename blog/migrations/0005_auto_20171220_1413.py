# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-20 12:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20171219_1924'),
    ]

    operations = [
        migrations.CreateModel(
            name='comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('comment', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(default='article-images/default.png', upload_to='article-images'),
        ),
    ]
