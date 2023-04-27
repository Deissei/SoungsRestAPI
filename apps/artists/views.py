from rest_framework.viewsets import ModelViewSet

from rest_framework.permissions import IsAuthenticated

from apps.artists.serializers import ArtistSerializer
from apps.artists.models import Artist


class ArtistViewSet(ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    permission_classes = [IsAuthenticated]
