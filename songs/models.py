from django.db import models
from django.core.urlresolvers import reverse
from music import conf

class Song(models.Model):
    #song name
    name = models.CharField(max_length=100)
    #song length
    length = models.DurationField()
    #song track number
    track_number = models.IntegerField()
    #song artists
    artists = models.ForeignKey("artists.Artist")

    class Meta:
        ordering = ["name"]

    def __unicode__(self):
        return self.name

    def get_artist_names(self):
        artist_names = [artist.name for artist in self.artists.all()]
        return ", ".join(artist_names)

    def get_absolute_url(self):
        return reverse("songs:song_detail", kwargs={"id":self.pk})

class Rate(models.Model):
    user = models.ForeignKey('core.MyUser', related_name='rate')
    song = models.ForeignKey('Song', related_name='rate')
    score = models.IntegerField(default=0, choices=conf.RATESCORE.choice())
    timestamp = models.DateTimeField()