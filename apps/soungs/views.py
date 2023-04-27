from rest_framework import viewsets
from rest_framework.validators import ValidationError

from rest_framework.permissions import IsAuthenticated

from apps.soungs.serializers import (
    SoungSerializer, 
    AlbumSerializer, 
    PlaylistSerializer
)

from apps.soungs.models import (
    Soung,
    Album,
    Playlist
)


class SoungViewSet(viewsets.ModelViewSet):
    queryset = Soung.objects.all()
    serializer_class = SoungSerializer
    permission_classes = [IsAuthenticated]
    

class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    permission_classes = [IsAuthenticated]


class PlaylistViewSet(viewsets.ModelViewSet):
    serializer_class = PlaylistSerializer

    def get_queryset(self):
        return Playlist.objects.filter(user=self.request.user)

    def get_permissions(self):
        if self.action in ('GET', 'UPDATE', 'DELETE'):
            ValidationError("Это не ваш Плейлист")
        return [IsAuthenticated()]
    
    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
