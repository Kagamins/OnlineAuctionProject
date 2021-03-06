# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-05 10:52
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Auction', '0007_live_auction_auction_bidding_open'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='auction_type',
            field=models.CharField(choices=[('P', 'Premium'), ('F', 'Freemium')], max_length=64, verbose_name='auction_type'),
        ),
        migrations.AlterField(
            model_name='auction',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='bid',
            name='Bidder',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='bid',
            name='Time_of_Bid',
            field=models.TimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='bid',
            name='User_bid',
            field=models.BigIntegerField(help_text='user bidding'),
        ),
        migrations.AlterField(
            model_name='item',
            name='certificate',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='item',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='item',
            name='picture',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='item',
            name='product_type',
            field=models.CharField(choices=[('C', 'Cars'), ('P', 'Parts')], max_length=64, verbose_name='Product_type'),
        ),
        migrations.AlterField(
            model_name='live_auction',
            name='Time_of_Auction',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='live_auction',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
