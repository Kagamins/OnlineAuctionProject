# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-05 14:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Auction', '0006_live_auction_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='live_auction',
            name='auction_bidding_open',
            field=models.BooleanField(default=False),
        ),
    ]
