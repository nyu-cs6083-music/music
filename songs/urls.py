from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.song_list, name="song_list"),
    url(r'^(?P<id>\d+)/detail$', views.song_detail, name="song_detail"),
    url(r'^(?P<id>\d+)/(?P<ptype>\d+)/(?P<sid>\d+)/play$', views.song_play, name="song_play"),
    url(r'^(?P<id>\d+)/edit/$', views.song_edit, name="song_edit"),
    url(r'^new/$', views.song_new, name="song_new"),
    url(r'^play/(?P<id>\d+)$', views.play_list, name="play_list"),
]

