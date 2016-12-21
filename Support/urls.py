from django.views.generic import ListView
from django.conf.urls import include, url
from Support import views
urlpatterns = [
    url(r'^main/create/ticket/$', views.create_ticket, name='Create_ticket',),
    url(r'^main/$',views.support_page,name='Support',),
]
