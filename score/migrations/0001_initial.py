# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-12-28 11:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Students_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('university', models.CharField(max_length=50)),
                ('major', models.CharField(max_length=50)),
                ('english_score', models.IntegerField()),
                ('math_score', models.IntegerField()),
                ('political_score', models.IntegerField()),
                ('major_score', models.IntegerField()),
                ('total_score', models.IntegerField()),
                ('rank', models.IntegerField()),
            ],
        ),
    ]
