from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404, JsonResponse,response
from django.contrib import messages
from django.db.models import Count, Q
from django.contrib.auth.decorators import login_required
from .models import Song, Rate, Play
from core.models import MyUser
from .forms import SongForm, RateForm
from .filters import SongFilter
from music.conf import anti_spider


@login_required
def song_list(request):

    if anti_spider(request):
        return response.HttpResponseNotFound(
            content="<h1>Not Found</h1><p>The requested URL " +
                    request.path_info +
                    " was not found on this server.</p>"
        )

    f = SongFilter(request.GET, queryset=Song.objects.all())

    context = {
        "filter": f,
    }

    return render(request, "songs/song_list.html", context)


@login_required
def song_detail(request, id):

    if anti_spider(request):
        return response.HttpResponseNotFound(
            content="<h1>Not Found</h1><p>The requested URL " +
                    request.path_info +
                    " was not found on this server.</p>"
        )

    song = get_object_or_404(Song, pk=id)

    try:
        rate = Rate.objects.get(user=request.user.myuser, song=song)
        scores = [False for i in range(5)]
        scores[rate.score-1] = True
    except Rate.DoesNotExist:
        scores = [False for i in range(5)]
        scores[0] = True

    context = {
        "song": song,
        "scores": scores,
    }

    # return HttpResponse("song details!")
    return render(request, "songs/song_detail.html", context)


@login_required
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
        song.play_count=song.play_count+1
        song.save()
    elif ptype == '2':
        play = Play(user=request.user.myuser,
                    song=song,
                    ptype=ptype)
        play.save()
        song.play_count = song.play_count + 1
        song.save()
    else:
        raise Http404

    context = {
        "song": song,
        "artist": song.artists,
    }
    return render(request, "songs/song_play.html", context)


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


@login_required
def song_torate(request):
    user = request.user.myuser
    if request.method == 'POST':
        songid = request.POST.get('songid', '')
        score = request.POST.get('score', '')
        try:
            rate = Rate.objects.get(user=user, song_id=songid)
            diff = int(score) - rate.score
            cnt = 0
        except Rate.DoesNotExist:
            rate = Rate(user=user, song_id=songid, score=1)
            diff = score
            cnt = 1
        song = Song.objects.get(pk=songid)
        song.score = song.score + int(diff)
        song.count = song.count + int(cnt)
        song.save()
        rate.score = score
        rate.save()

        return JsonResponse({'state': 1})

    return JsonResponse({'state': -1})


@login_required
def play_history(request):
    if anti_spider(request):
        return response.HttpResponseNotFound(
            content="<h1>Not Found</h1><p>The requested URL " +
                    request.path_info +
                    " was not found on this server.</p>"
        )

    user = request.user.myuser
    play = Play.objects.filter(user=user)
    song = [p.song for p in play]
    timestamp = [p.timestamp for p in play]
    context = {
        "song": song,
        "timestamp": timestamp,
    }
    return render(request, "core/play_history.html", context)















