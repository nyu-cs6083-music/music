from django.shortcuts import render, redirect
from django.http import Http404
from django.core.urlresolvers import reverse
from .models import Playlist
from core.models import MyUser
from .forms import PlaylistForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required
def playlist_list(request, uid):
    if uid == '0':
        playlists = Playlist.objects.all()
        creator = None
    else:
        playlists = Playlist.objects.filter(creator_id=uid)
        creator = MyUser.objects.get(pk=uid)
    context = {
        "playlists":playlists,
        "creator": creator,
    }

    return render(request, "playlists/playlist_list.html", context)


def playlist_detail(request, id):

    try:
        playlist = Playlist.objects.get(pk=id)
    except Playlist.DoesNotExist:
        raise Http404
    context = {
        "playlist": playlist,
        "songs": playlist.song.all(),
    }

    return render(request, "playlists/playlist_detail.html", context)


def playlist_edit(request):
    if request.method == "POST":
        form = PlaylistForm(request.POST)
        if form.is_valid():
            playlist = form.save()
            playlist.creator = request.user.myuser
            playlist.save()
            messages.success(request, "Playlist added!")
            return redirect("playlists:playlist_detail", id=playlist.pk)
    else:
        form = PlaylistForm()

    context = {
        "form":form,
    }

    return render(request, "playlists/playlist_edit.html", context)
