from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.playlist_list, name='playlist_list'),
    url(r'^playlist_edit/$', views.playlist_edit, name='playlist_edit'),
    url(r'^(?P<id>\d+)/$', views.playlist_detail, name="playlist_detail"),
]
