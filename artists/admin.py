from django.contrib import admin

from . models import Artist
from songs.models import Song

class SongInline(admin.StackedInline):
    model = Song
    can_delete = False

class ArtistAdmin (admin.ModelAdmin):
    inlines = (SongInline, )
    list_display = (
        "name",
    )

admin.site.register(Artist, ArtistAdmin)

