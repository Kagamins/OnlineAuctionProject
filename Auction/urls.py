from django.conf.urls import include, url
from django.contrib import admin
from Auction import views
from django.views.generic import ListView

urlpatterns = [
    url(r'^create/$', views.createAuction, name='Create_Auction',),
    url(r'^create/product/$', views.create_product, name='Create_Product',),
    url(r'^edit/(?P<pk>\d+)$', views.Edit_Auction.as_view(), name='Edit_Auction',),
    url(r'^view/(?P<pk>\d+)$',views.View_Auction.as_view(), name='View_Auction',),
    url(r'^view/product/(?P<pk>\d+)$', views.product_details, name='product_details',),

    url(r'^bid/(?P<pk>\d+)$',
        views.bid_auction, name='Bid_Auction',),
]
