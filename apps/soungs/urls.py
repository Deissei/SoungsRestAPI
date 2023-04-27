from rest_framework.routers import DefaultRouter

from apps.soungs.views import (
    SoungViewSet,
    AlbumViewSet,
    PlaylistViewSet
)

router = DefaultRouter()
router.register('soungs', SoungViewSet, basename='soung')

router.register('albums', AlbumViewSet, basename='album')
router.register('playlist', PlaylistViewSet, basename='playlist')

urlpatterns = router.urls
