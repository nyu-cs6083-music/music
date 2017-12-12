from django import forms

from .models import Song, Rate
from core.forms import BootstrapFormMixin

class SongForm (BootstrapFormMixin, forms.ModelForm):

    class Meta:
        model = Song
        fields = (
            "name",
            "length",
            "artists",
            "video",
        )


class RateForm(forms.ModelForm):
    class Meta:
        model = Rate
        fields = ("score",)

    def __init__(self, *args, **kwargs):
        super(RateForm, self).__init__(*args, **kwargs)

  


