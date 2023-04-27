from django.db import models


class GenreArtist(models.Model):
    title = models.CharField(max_length=70)

    def __str__(self):
        return self.title


class Artist(models.Model):
    alias = models.CharField(max_length=100)
    full_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='Photo/Artists/')

    short_biography = models.TextField(max_length=500)
    description_artist = models.TextField()

    genres = models.ManyToManyField(GenreArtist, related_name='genres_artist')

    def __str__(self):
        return self.alias
