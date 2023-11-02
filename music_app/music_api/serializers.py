from rest_framework import serializers
from .models import Artist, Album, Song

class SimpleSongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id', 'name']

class SimpleAlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ['id', 'name', 'year']

class SimpleArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['id', 'name']

class SimpleSongAlbumSerializer(serializers.ModelSerializer):
    artist = SimpleArtistSerializer(read_only=True)
    class Meta:
        model = Album
        fields = ['id', 'name', 'year', 'artist']

class SongSerializer(serializers.ModelSerializer):
    album = SimpleSongAlbumSerializer(read_only=True)
    class Meta:
        model = Song
        fields = ['id', 'name', 'album']

class AlbumSerializer(serializers.ModelSerializer):
    artist = SimpleArtistSerializer(read_only=True)
    songs = SimpleSongSerializer(many=True, read_only=True)

    class Meta:
        model = Album
        fields = ['id', 'name', 'year', 'artist', 'songs']

class ArtistSerializer(serializers.ModelSerializer):
    albums = SimpleAlbumSerializer(many=True, read_only=True)
    class Meta:
        model = Artist
        fields = ['id', 'name', 'albums']
