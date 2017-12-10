from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from . models import Album
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


@login_required
def album_list(request):
    albums = Album.objects.all()

    context = {
        "albums":albums

    }

    return render(request, "albums/album_list.html", context)


def album_detail(request, id):
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
