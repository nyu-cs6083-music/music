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
        fields = (
            "song",
            "score",)

    def __init__(self, *args, **kwargs):
        super(RateForm, self).__init__(*args, **kwargs)

"""
    def save(self, user, commit=True):
        rate = super(Rate, self).save(commit=False)
        print(rate.__dict__)
        rate.creator = user
        rate.save()
        return rate
"""
  


