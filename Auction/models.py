from django.db import models
from django.conf import settings
import os
from decimal import Decimal
from django.core.urlresolvers import *




def get_image_path(instance, filename):
    return os.path.join('photos', str(instance.id), filename)


class item(models.Model):
    CHOICES=(('C','Cars'),('P','Parts'))
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,null=True,blank=True)
    product_name = models.CharField(max_length=18, help_text=('Car_Name'))
    manufacture_year = models.CharField(
        max_length=120, help_text=('E.g.: 2015/2016'))
    picture = models.ImageField(null=True, blank=True)
    product_description = models.TextField()
    certificate = models.ImageField(null=True, blank=True)
    product_type = models.CharField("Product_type",max_length=64 ,choices=CHOICES,null=True)

    def get_absolute_url(self):
        return reverse(
            'Create_Auction',
            kwargs={'user': self.pk})

    def __unicode__(self):
        return u"{} : {}:{}".format(self.product_name, self.manufacture_year, self.product_type)

    def __str__(self):
        return u"{} : {}".format(self.product_name, self.manufacture_year)


class auction(models.Model):
    Choices = (('P','Premium'),('F','Freemium'))
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, null=True, blank=True)
    product = models.ForeignKey(item)
    auction_type = models.CharField("auction_type",max_length=64 ,choices=Choices,null=True)
    auction_date = models.DateField()
    auction_time = models.TimeField()

    def __unicode__(self):
        return u"{} :{} : {}: {} : at {}".format(self.user.username, self.product.product_name, self.product.manufacture_year, self.auction_date, self.auction_time)

    def __str__(self):
        return u"{} :{} : {}: {} : at {}".format(self.user.username, self.product.product_name, self.product.manufacture_year, self.auction_date, self.auction_time)



class live_auction(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,null=True)
    auction = models.ForeignKey(auction)
    Time_of_Auction = models.TimeField(null=True)
    #Live = models.BooleanField(NullBooleanField=True)
    initial_bid = models.BigIntegerField(
        null=True, help_text=("the initial bid"))
    def __str__(self):
        return u"{} : {}  ".format(self.auction, self.initial_bid)
    def __unicode__(self):
        return u"{} : {}  ".format(self.auction, self.initial_bid)
    def get_absolute_url(self):
        return reverse(
            'home')

class bid(models.Model):
    l_auction= models.ForeignKey(live_auction)
    User_bid = models.BigIntegerField(null=True, help_text=("user bidding"))
    Bidder = models.OneToOneField(
            settings.AUTH_USER_MODEL, null=True, blank=True)
    Time_of_Bid = models.TimeField(auto_now=True,null=True)
    def get_absolute_url(self):
        return reverse(
            'home')
    def __str__(self):
        return u'{} : {} : {} : {}'.format(self.l_auction.auction.user.username, self.l_auction.initial_bid, self.User_bid,self.Time_of_Bid)

class Payment(models.Model):
    CHOICES = (('Cash','Cash'),('Knet','Knet'),('Visa','Visa'))
    User = models.OneToOneField(settings.AUTH_USER_MODEL,null=False)
    Amount = models.BigIntegerField(null=False)
    Payment_Method = models.CharField("Payment method",max_length=50,choices=CHOICES)

    def __str__(self):
        return u'{} : {} : {} '.format(self.User.username, self.Amount, self.Payment_Method)
