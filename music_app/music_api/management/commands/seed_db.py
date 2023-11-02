from django.core.management.base import BaseCommand
from music_api.factory import ArtistFactory, AlbumFactory, SongFactory
import random

class Command(BaseCommand):
    help = 'Seeds the database with artists, albums, and songs'

    def handle(self, *args, **kwargs):
        artists = ArtistFactory.create_batch(20)

        for artist in artists:
            albums = AlbumFactory.create_batch(
                size=random.randint(5, 15), 
                artist=artist
            )
            for album in albums:
                SongFactory.create_batch(
                    size=random.randint(10, 20), 
                    album=album,
                )

        self.stdout.write(self.style.SUCCESS('Successfully seeded the database.'))
