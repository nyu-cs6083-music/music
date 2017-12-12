import django_filters
from .models import Album

class AlbumFilter(django_filters.FilterSet):
    class Meta:
        model = Album
        fields = {
            'year_released': ['lt', 'gt'],
        }
