# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-15 14:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Auction', '0009_auto_20170115_1437'),
    ]

    operations = [
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(upload_to='')),
                ('tittle', models.CharField(max_length=64)),
            ],
        ),
    ]
