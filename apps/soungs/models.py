from django.db import models

from apps.artists.models import Artist


class Soung(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='artist_soung')
    title = models.CharField(max_length=100, unique=True)
    duration = models.IntegerField(default=1)

    soung_file = models.FileField(upload_to='soungs/')

    def __str__(self):
        return self.title


class Album(models.Model):
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField()

    soungs = models.ManyToManyField(Soung, related_name='soungs_album')

    # social links
    facebook = models.CharField(max_length=200, null=True, blank=True)
    twitter = models.CharField(max_length=200, null=True, blank=True)
    vkontact = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.title
