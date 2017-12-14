from django.shortcuts import render, get_object_or_404, redirect
from django.http import response, JsonResponse
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from music.conf import anti_spider
from .models import Artist
from core.models import MyUser
from core.models import Like
from .forms import ArtistForm
from django.core.cache import cache


@login_required
def artist_list(request):
    user = request.user.myuser
    if anti_spider(request):
        return response.HttpResponseNotFound(
            content="<h1>Not Found</h1><p>The requested URL " +
                    request.path_info +
                    " was not found on this server.</p>"
        )

    artists = Artist.objects.all()

    query = request.GET.get("q")
    if query:
        artists = artists.filter(
            Q(name__icontains=query)
        )
        artists = artists.distinct()

    datas = cache.get(user.key("like"))
    if not datas:
        datas = map(
            lambda x: {
                "artist": x,
                "status": (True if Like.objects.filter(user=user, artist=x) else False),
            }, artists)
        cache.set(user.key("like"), list(datas), 5 * 60)

    context = {
        "datas": datas,
    }

    return render (request, "artists/artist_list.html", context)


def artist_detail(request, id):

    if anti_spider(request):
        return response.HttpResponseNotFound(
            content="<h1>Not Found</h1><p>The requested URL " +
                    request.path_info +
                    " was not found on this server.</p>"
        )

    artist = get_object_or_404(Artist, pk=id)
    user = request.user
    state = 'unlike'
    if Like.objects.filter(user=user.myuser, artist=artist):
        state = 'like'
    songs = artist.song.all()
    context = {
        "state": state,
        "artist": artist,
        "songs": songs,
    }

    # return HttpResponse("Here are the artists")
    return render (request, "artists/artist_detail.html", context)


def artist_edit(request, id):
    artist = get_object_or_404(Artist, pk=id)

    if request.method == "POST":
        form = ArtistForm(request.POST, instance=artist)
        if form.is_valid():
            # artist=form.save()
            artist = form.save(commit=False)
            artist.save()
            form.save_m2m()

            messages.success(request, "Artist updated!")
            return redirect("artists:artist_detail", id=artist.pk)

    else:
        form = ArtistForm(instance=artist)

    context = {
        "form": form,
        "artist": artist,
    }

    return render(request, "artists/artist_edit.html", context)

def unlike_artist(request):
    userself = request.user.myuser
    if request.method == 'POST':
        artistid = request.POST.get('artistid', '')
        artist = Artist.objects.get(pk=artistid)
        Like.objects.filter(user=userself,artist=artist).delete()

    return JsonResponse({'state': -1})
























