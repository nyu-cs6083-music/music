from django.shortcuts import render, get_object_or_404, redirect
from django.http import response
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from music.conf import anti_spider
from .models import Artist
from core.models import Like
from .forms import ArtistForm


@login_required
def artist_list(request):

    if anti_spider(request):
        return response.HttpResponseNotFound(
            content="<h1>Not Found</h1><p>The requested URL " +
                    request.path_info +
                    " was not found on this server.</p>"
        )

    artists = Artist.objects.all()
    # user=request.user
    # i=0;
    # state=[]
    # for artist in artists:
    #     state.append('unlike')
    #
    # for artist in artists:
    #     if Like.objects.filter(user=user.myuser, artist=artist):
    #         state[i] = 'like'
    #     i=i+1

    query = request.GET.get("q")
    if query:
        artists = artists.filter(
            Q(name__icontains=query)
        )
        artists = artists.distinct()

    context = {
        "artists": artists,
    }
    # return HttpResponse("Here be I.")
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























