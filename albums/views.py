from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from . models import Album
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

    albums = Album.objects.all()

    context = {
        "albums":albums

    }

    return render(request, "albums/album_list.html", context)


def album_detail(request, id):

    if anti_spider(request):
        return response.HttpResponseNotFound(
            content="<h1>Not Found</h1><p>The requested URL " +
                    request.path_info +
                    " was not found on this server.</p>"
        )

    album = Album.objects.get(pk=id)

    context = {
        "album": album

    }

    return render(request, "albums/album_detail.html", context)


def album_edit(request):
    albums = Album.objects.all()

    context = {
        "albums":albums

    }

    return render(request, "albums/album_list.html", context)
