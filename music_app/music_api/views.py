from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Artist, Album, Song
from .serializers import ArtistSerializer, AlbumSerializer, SongSerializer

class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.none()
    serializer_class = ArtistSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return Artist.objects.prefetch_related('albums').all()

class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.none()
    serializer_class = AlbumSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return Album.objects.select_related('artist').prefetch_related('songs').all()

class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.none()
    serializer_class = SongSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Song.objects.select_related('album', 'album__artist')
