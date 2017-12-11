from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from django.contrib import messages
from django.db.models import Count, Q
from django.contrib.auth.decorators import login_required
from .models import Song, Rate, Play
from core.models import MyUser
from .forms import SongForm
from django.http import response
from music.conf import anti_spider


@login_required
def song_list(request):

    if anti_spider(request):
        return response.HttpResponseNotFound(
            content="<h1>Not Found</h1><p>The requested URL " +
                    request.path_info +
                    " was not found on this server.</p>"
        )

    songs = Song.objects.all()

    query = request.GET.get("q")
    if query:
        # artists = Artist.objects.filter(name__icontains=query)
        songs = songs.filter(
            Q(name__icontains=query) 
            # Q(artists__in=artists)
        )
        songs = songs.distinct()

    context = {
        "songs": songs,
    }

    return render(request, "songs/song_list.html", context)


def song_detail(request, id):

    if anti_spider(request):
        return response.HttpResponseNotFound(
            content="<h1>Not Found</h1><p>The requested URL " +
                    request.path_info +
                    " was not found on this server.</p>"
        )

    song = get_object_or_404(Song, pk=id)
    context = {
        "song": song,
    }

    # return HttpResponse("song details!")
    return render(request, "songs/song_detail.html", context)


def song_play(request, id, ptype, sid):
    try:
        song = Song.objects.get(pk=id)
    except Song.DoesNotExist:
        raise Http404

    if ptype == '1' or ptype == '0':
        play = Play(user=request.user.myuser,
                    song=song,
                    ptype=ptype,
                    sourceid=sid)
        play.save()
    elif ptype == '2':
        play = Play(user=request.user.myuser,
                    song=song,
                    ptype=ptype)
        play.save()
    else:
        raise Http404

    context = {
        "song": song,
        "artist": song.artists,
    }
    return render(request, "songs/song_play.html", context)


def song_new(request):
    if request.method == "POST":
        form = SongForm(request.POST)
        if form.is_valid():
            song = form.save()
            messages.success(request, "Song added!")
            return redirect("songs:song_detail", id=song.pk)
    else:
        form = SongForm()

    context = {
        "form":form,
    }

    return render(request, "songs/song_edit.html", context)


def song_edit (request, id):
    song = get_object_or_404(Song, pk=id)

    if request.method == "POST":
        form = SongForm(request.POST, instance=song)
        if form.is_valid():
            song = form.save()
            messages.success(request, "Song updated!")
            return redirect("songs:song_detail", id=song.pk)

    else: 
        form = SongForm(instance=song)

    context = {
        "form": form, 
        "song": song,
    }

    return render(request, "songs/song_edit.html", context)


@login_required
def play_list(request, id):

    try:
        user = MyUser.objects.get(pk=id)
    except MyUser.DoesNotExist:
        raise Http404

    plays = Play.objects.filter(user_id=id)

    context = {
        "plays": plays,
        "user": user,
    }

    return render(request, "songs/play_list.html", context)




















