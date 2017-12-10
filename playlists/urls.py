from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^(?P<uid>\d+)/$', views.playlist_list, name='playlist_list'),
    url(r'^new/$', views.playlist_new, name='playlist_new'),
    url(r'^(?P<id>\d+)/detail$', views.playlist_detail, name="playlist_detail"),
    url(r'^(?P<id>\d+)/edit/$', views.playlist_edit, name="playlist_edit"),
]
