import factory
from factory import django
from faker import Faker
from .models import Artist, Album, Song

fake = Faker()

class ArtistFactory(django.DjangoModelFactory):
    class Meta:
        model = Artist

    name = factory.LazyFunction(fake.name)

class AlbumFactory(django.DjangoModelFactory):
    class Meta:
        model = Album

    name = factory.LazyFunction(fake.word)
    year = factory.LazyFunction(lambda: fake.date_between(start_date='-30y', end_date='today').year)
    artist = factory.SubFactory(ArtistFactory)

class SongFactory(django.DjangoModelFactory):
    class Meta:
        model = Song

    name = factory.LazyFunction(fake.word)
    album = factory.SubFactory(AlbumFactory)
