from django.conf.urls import include, url
from django.contrib import admin
from Auction import views
from django.views.generic import ListView

urlpatterns = [
    url(r'^create/$', views.createAuction, name='Create_Auction',),
    url(r'^create/Live$', views.createLiveAuction, name='Create_LiveAuction',),
    url(r'^create/product/$', views.create_product, name='Create_Product',),

    url(r'^edit/product/(?P<pk>\d+)$', views.edit_product, name='Edit_Product',),

    url(r'^edit/(?P<pk>\d+)$', views.Edit_Auction.as_view(), name='Edit_Auction',),

    url(r'^filter/car/$', views.index_car_filter, name='car_filter',),

    url(r'^filter/part/$', views.index_part_filter, name='part_filter',),

    url(r'^view/(?P<pk>\d+)$', views.auction_details, name='View_Auction',),

    url(r'^Stop/Auction/(?P<pk>\d+)$',views.stop_auction,name='Stop_Auction',),


    url(r'^view/product/(?P<pk>\d+)$',
        views.product_details, name='product_details',),

    url(r'^pay/$', views.payment_page, name='payment_page',),

    url(r'^upload/Picture$', views.pictures_upload, name="Upload_Picture",),

    url(r'^delete/product/(?P<pk>\d+)$',
        views.delete_product, name='product_delete',),
    url(r'^bid/(?P<pk>\d+)$',
        views.bid_auction, name='Bid_Auction',),
    url(r'^bid/update/(?P<pk>\d+)$',
        views.update_bid_auction, name='Update_Bid_Auction',),
]
