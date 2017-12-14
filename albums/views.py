from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from .models import Album
from .filters import AlbumFilter
from django.http import response
from music.conf import anti_spider
from django.contrib.auth.decorators import login_required


@login_required
def album_list(request):

    if anti_spider(request):
        return response.HttpResponseNotFound(
            content="<h1>Not Found</h1><p>The requested URL " +
                    request.path_info +
                    " was not found on this server.</p>"
        )


    f = AlbumFilter(request.GET, queryset=Album.objects.all())
    context = {
        "filter": f,

    }

    return render(request, "albums/album_list.html", context)


@login_required
def album_detail(request, id):

    if anti_spider(request):
        return response.HttpResponseNotFound(
            content="<h1>Not Found</h1><p>The requested URL " +
                    request.path_info +
                    " was not found on this server.</p>"
        )
    album = get_object_or_404(Album, pk=id)

    context = {
        "album": album,
        "songs": album.track.all(),


    }

    return render(request, "albums/album_detail.html", context)
