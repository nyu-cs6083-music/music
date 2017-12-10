from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from django.core.urlresolvers import reverse
from .models import Playlist
from .filters import PlaylistFilter
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
    f = PlaylistFilter(request.GET, queryset=playlists)
    context = {
        "playlists":playlists,
        "creator": creator,
        "filter": f,
    }

    return render(request, "playlists/playlist_list.html", context)


def playlist_detail(request, id):

    try:
        playlist = Playlist.objects.get(pk=id)
    except Playlist.DoesNotExist:
        raise Http404
    user = request.user.myuser
    creator = playlist.creator
    if creator.pk == user.pk:
        editable = True
    else:
        editable = False
    context = {
        "playlist": playlist,
        "songs": playlist.song.all(),
        "editable": editable,
    }

    return render(request, "playlists/playlist_detail.html", context)


def playlist_new(request):
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

def playlist_edit (request, id):
    playlist = get_object_or_404(Playlist, pk=id)

    if request.method == "POST":
        form = PlaylistForm(request.POST, instance=playlist)
        if form.is_valid():
            playlist = form.save()
            messages.success(request, "Song updated!")
            return redirect("playlists:playlist_detail", id=playlist.pk)

    else:
        form = PlaylistForm(instance=playlist)

    context = {
        "form": form,
        "playlist": playlist,
    }

    return render(request, "playlists/playlist_edit.html", context)