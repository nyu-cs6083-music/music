from django import forms
from .models import Playlist
from songs.models import Song


class PlaylistForm(forms.ModelForm):

    class Meta:
        model = Playlist
        fields = (
            "playlist_name",
            "song")

    def __init__(self, *args, **kwargs):
        super(PlaylistForm, self).__init__(*args, **kwargs)
        self.fields["song"].widget = forms.widgets.CheckboxSelectMultiple()
        self.fields["song"].help_text = ""
        self.fields["song"].queryset = Song.objects.all()

"""
    def save(self, user, commit=True):
        playlist = super(PlaylistForm, self).save(commit=False)
        print(playlist.__dict__)
        playlist.creator = user
        playlist.save()
        return playlist
"""