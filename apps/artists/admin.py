from django.contrib import admin

from apps.artists.models import Artist, GenreArtist


admin.site.register(Artist)
admin.site.register(GenreArtist)
