from django.contrib import admin
from . models import Song, Play, Rate

class SongAdmin(admin.ModelAdmin):
    search_fields = [
        "name",
    ]

    list_display = [
        "name",
        "get_artist_names",
        "length",
    ]

class PlayAdmin(admin.ModelAdmin):
    list_display = [
        "user",
        "song",
        "timestamp",
    ]

class RateAdmin(admin.ModelAdmin):
    list_display = [
        "user",
        "song",
        "score",
    ]

admin.site.register(Song, SongAdmin)
admin.site.register(Play, PlayAdmin)
admin.site.register(Rate, RateAdmin)

