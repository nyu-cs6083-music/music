from django.shortcuts import render, redirect
from django.http import Http404
from django.core.urlresolvers import reverse
from .models import Playlist
from .forms import PlaylistForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required
def playlist_list(request):
    playlists = Playlist.objects.all()

    context = {
        "playlists":playlists,

    }

    return render(request, "playlists/playlist_list.html", context)


def playlist_detail(request, id):

    try:
        playlist = Playlist.objects.get(pk=id)
    except Playlist.DoesNotExist:
        raise Http404
    songs = playlist.song.all()
    print(len(songs))
    context = {
        "playlist": playlist,
        "songs": playlist.song.all(),
    }

    return render(request, "playlists/playlist_detail.html", context)


def playlist_edit(request):
    if request.method == "POST":
        form = PlaylistForm(request.POST)
        if form.is_valid():
            #playlist = form.save(request.user.myuser)
            playlist = form.save()
            print(playlist.__dict__)
            playlist.creator = request.user.myuser
            playlist.save()
            print(playlist.__dict__)
            print("contain:", len(playlist.song.all()))
            messages.success(request, "Playlist added!")
            return redirect("playlists:playlist_detail", id=playlist.pk)
    else:
        form = PlaylistForm()

    context = {
        "form":form,
    }

    return render(request, "playlists/playlist_edit.html", context)
