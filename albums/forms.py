from django import forms

from .models import Album

class AlbumForm(forms.ModelForm):

    class Meta:
        model = Album
        fields = ("album_name", "year_released", "track")