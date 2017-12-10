from django.contrib import admin
from . models import Song, Play

class SongAdmin(admin.ModelAdmin):
    search_fields = [
        "name",
    ]

    list_display = [
        "get_artist_names",
        "name", 
        "length",
    ]

class PlayAdmin(admin.ModelAdmin):
    list_display = [
        "user",
        "song",
        "timestamp",
    ]

admin.site.register(Song, SongAdmin)
admin.site.register(Play, PlayAdmin)

