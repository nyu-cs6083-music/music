from django.db import models
from django.core.urlresolvers import reverse
from music import conf
from embed_video.fields import EmbedVideoField

class Song(models.Model):
    # song name
    name = models.CharField(max_length=100)
    # song length
    length = models.DurationField()
    # song artists
    artists = models.ForeignKey("artists.Artist", related_name="song")
    # song url
    video = EmbedVideoField(verbose_name='My video',
                            help_text='This is a help text')
    # song time
    year_released = models.DateField(max_length=8, auto_now=True)

    # song rate number
    count = models.IntegerField(default=0)
    # song rate score
    score = models.IntegerField(default=0)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    def get_artist_names(self):
        return self.artists.name

    def get_absolute_url(self):
        return reverse("songs:song_detail", kwargs={"id":self.pk})

    def get_average_rate(self):
        return str(1.0*self.score/self.count if self.count != 0 else 0.0)

class Rate(models.Model):
    user = models.ForeignKey('core.MyUser', related_name='rate')
    song = models.ForeignKey('Song', related_name='rate')
    score = models.IntegerField(default=0, choices=conf.RATESCORE.choice())
    timestamp = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('user', 'song')


class Play(models.Model):
    user = models.ForeignKey('core.MyUser', related_name='play')
    song = models.ForeignKey('Song', related_name='play')
    ptype = models.IntegerField(default=2, choices=conf.SOURCETYPE.choice())
    sourceid = models.IntegerField(null=True)
    timestamp = models.DateTimeField(auto_now=True)