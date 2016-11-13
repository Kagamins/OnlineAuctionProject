from django.conf.urls import include, url
from django.contrib import admin
from Auction import views
from django.views.generic import ListView

urlpatterns = [
    url(r'^create/',views.Create_Auction.as_view(),name='Create_Auction' ,),
    url(r'^edit/(?P<pk>\d+)$',views.Edit_Auction.as_view(),name='Edit_Auction',),
    url(r'^bid/(?P<auction_id>]\d+)$',views.Bid_Auction.as_view(),name='Bid_Auction',),

]
