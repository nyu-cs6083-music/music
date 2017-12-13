from django.db import models
from django.core.urlresolvers import reverse

class Artist (models.Model):
    #artist name
    name = models.CharField(max_length = 40)
    ArtistDescription = models.TextField()

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("artists:artist_detail", kwargs={"id":self.pk})

