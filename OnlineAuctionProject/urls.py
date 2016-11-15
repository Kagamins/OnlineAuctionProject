
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('allauth.urls',)),
    url(r'^auction/',include('Auction.urls',)),
    url(r'^',TemplateView.as_view(template_name='Index.html')),
]
