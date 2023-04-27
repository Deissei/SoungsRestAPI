from rest_framework import serializers

from apps.artists.models import Artist


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ('id', 'alias', 'full_name', 'image', 'short_biography', 'description_artist', 'genres')