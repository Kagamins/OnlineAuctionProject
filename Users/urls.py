
from django.conf.urls import include, url
from django.contrib import admin
from Users import views
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^create/$',views.create_user_profile,name='Create_User',),
    url(r'^edit/$',views.edit_profile,name='Edit_User',),
    url(r'^Message/Create/$',views.create_message,name='Create_Message',),
    url(r'^Message/Create/(?P<pk>\d+)$',views.create_message_auction,name='Create_Message_Auction',),
    url(r'^view/mypage/$', views.my_page, name='My_Page',),
    url(r'^Messages/View/(?P<pk>\d+)$',views.view_message_details,name='Message_Details',),
    url(r'^Message/ListView$',views.view_message_list,name='Message_List',),
    url(r'^Buying/History$',views.buyer_history,name='Buyer_History',),
    url(r'^Selling/History$',views.seller_history,name='Seller_History',),

]
