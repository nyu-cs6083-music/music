import django_filters
from .models import Playlist

class PlaylistFilter(django_filters.FilterSet):
    class Meta:
        model = Playlist
        fields = {
            'playlist_name': ['contains'],
            'year_released': ['lt', 'gt'],
        }
