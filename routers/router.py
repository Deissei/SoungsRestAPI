from rest_framework.routers import DefaultRouter

from apps.soungs.views import (
    SoungViewSet,
    AlbumViewSet,
    PlaylistViewSet
)

from apps.artists.views import (
    ArtistViewSet
)

router = DefaultRouter()
router.register('soungs', SoungViewSet, basename='soung')

router.register('albums', AlbumViewSet, basename='album')
router.register('playlist', PlaylistViewSet, basename='playlist')


router.register('artists', ArtistViewSet, basename='artist')

urlpatterns = router.urls
