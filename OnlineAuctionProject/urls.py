
from django.conf.urls import include, url
from django.contrib import admin
from Auction import views
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('allauth.urls',)),
    url(r'^auction/',include('Auction.urls',)),
    url(r'^User/',include('Users.urls',)),
    url(r'^Support/',include('Support.urls',)),
    url(r'^',views.index_page,name='home',),
]
