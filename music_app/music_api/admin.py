from django.contrib import admin
from .models import Artist, Album, Song

@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    search_fields = ('name',)

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'year', 'artist',)
    list_filter = ('year', 'artist',)
    search_fields = ('name', 'artist__name',)

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'album',)
    list_filter = ('album__year', 'album__artist',)
    search_fields = ('name', 'album__name', 'album__artist__name',)
