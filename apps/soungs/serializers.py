from rest_framework import serializers

from django.contrib.auth.models import User

from apps.soungs.models import (
    Soung,
    Album,
    Playlist
)


class SoungSerializer(serializers.ModelSerializer):
    class Meta:
        model = Soung
        fields = ('id', 'artist', 'title', 'duration', 'soung_file', 'point_listening')


class AlbumSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Album
        fields = ('id', 'title', 'description', 'soungs', 'facebook', 'twitter', 'vkontact')


class PlaylistSerializer(serializers.ModelSerializer):
    # user = serializers.SlugRelatedField('user', )
    
    class Meta:
        model = Playlist
        fields = ('id', 'title', 'soungs')